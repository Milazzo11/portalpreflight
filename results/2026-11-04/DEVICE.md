# Real-iPhone check, 3 of the 20 games (2026-11-04)

iPhone SE, iOS 26.2, Safari private tab, files served over the LAN. Observed through the phone's screen stream and the server's request log. This is a one-off manual check, not a feature of the tool, and one run per game per setup is a small sample.

| Game | At the server root | Under /game/ (how a portal hosts it) |
|---|---|---|
| Astray | ball.png, brick.png, concrete.png: 200; textured maze renders | same three files: 404; screen almost entirely black |
| pacman | not compared by frame | every file 200; board renders |
| javascript-tetris | not compared by frame | every file 200; renders "Press Space to Play" |

Result: the scorecard's Astray verdict (relative paths, missing files) reproduces on real Safari, and the two games it passed on those rules also load.

Not measured: frame rate, audio and load time on the device. One tap on pacman and tetris changed nothing visible at that spot; tetris asks for a Space key, but one tap is not enough to call either game unplayable by touch.
