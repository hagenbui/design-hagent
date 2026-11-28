# Color palettes

Part of the design-hagent skill. Read when you draft or change an app's colors (new app stage 3, a restyle, a dark appearance), suggest a palette, or review color (references/review-rules.md, group "Color palette"). SKILL.md still applies.

## Where the values live

- An app's colors live in its tier 2 App Color collection. The base colors are placeholders (Core principle). Never put an app palette into the base.
- Everything in this file is a suggestion. A palette becomes the app's only through the Approval loop: style tile on page Design, the designer's OK, then the values in App Color and the rule with its reason. Adding, renaming or removing a color variable or a mode (such as a dark appearance) needs its own OK.
- Screens and parts bind to App Color variables, never to raw hex. The hex values below are seeds for a style tile, not tokens.

## What a palette is made of

A tasteful app palette is mostly neutral, with one color that means "act here". Map each role below onto the App Color variables the file already has. If a role has no variable, it is a missing token: follow Core principle in SKILL.md (base first, with approval, then mirrored in tier 2) instead of reusing an unrelated variable. A full ramp is drawn on the style tile; App Color keeps only the steps its roles use.

| Role | Job | Share of the screen |
|---|---|---|
| Neutral ramp | background, surfaces, borders, text, icons | about 60 to 90 percent |
| Primary | main action, selected state, focus, links | about 5 to 10 percent |
| Accent (optional) | one highlight: badge, streak, reward, illustration detail | under 5 percent |
| Semantic | error, warning, success, info | only where that state is shown |
| Premium (IAA/IAP, optional) | paywall, Premium badge, locked marker | only on premium moments |

The 60-30-10 split (dominant, secondary, accent) is a starting point from interior design, not a law. What matters is that color is scarce enough to point.

## Building a ramp

