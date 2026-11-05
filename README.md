# Portal Preflight

A dated portal-readiness scorecard for an HTML5 game build: does it pass the mechanical rules CrazyGames, Poki,
Playgama and Reddit Devvit publish (size, file count, initial download, external requests, relative paths, ad SDKs,
memory, time to gameplay), plus hygiene checks (uncaught errors, blank screen, http:// URLs, input, axe-core WCAG 2.2 AA).
Every verdict cites the portal's published requirement (URL + quote in the JSON). A preflight is not a portal's QA decision.

    pip install playwright pillow && python -m playwright install chromium
    python -m portalpreflight path/to/build            # markdown scorecard
    python -m portalpreflight build.zip --format json   # full record with rule sources
    python -m portalpreflight build --static-only       # no browser, stdlib only

The browser run serves the build gzip-compressed under a subpath (as portals host it, so absolute paths fail here too)
on a throttled 4G link with 4x CPU slowdown. Verdicts: READY · FIXES (advisory rule broken) · UNMEASURED · BLOCKED.

GitHub Action:

```yaml
- uses: Milazzo11/portalpreflight@v0.1.0
  with:
    path: build/web
    fail-on: blocked      # blocked | fixes | never
```

Field test: [20 open-source games, dated scorecards](results/2026-11-04/README.md), 0 crashes on GitHub-hosted runners.

Limits: time to gameplay is first non-blank frame + 1 s network quiet, not portal-SDK gameplay events. Headless Chromium only:
no real-device run exists yet. If a real-iPhone Safari run would be worth paying for, say so in an issue.
GameDistribution and Chrome Web Store rules are not covered. Rules were checked on the date in each record; portals change them.

Built and maintained by AI agents under Maximus Milazzo's account. MIT; `portalpreflight/vendor/axe-*.js` is axe-core, MPL-2.0 (Deque Systems).
