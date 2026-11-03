---
name: Bhadvengers
description: Two forces. One fan-made team.
colors:
  night: "#070b13"
  night-soft: "#0c111b"
  blue-current: "#45baff"
  deep-current: "#1676ff"
  ember: "#ff6845"
  firelight: "#ffb34e"
  white: "#f3f6fb"
  muted: "#a1aebd"
typography:
  display:
    fontFamily: "Barlow Condensed, Impact, sans-serif"
    fontSize: "clamp(3.5rem, 8.5vw, 7.875rem)"
    fontWeight: 800
    lineHeight: 0.78
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Manrope, Segoe UI, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.7
rounded:
  sm: "2px"
  md: "3px"
spacing:
  page-gutter: "clamp(24px, 7.3vw, 112px)"
  section: "clamp(88px, 10vw, 146px)"
components:
  button-primary:
    backgroundColor: "linear-gradient(110deg, rgba(31, 126, 211, .68), rgba(37, 76, 127, .58) 54%, rgba(141, 56, 49, .72))"
    textColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: "0 21px"
    height: "50px"
  glass-panel:
    backgroundColor: "rgba(15, 23, 35, .76)"
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
---

# Design System: Bhadvengers

## Overview

**Creative North Star: "Tidal Ember"**

The interface treats water and fire as two currents meeting around the Bhadvengers name. Ink-dark space gives the cool blue and warm ember light room to move; translucent surfaces are reserved for controls and information that should feel close to the scene.

Headlines carry a condensed, poster-like voice while body copy stays calm and readable. The large emblem is typographic and image-free; member portraits and supplied artwork belong to the story, not the logo.

**Key Characteristics:**
- Blue current balanced by ember and firelight
- Centered, image-free wordmark inside a split-energy ring
- Condensed uppercase display type with open, restrained body copy
- Glass used for legibility and focus, not as a substitute for content

## Colors

Midnight ink is the ground; blue-current and ember own opposite sides of the story, with firelight as a small warm signal.

### Primary
- **Midnight Ink** (`#070b13`): Main canvas and the deepest page surfaces.
- **Blue Current** (`#45baff`): Water identity, cool interaction states, and fine edge light.
- **Ember** (`#ff6845`): Fire identity, selected emphasis, and small signals.

### Secondary
- **Deep Current** (`#1676ff`): A supporting blue in the ambient field.
- **Firelight** (`#ffb34e`): Warm highlights and concise calls to action.
- **Night Soft** (`#0c111b`): Recessed content surfaces.
- **White** (`#f3f6fb`): Primary copy and display type.
- **Muted** (`#a1aebd`): Secondary copy on dark surfaces.

## Typography

Barlow Condensed carries the team wordmark and dramatic, uppercase headings. Manrope carries navigation, body copy, form labels, and supporting details. Google Fonts load when available; the CSS stacks provide local fallbacks.

## Layout

Sections use a responsive page gutter, generous vertical pauses, and alternating image-and-copy compositions. The roster moves from three columns to one at small screen sizes. The join page pairs its story and form on wider screens, then stacks them on mobile. Main breakpoints are 900px and 680px.

## Elevation & Depth

Page sections are separated by tonal shifts and thin borders. Translucent backgrounds and backdrop blur belong on the navigation, action surfaces, portrait tags, and upload controls. Shadows use offset blur for physical separation; the energy ring may glow as an intentional identity detail.

## Shapes

Most edges are square or lightly rounded (2–3px). Circular geometry is reserved for the emblem, its orbit, and small identity markers. Form fields and cards use crisp outlines rather than pill shapes.

## Components

- **Primary button:** A compact blue-to-ember glass surface, strong label, and clear directional arrow.
- **Navigation:** Dark translucent header with underlined current route and an accessible compact menu on mobile.
- **Member portrait:** Image-led crop with a glass identity tag; profile details sit on an ink-toned surface.
- **Join form:** Clearly labeled fields, visible focus, native validation, photo preview, drag-and-drop support, and distinct loading, success, and error messages.

## Do's and Don'ts

- Do keep the Bhadvengers name centered and free of portrait imagery in the emblem.
- Do preserve the cool/warm balance and use animation sparingly to suggest current and flame.
- Do keep contrast, focus visibility, and reduced-motion behavior intact.
- Don't imply submitted profiles are shared across browsers; this version stores them locally.
- Don't represent this independent fan community as affiliated with Marvel or DC.