- Each hue used in the UI (neutral, primary, and accent if it fills anything) gets a ramp of about 10 to 12 steps, light to dark, not 3 or 4. A short ramp forces raw in-between values later. (Refactoring UI)
- Give steps a job, the Radix way: 1 to 2 app and subtle backgrounds, 3 to 5 component backgrounds (normal, hover or pressed, selected), 6 to 8 borders (7 also focus ring), 9 the solid fill (buttons, badges), 10 its hover fill, which on touch becomes the pressed fill, 11 secondary text, 12 primary text.
- Build in a perceptual space (OKLCH or Material's HCT), not HSL: equal lightness then looks equally light across hues, so contrast is predictable. Hold hue and chroma, step lightness, then tune by eye.
- Contrast by tone (Material HCT, tone 0 to 100): Material says a tone difference of 40 guarantees 3:1 (large text, icons, borders) and 50 guarantees 4.5:1 (body text, small controls). That holds for colors built in HCT. Seeds tuned by eye or taken from another source (a recipe below, a Wada color) are measured pair by pair.
- States come from the same ramp (pressed one step darker, selected a tint, disabled the neutral ramp), never from a new hue.

## Taste rules (what makes a palette look designed)

1. **Tint the neutrals.** Greys lean slightly toward the primary hue (OKLCH chroma about 0.005 to 0.02), cool for a blue brand, warm for an earthy one. One temperature for all greys on a screen. Pure neutral grey next to a colored brand looks unfinished.
2. **One action color.** The primary marks what can be tapped or what is selected. Don't use it for plain headings or decoration, or people can't tell what is interactive. (Apple HIG Color)
3. **Few hues.** One primary, at most one accent, plus the semantic set. A new hue needs a job no existing role does.
4. **Chroma by area.** Large areas (backgrounds, headers, big cards) get low chroma; full chroma only on small areas (buttons, badges, icons). A big vivid area tires the eye and steals focus from the action.
5. **Lightness carries hierarchy.** Check the palette in grayscale: the main action and the text still stand out. If they don't, fix lightness, not hue. (App Store "Differentiate without color alone": test with the Grayscale filter)
6. **Semantic colors are their own.** Error, warning and success differ from the primary and from each other, and each state also has an icon or text. If the brand is red or green, move the error or success hue away from it. Nudge semantic hues slightly toward the brand so they belong (Material harmonize), without losing their meaning.
7. **Dark appearance is not inverted.** Surfaces are dark grey, not pure black (Material dark theme: about #121212, tinted like the neutrals), higher surfaces a bit lighter. Primary and accent move lighter and less saturated, so they don't vibrate on dark. Every pair is measured again in dark.
8. **Gradients, sparingly.** Two neighboring hues of similar lightness, on art or a hero area, not behind body text. Measure text contrast at the gradient's worst point.
9. **Premium stays special.** A premium or gold color appears only on paywall, Premium badges and locked markers. Used elsewhere it stops meaning "paid".

## Suggestion recipes

Ten verified starting points (light seeds, then dark seeds). Every pair in each row was measured on 2026-11-26: text on background at least 7:1, secondary text on background and surface at least 4.5:1, label on primary and on accent at least 4.5:1, primary against background at least 3:1; in dark, text on background at least 7:1, secondary text on surface and label on primary at least 4.5:1, primary against surface at least 3:1. The table gives no dark accent or dark border: derive them by rule 7 and measure them. Use them as the first draft of a style tile, then tune to the brand. Show the designer two or three that fit the brief, not all ten.

| Recipe | Fits | Bg / Surface | Text / Text 2 | Border | Primary / On | Accent / On | Dark bg / surface | Dark text / text 2 | Dark primary / on |
|---|---|---|---|---|---|---|---|---|---|
| Calm utility | calendar, notes, tools | #F7F8FA / #FFFFFF | #14171F / #5B6472 | #D9DEE5 | #2F5BEA / #FFFFFF | #FFB020 / #14171F | #0F1115 / #181B21 | #ECEEF2 / #A3AAB6 | #8FA8FF / #0F1115 |
| Warm wellness | meditation, sleep, habits | #F7F4EF / #FFFDF9 | #1F1B16 / #6A6259 | #E3DCD1 | #3F7D6B / #FFFFFF | #E8956B / #1F1B16 | #141210 / #1D1A17 | #F0EBE4 / #B0A79C | #8CC7B3 / #141210 |
| Playful kids | kids, family, games | #FFF9F0 / #FFFFFF | #2A2340 / #655E7A | #EDE4D6 | #6C4CF5 / #FFFFFF | #FFC93C / #2A2340 | #16131F / #201C2C | #F3F0FA / #ADA6C2 | #B3A3FF / #16131F |
| Mystic night | astrology, palm, tarot | #F5F3FA / #FFFFFF | #1C1830 / #5E5875 | #DCD7E8 | #4B3BA8 / #FFFFFF | #C9A24A / #1C1830 | #0E0C18 / #181526 | #EEEAF7 / #A9A2C0 | #D9B865 / #0E0C18 |
| Trust finance | budget, banking, invoices | #F6F8F8 / #FFFFFF | #111A1C / #55625F | #D7DEDD | #0F6B5A / #FFFFFF | #1E3A8A / #FFFFFF | #0C1112 / #151B1C | #E9EFEE / #9EAAA8 | #6FD1B8 / #0C1112 |
| Creative night | voice, video, music, social | #F7F6F9 / #FFFFFF | #16141B / #5C5866 | #DEDBE3 | #B5179E / #FFFFFF | #C6F432 / #16141B | #0E0D11 / #18161D | #F1EFF5 / #A8A3B3 | #F06AD8 / #0E0D11 |
| Quiet premium | luxury, fashion, editorial | #F6F5F2 / #FFFFFF | #161513 / #5F5B54 | #DDD9D1 | #1C1B19 / #FFFFFF | #B08D57 / #161513 | #0D0D0C / #171615 | #EEEBE5 / #A8A39A | #D8BC8A / #0D0D0C |
| Energetic fitness | workout, running, sport | #F6F7F7 / #FFFFFF | #121416 / #565C62 | #D8DCDF | #C93C0A / #FFFFFF | #2563EB / #FFFFFF | #0D0F10 / #17191B | #ECEFF1 / #A0A7AD | #FF7A45 / #0D0F10 |
| Fresh kitchen | recipes, food, grocery | #FBF8F3 / #FFFFFF | #211C17 / #675E55 | #E8E0D5 | #B83E22 / #FFFFFF | #5A6D2F / #FFFFFF | #14110E / #1E1A16 | #F3EEE7 / #B3A99D | #F0876B / #14110E |
| Bright learning | education, language, quiz | #F7F9FC / #FFFFFF | #13203A / #55617A | #D8E0EC | #1F6FEB / #FFFFFF | #FFD23F / #13203A | #0D121C / #161D2A | #EAF0F8 / #A0ACC2 | #7FB0FF / #0D121C |

Notes: accents are measured as fills with their label. As an icon, badge edge or line on the light background, six of them are under 3:1 (DR-002): use them as fills, or use a darker step. Quiet premium marks actions by shape (filled black buttons), since its primary is close to its text color: links and selected text then need an underline, a weight or an icon (rule 2). Mystic night and Quiet premium are gold-brand recipes: their premium marker needs another cue (rule 9). In dark, labels on the primary are dark (the "On" column), since the primary turns light. Mystic night's dark primary is its gold: the indigo moves to surfaces. A recipe has no semantic set; pick error, warning and success per rule 6 and measure them. Border steps are for dividers and card edges; a control edge that must be seen needs 3:1 (DR-002), so use a darker step for input outlines.

## Japanese color combinations (Sanzo Wada)

Sanzo Wada's *A Dictionary of Color Combinations* (Seigensha) is a good source of palettes that feel crafted rather than generated:
- Vol. 1 (2010 reprint of Haishoku Soukan, 1933 to 1934): 348 combinations of 2, 3 and 4 colors, from 159 colors. A free digital version of Vol. 1 is the MIT-licensed dataset github.com/mattdesl/dictionary-of-colour-combinations (colors.json: name, combination ids 1 to 348, CMYK, Lab, RGB, hex). Its hex values are converted from print CMYK, so they are close to the book, not exact.
- Vol. 2 (2020, Wada's works from 1935 to 1936 and 1938): 72 combinations of three to seven colors themed on the twelve months, and 165 combinations from 1910s to 1930s Japanese fashion, interior and graphic design. There is no complete digital version: use the designer's copy and cite the page.
- wada-sanzo-colors.com has the Vol. 1 colors with some corrected values, and a seasons collection.

Wada's combinations are print and textile harmonies, not UI systems. Four equal colors as UI fills break taste rules 3 and 4. Turn one into an app palette like this:
1. Pick two or three combinations that match the brief's mood. Name them by number (Vol. 1) or page (Vol. 2) so the designer can look them up.
2. Give each color one role: the most muted or darkest becomes the neutral hue (tint the neutral ramp toward it), the clearest mid-tone becomes the primary, one other becomes the accent or illustration color. A seasonal set (Vol. 2) suits art, seasonal themes and event screens, not the core UI.
3. Keep the hue, then adjust lightness and chroma in OKLCH until the pairs pass (text 4.5:1, controls 3:1). Say which values moved from the book and by how much.
4. Show the original swatches next to the adjusted ramp on the style tile, with the combination number, so the designer sees the source and the change.
5. The dataset and the books are references, not a license to copy a whole page layout or chip set into a product.

Wada's combinations often pair a soft, low-chroma color with a deeper one and a small strong note. That is the same structure as a good UI palette (neutral, primary, accent), which is why they translate well. This is an observation, not a rule the books state.

### Wada starter palettes (Vol. 1, verified)

Eight Vol. 1 combinations already turned into roles by the steps above, so a designer can pick one without the conversion work. Source hex is from the mattdesl dataset (print CMYK converted, close to the book). Built on 2026-11-28 in OKLCH: neutrals keep the hue of the source's neutral color at chroma 0.003 to 0.03; the primary and accent keep their source hue; lightness moved only where a pair failed, and chroma only where noted below. Every row passes the same checks as the recipes above (text on background at least 7:1, secondary text at least 4.5:1, labels at least 4.5:1, primary at least 3:1, the same in dark). The name is ours, for talking about it; the number is Wada's.

| Combination | Fits | Source colors | Bg / Surface | Text / Text 2 | Border | Primary / On | Accent / On | Dark bg / surface | Dark text / text 2 | Dark primary / on |
|---|---|---|---|---|---|---|---|---|---|---|
| 140 Harbor slate | finance, utility, productivity | Slate Color #34454C, Antwarp Blue #007190, Golden Yellow #F3A257 | #F5F7F8 / #FDFEFE | #171B1D / #606466 | #D9DDDF | #007190 / #FFFFFF | #F3A257 / #171B1D | #0D1011 / #171A1B | #E9EBEC / #ABAFB0 | #82BBD2 / #0D1011 |
| 135 Garden morning | wellness, habits, plants | Sulpher Yellow #F5ECC2, Cossack Green #437742, Salvia Blue #97ACC8 | #F8F7F2 / #FEFDFC | #1D1B12 / #65635B | #DEDCD5 | #437742 / #FFFFFF | #97ACC8 / #1D1B12 | #110F0B / #1B1A14 | #ECEBE7 / #AFAEA7 | #97BD95 / #110F0B |
| 155 Festival ember | fitness, sport, events | Deep Indigo #051230, Jasper Red #EB5324, Benzol Green #00978D | #F4F7FC / #FDFDFE | #161B24 / #5F636C | #D8DCE4 | #C54E2C / #FFFFFF | #00978D / #161B24 | #0D0F14 / #171A1F | #E9EBEF / #AAAEB5 | #EF977E / #0D0F14 |
| 226 Night lantern | astrology, tarot, sleep | Vistoris Lake #6D4145, Violet #4F4086, Cream Yellow #FDBF68 | #FCF5F5 / #FEFDFD | #221718 / #6B6061 | #E4DADA | #4F4086 / #FFFFFF | #FDBF68 / #221718 | #140D0E / #1E1718 | #EFEAEA / #B5ABAC | #B0A9E0 / #140D0E |
| 190 Ink and vermilion | recipes, editorial, reading | Ivory Buff #EBD3A2, English Red #D96629, Black #111314 | #F9F6F1 / #FEFDFB | #1F1A0F / #686359 | #E0DCD3 | #C2520B / #FFFFFF | #233036 / #FFFFFF | #120F09 / #1C1913 | #EDEBE7 / #B1ADA5 | #EC9A74 / #120F09 |
| 227 Spring tide | kids health, care, family | Hermosa Pink #F9C1CE, Cerulian Blue #0093A5 | #FCF5F6 / #FEFDFD | #23171A / #6C6062 | #E4D9DB | #038191 / #FFFFFF | #F9C1CE / #23171A | #140D0F / #1E1719 | #EFE9EB / #B5ABAD | #7EBDC8 / #140D0F |
| 343 Indigo workshop | notes, journaling, craft, learning | Ivory Buff #EBD3A2, Vandar Poel's Blue #064F6E, Burnt Sienna #AE5224 | #F9F6F1 / #FEFDFB | #1F1A0F / #686359 | #E0DCD3 | #064F6E / #FFFFFF | #C96A3E / #1F1A0F | #120F09 / #1C1913 | #EDEBE7 / #B1ADA5 | #8EB8D0 / #120F09 |
| 141 Citrus harbor | language, quiz, kids learning | Dark Tyrian Blue #12354E, Orange #F37420 | #F3F7FB / #FDFDFE | #131C22 / #5C646B | #D6DDE3 | #0369A2 / #FFFFFF | #F37420 / #131C22 | #0B1014 / #151A1E | #E8ECEE / #A8AFB4 | #82B8E3 / #0B1014 |

What moved from the book (OKLCH lightness, chroma where it changed): Festival ember primary 0.64 to 0.58 (chroma 0.20 to 0.16), Ink and vermilion primary 0.64 to 0.58 and its ink accent 0.18 to 0.30 (chroma 0.004 to 0.02, a slate tint), Spring tide primary 0.61 to 0.55 (chroma 0.105 to 0.095), Indigo workshop accent 0.55 to 0.63, Citrus harbor primary 0.32 to 0.50 (chroma 0.06 to 0.12: Wada's navy became a usable blue; the navy stays as the text tint). Everything else keeps the book's value. Show the original swatches beside these on the style tile (step 4 above).

Notes: as an icon, line or badge edge on the light background, five accents are under 3:1 (all but Festival ember, Indigo workshop and Ink and vermilion's ink): use them as fills with their label, or a darker step (DR-002). Festival ember pairs a red primary with a green accent, so its error red and success green move clearly away from both (rule 6) and every state keeps an icon (DR-003). Ink and vermilion's accent is ink, not a hue: use it for filled highlight cards and tags, not as a second action color. Night lantern's cream yellow reads as gold: if the app has IAP, mark premium with another cue (rule 9). Like the recipes, these have no semantic set, dark accent or dark border: derive and measure them.

## Suggesting a palette (stage 3)

1. Read the BRIEF: audience, mood words, brand colors already fixed, platforms, whether there is a dark appearance, and IAA/IAP. Ask for what is missing. Never invent a brand color.
2. Propose two or three options: a recipe above, a Wada starter palette, another Wada combination turned into roles, or the brand's own color run through the ramp steps. Say in one line why each fits the brief.
3. For each, draw one style tile on page Design: a sample screen (header, list, primary button, a badge, an error field), the ramps, and the dark version if the app has one.
4. Add a contrast table under the tile: each text, icon and control pair with its ratio, light and dark. Fails are fixed before showing, or flagged.
5. After the designer picks, write the values into App Color and the rule "Color: <recipe or source>, why: <reason>" through the Approval loop. Then run the done check and offer the color review.

## Sources

Material 3 color roles and HCT tones (m3.material.io/styles/color; material.io/blog/science-of-color-design), Material dark theme (m2.material.io/design/color/dark-theme), Apple HIG Color (developer.apple.com/design/human-interface-guidelines/color), App Store Connect "Differentiate without color alone", Radix Colors "Understanding the scale" (radix-ui.com/colors/docs/palette-composition/understanding-the-scale), Refactoring UI "Building your color palette", OKLCH (evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl), WCAG 2.2 contrast, Sanzo Wada *A Dictionary of Color Combinations* Vol. 1 and 2 (en.seigensha.com), mattdesl dataset. Research date 2026-11-26.
