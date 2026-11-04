"""Static checks on a game bundle directory (stdlib only, no browser)."""
import gzip, re
from pathlib import Path

TEXT = {".html", ".htm", ".js", ".mjs", ".css", ".json"}
SKIP_DIRS = {".git", "node_modules", ".github", "__MACOSX"}
SKIP_FILES = {".DS_Store"}
# known ad/analytics SDK hosts and globals (a portal that sells its own ads forbids these)
AD_SDKS = {"googlesyndication.com": "AdSense", "imasdk.googleapis.com": "Google IMA", "doubleclick.net": "DoubleClick",
           "adinplay": "AdInPlay", "applixir": "AppLixir", "cpmstar": "CPMStar", "admob": "AdMob"}
PORTAL_SDKS = {"sdk.crazygames.com": "CrazyGames SDK", "game-cdn.poki.com": "Poki SDK", "poki-sdk": "Poki SDK",
               "html5.api.gamedistribution.com": "GameDistribution SDK", "playgama-bridge": "Playgama Bridge"}
_SRC = re.compile(r"""<(?:script|link|img|audio|video|source|iframe)\b[^>]*?\b(?:src|href)\s*=\s*["']([^"']+)["']""", re.I)
_CSS_URL = re.compile(r"""url\(\s*["']?([^"')]+)["']?\s*\)""", re.I)
_EXT = re.compile(r"""["'`](https?:)?//([a-z0-9.-]+\.[a-z]{2,})(/[^"'`\s]*)?["'`]""", re.I)


def files_of(root):
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if p.is_file() and not (set(rel.parts[:-1]) & SKIP_DIRS) and p.name not in SKIP_FILES:
            yield p, rel


def gz_len(p):
    try:
        return len(gzip.compress(p.read_bytes(), 6))
    except OSError:
        return 0


def analyze(root, entry="index.html"):
    root = Path(root).resolve()
    rec = {"root_index": (root / entry).is_file()}
    total = count = 0
    non_latin, big = [], []
    abs_paths, remote_scripts, insecure, ext_hosts, ads, sdks = [], [], [], set(), set(), set()
    insecure_strings = set()  # http:// in JS: usually credit links, reported only
    eval_uses = 0
    for p, rel in files_of(root):
        count += 1
        size = p.stat().st_size
        total += size
        if not str(rel).isascii():
            non_latin.append(str(rel))
        if size > 10e6:
            big.append([str(rel), round(size / 1e6, 1)])
        if p.suffix.lower() not in TEXT or size > 8e6:
            continue
        s = p.read_text(errors="replace")
        low = s.lower()
        for k, v in {**AD_SDKS, **PORTAL_SDKS}.items():
            if k in low:
                (ads if k in AD_SDKS else sdks).add(v)
        if p.suffix.lower() in (".html", ".htm", ".css"):
            refs = _SRC.findall(s) + (_CSS_URL.findall(s) if p.suffix.lower() == ".css" else [])
            for u in refs:
                if u.startswith(("data:", "blob:", "#", "mailto:", "javascript:")):
                    continue
                if u.startswith(("http://", "https://", "//")):
                    host = re.sub(r"^(https?:)?//", "", u).split("/")[0]
                    ext_hosts.add(host)
                    if re.search(r"<script\b[^>]*" + re.escape(u), s, re.I):
                        remote_scripts.append(u)
                    if u.startswith("http://"):
                        insecure.append(u)
                elif u.startswith("/"):
                    abs_paths.append(f"{rel}: {u}")
        if p.suffix.lower() in (".js", ".mjs"):
            eval_uses += len(re.findall(r"\beval\s*\(|new\s+Function\s*\(", s))
            for m in _EXT.finditer(s):
                host = m.group(2).lower()
                if not host.endswith((".org", ".w3.org")) or "cdn" in host:
                    ext_hosts.add(host)
                if m.group(1) == "http:" and "w3.org" not in host and "localhost" not in host:
                    insecure_strings.add(m.group(0).strip("\"'`"))
    rec.update({
        "file_count": count, "total_mb": round(total / 1e6, 2), "non_latin_names": len(non_latin),
        "non_latin_examples": non_latin[:5], "big_files": big[:5], "absolute_paths": len(abs_paths),
        "absolute_path_examples": abs_paths[:5], "remote_scripts": len(remote_scripts),
        "remote_script_examples": remote_scripts[:5], "insecure_urls": len(set(insecure)),
        "insecure_examples": sorted(set(insecure))[:5], "insecure_js_strings": sorted(insecure_strings)[:5], "referenced_hosts": sorted(ext_hosts)[:20],
        "foreign_ad_sdks": len(ads), "ad_sdks": sorted(ads), "portal_sdks": sorted(sdks), "eval_uses": eval_uses,
    })
    return rec
