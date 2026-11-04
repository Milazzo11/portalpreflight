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
- uses: Milazzo11/portalpreflight@v0
  with:
    path: build/web
    fail-on: blocked      # blocked | fixes | never
```
