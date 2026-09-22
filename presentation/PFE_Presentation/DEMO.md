# Demonstration handoff

Slide 18 currently uses a three-step evidence walkthrough (failure state → execution path → source diagnosis). Normal presentation controls or the on-screen tabs advance it. It is deliberately labeled as a walkthrough, not a live-session recording. Youssef will record the hardware session when a board is available.

Static screenshots of the walkthrough are ready as an additional fallback: [halt state](./public/demo/walkthrough-1.png), [execution sequence](./public/demo/walkthrough-2.png), and [source diagnosis](./public/demo/walkthrough-3.png). These are screenshots of the presentation's evidence panels, not of a hardware debugging session.

## Record 90 seconds

Use the NUCLEO-H7S3L8 / STLINK-V3EC and the W7 firmware in `emTrailer/engine/validation/firmware/w7_fault`. Use the working project's normal launch configuration and the matching built ELF. Preserve the exact ELF and ETM configuration with the capture.

| Time | Show | Narration |
| --- | --- | --- |
| 0–15 s | Launch W7, arm trace, breakpoint at `HardFault_Handler` entry | “Capture is active before the fault.” |
| 15–30 s | Halt and inspect the fault registers | “INVSTATE escalated to HardFault; the final state identifies the failure.” |
| 30–60 s | Open trace and follow `Process()`, its return and `on_complete()` | “The record shows the execution leading to the indirect call.” |
| 60–80 s | Navigate to the copy loop and adjacent buffer/pointer fields | “The inclusive loop bound writes beyond the buffer.” |
| 80–90 s | Keep source and trace visible together | “Control flow plus source code explains the path to failure.” |

Halt at handler entry: letting its loop run can overwrite the pre-fault history in the small buffer. Use a fresh output capture for each recording. Do not infer the current cached pointer value from an SRAM read or describe instruction trace as data-value tracing.

Record at 1920×1080 or higher with enlarged editor and trace text. Prefer a quiet screen recording with narration delivered in person, so the talk can adapt to the jury. Export MP4 with H.264 video for broad browser support.

## Add the recording

1. Save it as `public/demo/fault-investigation.mp4`.
2. In `slides.md`, replace `<DemoWalkthrough />` with `<DemoWalkthrough video-src="/demo/fault-investigation.mp4" />`.
3. Rebuild and inspect slide 18. The video has native controls and does not autoplay. A playback error, or the “Show evidence walkthrough” button, reveals the existing fallback.
4. Save three actual screenshots from the recording: halt state, trace sequence, source diagnosis. Until those exist, the current fallback uses the saved W7 state and documented trace sequence. The screenshots on slide 16 depict a different startup capture.
5. Practice the 90-second segment, then rehearse the full presentation. PDF export shows the currently selected walkthrough step; it cannot play video.

The walkthrough's three panels are available now. No board access, new fault capture, or video recording was performed while building this deck.
