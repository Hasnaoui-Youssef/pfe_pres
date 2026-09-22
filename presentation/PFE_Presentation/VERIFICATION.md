# Presentation verification

Checked on 22 September 2026:

- Production build: `npm run build` passes.
- Inventory: 23 timed slides, 7 backups, 30 speaker-note blocks, 1,200 seconds allocated.
- Exact title appears in the metadata and visible title slide; date is 26 September 2026.
- Chromium review at 1280×720: all 30 slides render without missing images, runtime exceptions, horizontal overflow or content entering the footer area.
- Academic revision: initial and final reveal states checked across all 30 slides; spacing fixes rechecked on slides 6, 8, 9, 13, 16, 18, 19 and 23. Architecture spacing and trace screenshot magnification reviewed visually.
- Worked ETM example: keyboard progression produces 0, 4, 8, 12 and 16 instructions with four successive loop passes; the following keypress advances to slide 14.
- Narrative distinguishes reused, extended and implemented components. Named board and processor are introduced in the validation setup. No visible W1–W7 workload codes remain.
- Reference theme pass: exact blue `#03234B` / yellow `#FFD200`, numbered navigation, and University of Carthage, ENICarthage and STMicroelectronics logos verified in-browser. All three fallback screenshots regenerated in the new theme.
- All three walkthrough buttons select the expected panel; static fallback screenshots saved.
- Earlier video-slot check: playback advanced with a temporary in-memory test clip; manual and missing-video fallbacks worked. The current revision rechecked walkthrough controls and screenshots; the final hardware recording remains to be tested. No test clip is shipped.
- `git diff --check` passes.

Still to do with the presenter: record the actual 90-second hardware demonstration, verify that recording in the presentation browser, and rehearse the complete talk aloud against the timing in the speaker notes. A timed speaking allocation does not replace that rehearsal.
