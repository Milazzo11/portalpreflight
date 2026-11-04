<!-- noindex until the publish word (R&D 102a) -->
# Portal Preflight: 20 open-source HTML5 games (2026-11-04)

20 games from GitHub at pinned commits, each run as-is from its repository root. Tool crashes: 0. Each game: Chromium on a throttled 4G link (9 Mbps, 170 ms RTT) with 4x CPU slowdown, served gzip-compressed under a subpath the way portals host it; median of the runs by time to gameplay. Verdicts cite each portal's published rules (see `portalpreflight/portals.py`); a preflight is not a portal's QA decision. These are open-source repos, not the authors' portal submissions: many were never meant for a portal, and a game whose repo needs a build step shows its missing build output as 404s (the scorecard measures what is committed). ttg = first non-blank frame with the network quiet for 1 s (engine-agnostic; a title screen counts).

| Game | CrazyGames | Poki | Playgama | Reddit Devvit Web | Any portal | ttg s | initial MB | external req |
|---|---|---|---|---|---|---|---|---|
| [2048](https://github.com/gabrielecirulli/2048/tree/478b6ec346) | READY | READY | READY | READY | FIXES | 1.05 | 0.07 | 0 |
| [hextris](https://github.com/hextris/hextris/tree/3f4847dc8f) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 5.23 | 0.26 | 20 |
| [clumsy-bird](https://github.com/ellisonleao/clumsy-bird/tree/fae3d487d5) | READY | READY | READY | READY | FIXES | 2.26 | 1.51 | 0 |
| [floppybird](https://github.com/nebez/floppybird/tree/efd2c7f740) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 1.78 | 0.12 | 2 |
| [javascript-tetris](https://github.com/jakesgordon/javascript-tetris/tree/e5c0c42f7d) | READY | READY | READY | READY | FIXES | 0.7 | 0.05 | 0 |
| [javascript-pong](https://github.com/jakesgordon/javascript-pong/tree/ca3240536e) | READY | READY | READY | READY | FIXES | 1.38 | 0.03 | 0 |
| [javascript-breakout](https://github.com/jakesgordon/javascript-breakout/tree/eed59e2aff) | READY | READY | READY | READY | FIXES | 1.23 | 0.22 | 0 |
| [javascript-racer](https://github.com/jakesgordon/javascript-racer/tree/3e8a060b59) | READY | READY | READY | READY | FIXES | 0.57 | 0.0 | 0 |
| [javascript-boulderdash](https://github.com/jakesgordon/javascript-boulderdash/tree/61f0bb5978) | READY | READY | READY | READY | FIXES | 1.26 | 0.02 | 0 |
| [javascript-gauntlet](https://github.com/jakesgordon/javascript-gauntlet/tree/2f9020dc64) | READY | READY | READY | READY | FIXES | 4.74 | 7.42 | 0 |
| [pacman](https://github.com/daleharvey/pacman/tree/3acc5e2bb1) | READY | READY | READY | READY | READY | 1.8 | 0.1 | 0 |
| [Astray](https://github.com/wwwtyro/Astray/tree/d3c4f61f2c) | BLOCKED | READY | READY | READY | BLOCKED | 3.34 | 0.18 | 0 |
| [adarkroom](https://github.com/doublespeakgames/adarkroom/tree/1fada4620b) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 4.49 | 3.01 | 4 |
| [Captain-Rogers](https://github.com/EnclaveGames/Captain-Rogers/tree/5b4336d668) | READY | READY | READY | READY | FIXES | 5.07 | 1.46 | 0 |
| [radius-raid-js13k](https://github.com/jackrugile/radius-raid-js13k/tree/361ab51665) | READY | READY | READY | READY | FIXES | 3.5 | 0.02 | 0 |
| [HexGL](https://github.com/BKcore/HexGL/tree/6addc95a2f) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 2.12 | 0.76 | 2 |
| [q1k3](https://github.com/phoboslab/q1k3/tree/8ee934856c) | READY | READY | READY | READY | BLOCKED | 4.51 | 0.03 | 0 |
| [Gamedev-Phaser-Content-Kit](https://github.com/end3r/Gamedev-Phaser-Content-Kit/tree/307c14914d) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 0.95 | 0.0 | 1 |
| [untrusted](https://github.com/AlexNisnevich/untrusted/tree/ab4a8ed280) | READY | BLOCKED | BLOCKED | BLOCKED | BLOCKED | 1.77 | 0.22 | 14 |
| [cube-composer](https://github.com/sharkdp/cube-composer/tree/83e5b66b05) | READY | BLOCKED | BLOCKED | BLOCKED | BLOCKED | 0.9 | 0.0 | 4 |

Totals: CrazyGames: BLOCKED 1, READY 19; Poki: BLOCKED 7, READY 13; Playgama: BLOCKED 7, READY 13; Reddit Devvit Web: BLOCKED 7, READY 13; Any portal (hygiene): BLOCKED 4, FIXES 15, READY 1

## Most common findings

| Rule | Games |
|---|---|
| axe-core WCAG 2.2 AA violations = 0 | 18: 2048, Captain-Rogers, Gamedev-Phaser-Content-Kit, HexGL, adarkroom, clumsy-bird, cube-composer, floppybird, hextris, javascript-boulderdash, javascript-breakout, javascript-gauntlet, javascript-pong, javascript-racer, javascript-tetris, q1k3, radius-raid-js13k, untrusted |
| no external requests | 7: Gamedev-Phaser-Content-Kit, HexGL, adarkroom, cube-composer, floppybird, hextris, untrusted |
| no external resources | 7: Gamedev-Phaser-Content-Kit, HexGL, adarkroom, cube-composer, floppybird, hextris, untrusted |
| no external requests (webview CSP) | 7: Gamedev-Phaser-Content-Kit, HexGL, adarkroom, cube-composer, floppybird, hextris, untrusted |
| no http:// resources loaded (portals serve https) | 5: HexGL, adarkroom, cube-composer, hextris, untrusted |
| no remote scripts | 4: adarkroom, floppybird, hextris, untrusted |
| a tap changes the screen (mobile input) | 4: adarkroom, javascript-racer, q1k3, untrusted |
| every file the game requests exists (no 404s) | 4: Astray, cube-composer, q1k3, untrusted |
| no other ad systems | 1: hextris |
| relative paths only | 1: Astray |
| no uncaught JS errors on load | 1: q1k3 |

## Scorecards

### 2048 (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [3] |

| Measure | Value |
|---|---|
| total_mb | 0.6 |
| file_count | 34 |
| initial_mb | 0.07 |
| first_paint_s | 1.05 |
| ttg_s | 1.05 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.4 |
| axe_violations | 3 |
| touch_changes_frame | yes |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### hextris (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [20]; no other ad systems [1] | - |
| Playgama | **BLOCKED** | no external resources [20] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [20]; no remote scripts [1] | - |
| Any portal (hygiene) | **FIXES** | - | no http:// resources loaded (portals serve https) [3]; axe-core WCAG 2.2 AA violations = 0 [8] |

| Measure | Value |
|---|---|
| total_mb | 1.52 |
| file_count | 73 |
| initial_mb | 0.26 |
| first_paint_s | 3.04 |
| ttg_s | 5.23 |
| external_requests | 20 |
| absolute_paths | 0 |
| remote_scripts | 1 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 3 |
| peak_js_heap_mb | 17.2 |
| axe_violations | 8 |
| touch_changes_frame | yes |

**Fix list**

- Bundle these external hosts: ep1.adtrafficquality.google, ep2.adtrafficquality.google, fonts.googleapis.com, googleads.g.doubleclick.net, hextris.io, pagead2.googlesyndication.com
- Third-party ad SDKs found: AdSense (portals with their own ads refuse these)

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### clumsy-bird (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [1] |

| Measure | Value |
|---|---|
| total_mb | 3.99 |
| file_count | 51 |
| initial_mb | 1.51 |
| first_paint_s | 1.55 |
| ttg_s | 2.26 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 6.9 |
| axe_violations | 1 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### floppybird (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [2] | - |
| Playgama | **BLOCKED** | no external resources [2] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [2]; no remote scripts [1] | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [4] |

| Measure | Value |
|---|---|
| total_mb | 0.43 |
| file_count | 54 |
| initial_mb | 0.12 |
| first_paint_s | 1.77 |
| ttg_s | 1.78 |
| external_requests | 2 |
| absolute_paths | 0 |
| remote_scripts | 1 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.0 |
| axe_violations | 4 |
| touch_changes_frame | - |

**Fix list**

- Bundle these external hosts: yummy.nebez.dev

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### javascript-tetris (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [1] |

| Measure | Value |
|---|---|
| total_mb | 0.07 |
| file_count | 5 |
| initial_mb | 0.05 |
| first_paint_s | 0.7 |
| ttg_s | 0.7 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.4 |
| axe_violations | 1 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### javascript-pong (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [11] |

| Measure | Value |
|---|---|
| total_mb | 0.19 |
| file_count | 37 |
| initial_mb | 0.03 |
| first_paint_s | 1.38 |
| ttg_s | 1.38 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.7 |
| axe_violations | 11 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### javascript-breakout (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [1] |

| Measure | Value |
|---|---|
| total_mb | 11.16 |
| file_count | 71 |
| initial_mb | 0.22 |
| first_paint_s | 1.23 |
| ttg_s | 1.23 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.1 |
| axe_violations | 1 |
| touch_changes_frame | yes |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### javascript-racer (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | a tap changes the screen (mobile input) [no]; axe-core WCAG 2.2 AA violations = 0 [5] |

| Measure | Value |
|---|---|
| total_mb | 8.92 |
| file_count | 56 |
| initial_mb | 0.0 |
| first_paint_s | 0.57 |
| ttg_s | 0.57 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.1 |
| axe_violations | 5 |
| touch_changes_frame | no |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### javascript-boulderdash (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [1] |

| Measure | Value |
|---|---|
| total_mb | 0.09 |
| file_count | 22 |
| initial_mb | 0.02 |
| first_paint_s | 1.26 |
| ttg_s | 1.26 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.6 |
| axe_violations | 1 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### javascript-gauntlet (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [12] |

| Measure | Value |
|---|---|
| total_mb | 16.86 |
| file_count | 109 |
| initial_mb | 7.42 |
| first_paint_s | 4.74 |
| ttg_s | 4.74 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.2 |
| axe_violations | 12 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### pacman (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **READY** | - | - |

| Measure | Value |
|---|---|
| total_mb | 0.36 |
| file_count | 25 |
| initial_mb | 0.1 |
| first_paint_s | 0.91 |
| ttg_s | 1.8 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 5.7 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### Astray (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **BLOCKED** | relative paths only [3] | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **BLOCKED** | every file the game requests exists (no 404s) [3] | - |

| Measure | Value |
|---|---|
| total_mb | 1.62 |
| file_count | 11 |
| initial_mb | 0.18 |
| first_paint_s | 3.34 |
| ttg_s | 3.34 |
| external_requests | 0 |
| absolute_paths | 3 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 3 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.8 |
| touch_changes_frame | - |

**Fix list**

- Make paths relative (portals host under a subpath): /ball.png, /brick.png, /concrete.png
- Files requested but missing (404): /ball.png, /brick.png, /concrete.png

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### adarkroom (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [4] | - |
| Playgama | **BLOCKED** | no external resources [4] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [4]; no remote scripts [2] | - |
| Any portal (hygiene) | **FIXES** | - | no http:// resources loaded (portals serve https) [2]; a tap changes the screen (mobile input) [no]; axe-core WCAG 2.2 AA violations = 0 [2] |

| Measure | Value |
|---|---|
| total_mb | 10.28 |
| file_count | 231 |
| initial_mb | 3.01 |
| first_paint_s | 3.06 |
| ttg_s | 4.49 |
| external_requests | 4 |
| absolute_paths | 0 |
| remote_scripts | 2 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 2 |
| peak_js_heap_mb | 12.4 |
| axe_violations | 2 |
| touch_changes_frame | no |

**Fix list**

- Bundle these external hosts: ajax.googleapis.com, www.google-analytics.com, www.googletagmanager.com

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### Captain-Rogers (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [2] |

| Measure | Value |
|---|---|
| total_mb | 10.04 |
| file_count | 188 |
| initial_mb | 1.46 |
| first_paint_s | 4.45 |
| ttg_s | 5.07 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.0 |
| axe_violations | 2 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### radius-raid-js13k (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [1] |

| Measure | Value |
|---|---|
| total_mb | 0.17 |
| file_count | 23 |
| initial_mb | 0.02 |
| first_paint_s | 3.5 |
| ttg_s | 3.5 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.7 |
| axe_violations | 1 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### HexGL (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [2] | - |
| Playgama | **BLOCKED** | no external resources [2] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [2] | - |
| Any portal (hygiene) | **FIXES** | - | no http:// resources loaded (portals serve https) [3]; axe-core WCAG 2.2 AA violations = 0 [1] |

| Measure | Value |
|---|---|
| total_mb | 20.42 |
| file_count | 198 |
| initial_mb | 0.76 |
| first_paint_s | 0.96 |
| ttg_s | 2.12 |
| external_requests | 2 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 3 |
| peak_js_heap_mb | 7.9 |
| axe_violations | 1 |
| touch_changes_frame | - |

**Fix list**

- Bundle these external hosts: www.google-analytics.com

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### q1k3 (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **READY** | - | - |
| Playgama | **READY** | - | - |
| Reddit Devvit Web | **READY** | - | - |
| Any portal (hygiene) | **BLOCKED** | no uncaught JS errors on load [1]; every file the game requests exists (no 404s) [1] | a tap changes the screen (mobile input) [no]; axe-core WCAG 2.2 AA violations = 0 [3] |

| Measure | Value |
|---|---|
| total_mb | 0.51 |
| file_count | 95 |
| initial_mb | 0.03 |
| first_paint_s | 4.46 |
| ttg_s | 4.51 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 1 |
| input_errors | 0 |
| missing_files | 1 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.3 |
| axe_violations | 3 |
| touch_changes_frame | no |

**Fix list**

- Uncaught error on load: `Cannot read properties of undefined (reading 'c')`
- Files requested but missing (404): /game/build/l

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### Gamedev-Phaser-Content-Kit (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [1] | - |
| Playgama | **BLOCKED** | no external resources [1] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [1] | - |
| Any portal (hygiene) | **FIXES** | - | axe-core WCAG 2.2 AA violations = 0 [22] |

| Measure | Value |
|---|---|
| total_mb | 24.78 |
| file_count | 347 |
| initial_mb | 0.0 |
| first_paint_s | 0.95 |
| ttg_s | 0.95 |
| external_requests | 1 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.9 |
| axe_violations | 22 |
| touch_changes_frame | yes |

**Fix list**

- Bundle these external hosts: camo.githubusercontent.com

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### untrusted (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [14] | - |
| Playgama | **BLOCKED** | no external resources [14] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [14]; no remote scripts [5] | - |
| Any portal (hygiene) | **BLOCKED** | every file the game requests exists (no 404s) [1] | no http:// resources loaded (portals serve https) [9]; a tap changes the screen (mobile input) [no]; axe-core WCAG 2.2 AA violations = 0 [3] |

| Measure | Value |
|---|---|
| total_mb | 229.32 |
| file_count | 570 |
| initial_mb | 0.22 |
| first_paint_s | 1.77 |
| ttg_s | 1.77 |
| external_requests | 14 |
| absolute_paths | 0 |
| remote_scripts | 5 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 1 |
| insecure_urls | 9 |
| peak_js_heap_mb | 13.0 |
| axe_violations | 3 |
| touch_changes_frame | no |

**Fix list**

- Bundle these external hosts: ajax.googleapis.com, fonts.googleapis.com, github.blog, www.google-analytics.com, www.googletagmanager.com, www.paypalobjects.com
- Files requested but missing (404): /game/scripts/build/untrusted.js

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### cube-composer (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [4] | - |
| Playgama | **BLOCKED** | no external resources [4] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [4] | - |
| Any portal (hygiene) | **BLOCKED** | every file the game requests exists (no 404s) [2] | no http:// resources loaded (portals serve https) [1]; axe-core WCAG 2.2 AA violations = 0 [2] |

| Measure | Value |
|---|---|
| total_mb | 0.61 |
| file_count | 48 |
| initial_mb | 0.0 |
| first_paint_s | 0.9 |
| ttg_s | 0.9 |
| external_requests | 4 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 2 |
| insecure_urls | 1 |
| peak_js_heap_mb | 8.6 |
| axe_violations | 2 |
| touch_changes_frame | yes |

**Fix list**

- Bundle these external hosts: api.github.com, fonts.googleapis.com, ghbtns.com, www.google-analytics.com
- Files requested but missing (404): /game/dist/main.css, /game/dist/main.js

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

