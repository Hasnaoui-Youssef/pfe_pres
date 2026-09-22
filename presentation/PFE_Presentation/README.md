# PFE defense presentation

**Design and Implementation of a Debugger with Instruction Trace Capabilities.**

Youssef Hasnaoui · 26 September 2026 · English · 20 minutes.

## Run

```sh
npm install
npm run dev
```

For a local server without opening a browser: `npm exec slidev -- --port 3030`.
Build with `npm run build`. The static output is in `dist/`.

The visual theme follows the supplied PowerPoint references: exact blue `#03234B` and yellow `#FFD200`, with all three institutional logos on the title slide. See [THEME.md](./THEME.md) for sources and visual conventions.

## Present

There are **23 main slides and 7 backup slides**. The main presentation ends on slide 23. The small footer tracks sections without extra divider slides. Speaker notes include explanations, evidence references, transitions and timing that totals exactly 20 minutes.

| Section | Slides | Duration | Cumulative |
| --- | --- | --- | --- |
| Context and problem | 1–4 | 3:00 | 3:00 |
| Objectives and approach | 5–8 | 3:00 | 6:00 |
| Design and implementation | 9–16 | 7:00 | 13:00 |
| Demonstration | 17–18 | 2:00 | 15:00 |
| Validation and results | 19–21 | 3:00 | 18:00 |
| Limits and conclusion | 22–23 | 2:00 | 20:00 |

Use Slidev's presenter mode to read the notes. Normal presentation controls advance the staged diagrams before moving to the next slide. Slide 13 reconstructs the report’s loop with four successive ETM atoms (E, E, E, N); its counter advances 0 → 4 → 8 → 12 → 16 instructions. The evidence walkthrough on slide 18 has three steps, reachable with either the keyboard or its tabs. The real 90-second recording is pending board availability; [DEMO.md](./DEMO.md) explains the recording and one-line integration. [EVIDENCE.md](./EVIDENCE.md) records asset and metric provenance.

The narrative separates reused libraries, extended drivers and the project implementation. The capture architecture is device-independent; the named processor and development board appear as validation resources on slide 19. Main-slide explanations use plain technical language, with detailed interpretation in speaker notes.

## Check and rehearse

- Run `npm run build` after editing.
- Check all 30 slides at 16:9, especially code, trace screenshots and chart labels.
- Check both initial and revealed states. Replay the four ETM atoms and confirm that the next advance leaves slide 13.
- Exercise all three walkthrough steps; when the recording is added, check playback and the fallback.
- Rehearse aloud to the timing above. The timing allocation is a rehearsal target, not a claim that a spoken rehearsal has already been completed.
- Use `npm run export` for PDF export when Playwright is installed; video and interactive controls become static in PDF.

The chart is regenerated with `python3 scripts/generate-chart.py`. `scripts/slide-manifest.json` records the slide inventory and timing; keep it aligned if the structure changes.
