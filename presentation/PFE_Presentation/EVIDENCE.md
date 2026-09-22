# Evidence and asset provenance

Paths below are relative to the sibling workspaces `dissertation_pfe` and `emTrailer`. Speaker notes in `slides.md` identify the source for each slide. The presentation describes final behavior, without narrating the implementation's debugging history.

| Material | Source | Use |
| --- | --- | --- |
| Author, program and supervisors | `dissertation_pfe/global_config.tex` | Title slide |
| Institution | `dissertation_pfe/tpl/cover_page.tex` | National Engineering School of Carthage |
| Defense date | User confirmation: 26 September 2026 | Title slide |
| Jury members | User confirmation: Ms Nourelhouda BEN YOUSSEF, Reviewer; Ms Samia HACHMI, Jury President | Title slide |
| Theme and logos | Supplied PowerPoint themes and report logo assets; see `THEME.md` | Exact blue/yellow palette and three-logo title masthead |
| Host team, problem and tool positioning | `dissertation_pfe/chap_01.tex` | Slides 2–6 and B1 |
| ETM loop example | `dissertation_pfe/img/gen_fig/fig_trace_elements_loop.tex` | Slide 13: four instructions, E/E/E/N, four iterations; synchronization omitted |
| Bytes → packets → elements | `dissertation_pfe/img/gen_fig/fig_bytes_to_elements.tex` | Slide 12: saved-capture excerpt; shortened packet names |
| Range-expansion pseudocode | `emTrailer/engine/modules/providers/trace/trace_transform/include/trace_transform/reconstructed_instruction_transform.hpp` | Slide 14: simplified actual range-walking algorithm |
| Address-sequence excerpt | `emTrailer/engine/validation/captures/w1_baseline/shadow_trace/shadow_addresses.json` | First four observed addresses shown on slide 20 |
| Architecture and integration | `dissertation_pfe/chap_04.tex`; `emTrailer/engine/docs/architecture/` | Slides 9–16 and B2–B4 |
| Actual trace screenshots | `dissertation_pfe/img/debugger_screenshots/{function_trace_ui,instruction_trace_ui}.png` | Copied unchanged to `public/evidence/`; startup capture, not W7 |
| W7 fault | `emTrailer/engine/validation/findings/07-fault-case-study.md` and `validation/firmware/w7_fault/Core/Src/main.c` | Slides 17–18 and B7 |
| Saved halt state | `emTrailer/engine/validation/captures/w7_fault/state_at_halt.json` | Copied to `public/evidence/fault-state.json` |
| Walkthrough fallback screenshots | Browser render of slide 18's three evidence panels | `public/demo/walkthrough-{1,2,3}.png`; not hardware-session screenshots |
| Oracle agreement | `emTrailer/engine/validation/findings/11-shadow-trace-oracle.md` | 400/400 exact address matches, one interrupt-free W1 interval |
| Structural coverage | `emTrailer/engine/validation/findings/12-cfg-conformance-checker.md` | 229,424 transitions, 61 captures; presented as coverage |
| Buffer capacity | `emTrailer/engine/validation/analysis/density_summary.csv`; Findings 10 and 17 | Chart: density × 2,048 usable bytes; six captures/class |
| Timing | `emTrailer/engine/validation/findings/14-timing-reconstruction-blocked-by-decoder-limitation.md` | Despite the stale filename, its content establishes working timing reconstruction: 316/324, 316/324, 314/322 cycles |
| Scope | Findings 07 and 17 | One demonstrated fault class; one target configuration |

## Reading the metrics

- **100% agreement** means exactly 400 matching instruction addresses in the independent-oracle experiment. It is not a general all-input guarantee.
- **229,424 transitions** is a structural coverage count, not another accuracy percentage. No superseded aggregate conformance percentage or old decoder-limitation explanation is presented.
- **1.6k–8.7k instructions** is the overall observed range derived from the density measurements. The bars show means; the whiskers show sample minima and maxima, not confidence intervals.
- **Within 2.5% of DWT** is one bracketed ISR-span experiment over three repeats, not all-workload profiling accuracy.
- Slide 7 uses language-level illustrative pseudocode. Slide 13 adapts the report’s ETM teaching example. Slide 14 presents a simplified implementation algorithm and a teaching equivalent of the loop’s source grouping.
- Board-independent architecture does not imply support for every trace protocol. The implemented acquisition scope remains ETMv4 and an on-chip trace sink; the named board and processor are experimental resources.

## Regenerate the chart

Run `python3 scripts/generate-chart.py`. It reads the committed CSV and emits a standalone accessible SVG without additional dependencies.
