# Portal Preflight: 20 open-source HTML5 games (2026-11-04)

20 games from GitHub at pinned commits, each run as-is from its repository root. Tool crashes: 0. Each game: Chromium on a throttled 4G link (9 Mbps, 170 ms RTT) with 4x CPU slowdown, served gzip-compressed under a subpath the way portals host it; median of the runs by time to gameplay. Verdicts cite each portal's published rules (see `portalpreflight/portals.py`); a preflight is not a portal's QA decision. These are open-source repos, not the authors' portal submissions: many were never meant for a portal, and a game whose repo needs a build step shows its missing build output as 404s (the scorecard measures what is committed). ttg = first non-blank frame with the network quiet for 1 s (engine-agnostic; a title screen counts).

| Game | CrazyGames | Poki | Playgama | Reddit Devvit Web | Any portal | ttg s | initial MB | external req |
|---|---|---|---|---|---|---|---|---|
| [2048](https://github.com/gabrielecirulli/2048/tree/478b6ec346) | READY | READY | READY | READY | FIXES | 0.92 | 0.07 | 0 |
| [hextris](https://github.com/hextris/hextris/tree/3f4847dc8f) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 6.45 | 0.26 | 21 |
| [clumsy-bird](https://github.com/ellisonleao/clumsy-bird/tree/fae3d487d5) | READY | READY | READY | READY | FIXES | 3.26 | 1.52 | 0 |
| [floppybird](https://github.com/nebez/floppybird/tree/efd2c7f740) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 1.6 | 0.12 | 2 |
| [javascript-tetris](https://github.com/jakesgordon/javascript-tetris/tree/e5c0c42f7d) | READY | READY | READY | READY | FIXES | 0.79 | 0.05 | 0 |
| [javascript-pong](https://github.com/jakesgordon/javascript-pong/tree/ca3240536e) | READY | READY | READY | READY | FIXES | 0.94 | 0.03 | 0 |
| [javascript-breakout](https://github.com/jakesgordon/javascript-breakout/tree/eed59e2aff) | READY | READY | READY | READY | FIXES | 1.25 | 0.22 | 0 |
| [javascript-racer](https://github.com/jakesgordon/javascript-racer/tree/3e8a060b59) | READY | READY | READY | READY | FIXES | 0.64 | 0.0 | 0 |
| [javascript-boulderdash](https://github.com/jakesgordon/javascript-boulderdash/tree/61f0bb5978) | READY | READY | READY | READY | FIXES | 0.86 | 0.02 | 0 |
| [javascript-gauntlet](https://github.com/jakesgordon/javascript-gauntlet/tree/2f9020dc64) | READY | READY | READY | READY | FIXES | 5.16 | 7.42 | 0 |
| [pacman](https://github.com/daleharvey/pacman/tree/3acc5e2bb1) | READY | READY | READY | READY | READY | 1.87 | 0.1 | 0 |
| [Astray](https://github.com/wwwtyro/Astray/tree/d3c4f61f2c) | BLOCKED | READY | READY | READY | BLOCKED | 1.78 | 0.18 | 0 |
| [adarkroom](https://github.com/doublespeakgames/adarkroom/tree/1fada4620b) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 4.57 | 3.01 | 4 |
| [Captain-Rogers](https://github.com/EnclaveGames/Captain-Rogers/tree/5b4336d668) | READY | READY | READY | READY | FIXES | 5.17 | 1.46 | 0 |
| [radius-raid-js13k](https://github.com/jackrugile/radius-raid-js13k/tree/361ab51665) | READY | READY | READY | READY | FIXES | 4.45 | 0.02 | 0 |
| [HexGL](https://github.com/BKcore/HexGL/tree/6addc95a2f) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 1.9 | 0.76 | 4 |
| [q1k3](https://github.com/phoboslab/q1k3/tree/8ee934856c) | READY | READY | READY | READY | BLOCKED | 4.22 | 0.03 | 0 |
| [Gamedev-Phaser-Content-Kit](https://github.com/end3r/Gamedev-Phaser-Content-Kit/tree/307c14914d) | READY | BLOCKED | BLOCKED | BLOCKED | FIXES | 0.67 | 0.0 | 1 |
| [untrusted](https://github.com/AlexNisnevich/untrusted/tree/ab4a8ed280) | READY | BLOCKED | BLOCKED | BLOCKED | BLOCKED | 1.94 | 0.22 | 9 |
| [cube-composer](https://github.com/sharkdp/cube-composer/tree/83e5b66b05) | READY | BLOCKED | BLOCKED | BLOCKED | BLOCKED | 0.89 | 0.0 | 5 |

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
| file_count | 35 |
| initial_mb | 0.07 |
| first_paint_s | 0.84 |
| ttg_s | 0.92 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.9 |
| axe_violations | 3 |
| touch_changes_frame | yes |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### hextris (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [21]; no other ad systems [1] | - |
| Playgama | **BLOCKED** | no external resources [21] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [21]; no remote scripts [1] | - |
| Any portal (hygiene) | **FIXES** | - | no http:// resources loaded (portals serve https) [3]; axe-core WCAG 2.2 AA violations = 0 [8] |

| Measure | Value |
|---|---|
| total_mb | 1.52 |
| file_count | 74 |
| initial_mb | 0.26 |
| first_paint_s | 1.39 |
| ttg_s | 6.45 |
| external_requests | 21 |
| absolute_paths | 0 |
| remote_scripts | 1 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 3 |
| peak_js_heap_mb | 21.3 |
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
| file_count | 52 |
| initial_mb | 1.52 |
| first_paint_s | 1.07 |
| ttg_s | 3.26 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.9 |
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
| file_count | 55 |
| initial_mb | 0.12 |
| first_paint_s | 1.11 |
| ttg_s | 1.6 |
| external_requests | 2 |
| absolute_paths | 0 |
| remote_scripts | 1 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.4 |
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
| file_count | 6 |
| initial_mb | 0.05 |
| first_paint_s | 0.79 |
| ttg_s | 0.79 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.1 |
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
| file_count | 38 |
| initial_mb | 0.03 |
| first_paint_s | 0.68 |
| ttg_s | 0.94 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.2 |
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
| file_count | 72 |
| initial_mb | 0.22 |
| first_paint_s | 1.25 |
| ttg_s | 1.25 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.9 |
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
| file_count | 57 |
| initial_mb | 0.0 |
| first_paint_s | 0.64 |
| ttg_s | 0.64 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.9 |
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
| file_count | 23 |
| initial_mb | 0.02 |
| first_paint_s | 0.8 |
| ttg_s | 0.86 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.5 |
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
| file_count | 110 |
| initial_mb | 7.42 |
| first_paint_s | 1.5 |
| ttg_s | 5.16 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 8.7 |
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
| file_count | 26 |
| initial_mb | 0.1 |
| first_paint_s | 0.71 |
| ttg_s | 1.87 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 6.0 |
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
| file_count | 12 |
| initial_mb | 0.18 |
| first_paint_s | 1.78 |
| ttg_s | 1.78 |
| external_requests | 0 |
| absolute_paths | 3 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 3 |
| insecure_urls | 0 |
| peak_js_heap_mb | 9.6 |
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
| file_count | 232 |
| initial_mb | 3.01 |
| first_paint_s | 2.46 |
| ttg_s | 4.57 |
| external_requests | 4 |
| absolute_paths | 0 |
| remote_scripts | 2 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 2 |
| peak_js_heap_mb | 14.0 |
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
| file_count | 189 |
| initial_mb | 1.46 |
| first_paint_s | 1.49 |
| ttg_s | 5.17 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 7.2 |
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
| file_count | 24 |
| initial_mb | 0.02 |
| first_paint_s | 4.45 |
| ttg_s | 4.45 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 16.0 |
| axe_violations | 1 |
| touch_changes_frame | - |

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

### HexGL (2026-11-04)

portalpreflight 0.1.0 · Chromium, 4G + 4x CPU throttle, served under a subpath

| Target | Verdict | Blocking | Advisory |
|---|---|---|---|
| CrazyGames | **READY** | - | - |
| Poki | **BLOCKED** | no external requests [4] | - |
| Playgama | **BLOCKED** | no external resources [4] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [4] | - |
| Any portal (hygiene) | **FIXES** | - | no http:// resources loaded (portals serve https) [3]; axe-core WCAG 2.2 AA violations = 0 [1] |

| Measure | Value |
|---|---|
| total_mb | 20.42 |
| file_count | 199 |
| initial_mb | 0.76 |
| first_paint_s | 1.04 |
| ttg_s | 1.9 |
| external_requests | 4 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 3 |
| peak_js_heap_mb | 8.0 |
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
| file_count | 96 |
| initial_mb | 0.03 |
| first_paint_s | 0.76 |
| ttg_s | 4.22 |
| external_requests | 0 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 1 |
| input_errors | 0 |
| missing_files | 1 |
| insecure_urls | 0 |
| peak_js_heap_mb | 16.8 |
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
| total_mb | 24.79 |
| file_count | 348 |
| initial_mb | 0.0 |
| first_paint_s | 0.67 |
| ttg_s | 0.67 |
| external_requests | 1 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 0 |
| insecure_urls | 0 |
| peak_js_heap_mb | 11.8 |
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
| Poki | **BLOCKED** | no external requests [9] | - |
| Playgama | **BLOCKED** | no external resources [9] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [9]; no remote scripts [5] | - |
| Any portal (hygiene) | **BLOCKED** | every file the game requests exists (no 404s) [1] | no http:// resources loaded (portals serve https) [9]; a tap changes the screen (mobile input) [no]; axe-core WCAG 2.2 AA violations = 0 [3] |

| Measure | Value |
|---|---|
| total_mb | 229.32 |
| file_count | 571 |
| initial_mb | 0.22 |
| first_paint_s | 0.95 |
| ttg_s | 1.94 |
| external_requests | 9 |
| absolute_paths | 0 |
| remote_scripts | 5 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 1 |
| insecure_urls | 9 |
| peak_js_heap_mb | 11.7 |
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
| Poki | **BLOCKED** | no external requests [5] | - |
| Playgama | **BLOCKED** | no external resources [5] | - |
| Reddit Devvit Web | **BLOCKED** | no external requests (webview CSP) [5] | - |
| Any portal (hygiene) | **BLOCKED** | every file the game requests exists (no 404s) [2] | no http:// resources loaded (portals serve https) [1]; axe-core WCAG 2.2 AA violations = 0 [2] |

| Measure | Value |
|---|---|
| total_mb | 0.61 |
| file_count | 49 |
| initial_mb | 0.0 |
| first_paint_s | 0.74 |
| ttg_s | 0.89 |
| external_requests | 5 |
| absolute_paths | 0 |
| remote_scripts | 0 |
| page_errors | 0 |
| input_errors | 0 |
| missing_files | 2 |
| insecure_urls | 1 |
| peak_js_heap_mb | 10.6 |
| axe_violations | 2 |
| touch_changes_frame | yes |

**Fix list**

- Bundle these external hosts: api.github.com, fonts.googleapis.com, ghbtns.com, www.google-analytics.com
- Files requested but missing (404): /game/dist/main.css, /game/dist/main.js

Rules and sources: each verdict cites the portal's published requirement (`--format json` has the quotes). A preflight is not a portal's QA decision.

