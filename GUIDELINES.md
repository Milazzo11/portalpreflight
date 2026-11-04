# portalpreflight: guidelines (inherits the iLazy Global Set)

inherits: iLazy GS11 (operator/GUIDELINES.md)

- AMEND GL-TST1: suite = `python3 -m unittest discover -s tests`; corpus/run.py is the 20-game field test, not the suite.
- ADD PPF-1: a portal rule enters portals.py only with its source URL and a verbatim quote (date in `checked`); a number
  we cannot cite is not a rule. Rule changes arrive via ruleradar diffs, not model re-reads.
- ADD PPF-2: we preflight only bundles their owner submits or that are public open source; nothing third-party is
  redistributed, only our measurements are published.
- ADD PPF-3: the public repo flip and the Marketplace listing need the controller's go (R&D 102a scope); forum posts need
  the S6 word `rd-portal-preflight`.
ENERGY STAR: yes - deterministic checks (stdlib + headless Chromium), 0 tokens per run, $0/mo on free CI minutes.
