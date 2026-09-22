# Reference theme

The two supplied references are `../Main Presentation.pptx` and `../Debugger_with_trace.pptx`. Their primary theme (`ppt/theme/theme1.xml`) defines the same palette and Arial typeface.

The presentation uses the user's selected primary colors exactly:

| Role | Color |
| --- | --- |
| Blue: text, cover, diagram blocks | `#03234B` |
| Yellow: emphasis, active stages, side stripe | `#FFD200` |
| White: content background and reversed text | `#FFFFFF` |
| Neutral text | `#525A63` |
| Neutral panels | `#EEEFF1` |
| Neutral borders | `#C0C8D2` |

Adapted visual patterns:

- Blue cover and yellow left stripe from both reference title layouts.
- Yellow title label and institutional masthead inspired by Main Presentation's first slide.
- Numbered section navigation from Main Presentation, retained as a compact footer to preserve the approved slide sequence.
- Solid diagram blocks, connectors and highlighted processing stages from Debugger_with_trace (especially slides 25, 38 and 45–50).
- Blue/white content panels and yellow emphasis throughout the charts, tables and walkthrough.

No magenta, cyan or teal is used as a presentation theme color. Original logos and captured debugger screenshots retain their source colors.

## Logos

- University of Carthage: `dissertation_pfe/img/ST_Summer_Internship/uni_car.png`.
- ENICarthage: `dissertation_pfe/img/ST_Summer_Internship/logo_enicar.jpg`.
- STMicroelectronics: original blue SVG, `ppt/media/image1.svg` in `Debugger_with_trace.pptx`.

All three assets are copied into `public/branding/` and displayed on a white masthead. The ENICarthage image's surrounding white space is cropped by its CSS viewport; the artwork itself is unchanged.

## Academic figure conventions

The main deck now uses semantic line icons, component diagrams, an acquisition sequence diagram, annotated actual UI views, a progressive ETM-loop reconstruction and a visual sequence comparison. Reused components are neutral; extensions are blue with a yellow edge; project implementations are yellow in ownership diagrams. Outside ownership diagrams, yellow identifies the active step or important evidence.

Slide transitions are directional within sections and fade between sections. Progressive reveals follow the explanation rather than adding decorative motion. The ETM example and fault walkthrough use ordinary presentation controls. Reduced-motion preferences disable movement.
