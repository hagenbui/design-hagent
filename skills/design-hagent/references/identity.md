# Distinctive look and smart UX

Part of the design-hagent skill. Read when you set an app's visual style (new app stage 3, a restyle), make or prompt art, patterns or illustrations, build a moment screen (splash, onboarding, empty, result, success, paywall), or review the look (references/review-rules.md, group "Distinctive look and smart UX"). SKILL.md still applies; color has its own file, references/color.md.

An app built only from defaults looks machine-made: it could be any app with the logo covered. Each app needs a few signature choices, made once, written as rules, and repeated on every screen, plus UX that thinks for the user so screens need fewer words.

## Where it lives

- The signature lives only in the tier 2 file: the style rules in its RULES block (the template's style rules 2.1, 2.2, 2.4, under a "Signature" heading), patterns, motifs and art as parts on page App Components, values in App Color and Typography. Never in the base (Core principle).
- **What counts as the app's signature rules:** any approved rule that fixes the look, whatever its heading: the style rules (2.1, 2.2, 2.4), an art rule, or a separate block such as ART DIRECTION. An app needs no heading named "Signature". Rules still marked Pending or draft don't count yet.
- Everything here is a suggestion until the designer approves it (Approval loop). Never invent a logo, mascot or brand color; ask for brand material first. Never copy another app's look, art or mascot.

## Generic tells (what makes it read as AI-made)

Count these on a screen. Each one is fine alone when an app rule chose it on purpose; three or more together, with no rule behind them, is the generic look.
1. The base placeholders still showing: Inter and the base placeholder colors, untouched by the app's Typography and App Color. Not counted: base colors logged as known limits in FINDINGS (Switch, Radio, CheckBox, overlay scrim, finding T2), wireframe screens (new app stage 4), and a typeface or color an app rule chose (an app may pick Inter on purpose).
2. A purple-to-blue or rainbow gradient as the main brand color, or gradient text.
3. Glass blur, glow or soft shadow on most surfaces instead of one surface level.
4. The same card repeated in a uniform grid: equal radius, equal size, icon top left, title, two lines of grey text.
5. Stock-looking art: 3D blobs, floating shapes, generic isometric people, sparkles, a robot, emoji used as icons, art that changes style from screen to screen.
6. Icons mixed from different sets (stroke and fill, different weights).
7. A flat empty background on every screen, moment screens included.
8. Filler or vague copy: "Welcome to App", "Unlock your potential", "Seamless", "All-in-one", a headline plus a subtitle that says it again, a bare "Loading..." where the app could say what it is doing ("Reading your palm...").
9. Every screen centered and symmetric, with the same visual weight everywhere and no focal point.
10. Every button styled as primary, so nothing leads.
11. Cards nested inside cards, or a thick colored bar on the left edge of cards, list items or alerts.
12. Soft-shadowed rounded boxes, rings or sparklines standing in for real content.
13. The same entrance animation on every element instead of one chosen moment.
14. Platform controls redrawn for flavor (see "Native first").

## The signature kit (stage 3)

Derive it from the BRIEF: three mood words, the audience, and one object from the app's domain (a palm line, a dumbbell plate, a recipe card, a star chart). The domain object is the seed of the motif, so the look belongs to this app only. Write each choice as one rule with its Why.

- **Mood words are concrete.** Name things you could photograph or touch ("worn paper, ink, night sky", "chalk, rubber floor, stopwatch"). "Clean, modern, simple, premium" are not mood words: they produce the most average screen. If the brief only has those, ask the designer for concrete ones.
- **Obvious first, then away from it.** Before drafting options, write in one line the direction any generator would pick for this brief (for a meditation app: soft purple gradient, floating blobs, rounded white cards). Then build each option away from it. Show that line on the style tile as "Avoided", so the designer sees what was rejected.
- **A mascot comes from the domain.** A generic cute character is no signature, since many apps have one. If the app has a mascot, derive it from the domain object and the illustration style, and only with the designer's OK.

| Element | Decide | Example |
|---|---|---|
| Illustration style | medium (flat, line, grain, paper cut, 3D clay), line weight, colors taken only from the palette, perspective, how people or a mascot are drawn | "Flat shapes with 2 px ink line, palette primary and accent, front view, no faces" |
| Shape language | corner style beyond the radius token: soft, sharp, cut corner, pill, an organic edge, a ticket notch | "Cards have one cut corner" |
| Background treatment | a pattern, texture or motif from the domain object, low contrast (chroma by area, color.md rule 4), where it appears | "Faint star chart on splash, onboarding and result; plain on lists" |
| Icon style | one set, stroke or fill, one weight per size, plus a few custom icons for the app's key objects | "Rounded stroke 1.5, custom icons for the 3 main features" |
| Display type | an optional display face or weight for big moments only, with clear contrast to body (a large size step and a clear weight step, from the approved text styles); body stays readable | "Serif display on result titles, about 3 times body size" |
| Signature moment | the one screen people remember (peak-end): result, streak, reading, finished workout | "Result card with motif frame, made to be shared" |
| Motion | one character for transitions and feedback, and one authored moment rather than the same entrance everywhere (references/motion.md) | "Quick, slight overshoot on success; result card reveal is the moment" |

Show the kit on the style tile next to the palette: a moment screen and a functional screen, so the designer sees both levels.

## Loud and quiet screens

- Moment screens (splash, onboarding, empty, success, result, paywall, rewards, level up) carry the signature: art, motif, display type.
- Functional screens (lists, settings, forms, search) stay quiet: palette, shape language and icon style only. A pattern behind text or a list costs legibility.
- Art and motif replace words, not sit beside them (base 7.13): an empty state is an illustration plus one line and one button, not a paragraph.
- Every screen has one focal element (the main content or the one primary action) and everything else steps back in size, weight or color. Equal weight everywhere is the generated look.

## Native first

The most common mobile tell is an app that looks ported from a website: platform controls redrawn for flavor. People trust controls they already know.
- Keep the platform's behavior and shape for switches, pickers, steppers, segmented controls, alerts, action sheets, sheets (swipe to dismiss), navigation bars, tab bars and back (the iOS edge swipe, the Android system back). The base parts are built for this; style them through wraps (color, type, radius tokens), not by changing their structure.
- Put the signature where it belongs: art, motif, display type, color and the signature moment. Not into redrawn controls.
- One icon set per app, matching the platform's icon weight and alignment; don't mix a web icon set in.

## Premium finish

An app looks premium because of restraint and finished details, not extra decoration. These are the details that separate a polished app from a sloppy one. Each is a wrap or note decision, made once, not a per-screen effect.
- **Continuous corners.** iOS draws smooth (squircle) corners, not plain circular arcs. On iOS wraps, set corner smoothing to Figma's iOS preset (60%), so cards and buttons sit well next to system controls. Android keeps plain rounded corners (Material shapes).
- **Nested radius.** An inner corner is the outer corner minus the padding between them (a card with radius 24 and padding 12 holds an image with radius 12), with zero as the floor. The same radius at two depths looks off.
- **One depth method.** Show layers one way per app: a background step, one very soft shadow, or a hairline border, used the same everywhere. Hard shadows, a border plus a shadow, or depth on every element look amateur. Write the choice as an app rule.
- **Tabular numbers.** Times, prices, timers, counters and anything that changes in place use tabular (fixed-width) digits so the text doesn't jitter. One time and date format per app (not "09:00 AM" on one screen and "7:00 AM" on another).
- **Optical alignment.** Center icons by eye, not by their box (a play triangle sits slightly right of center). Text and icons in a row share one center line. Values a step apart (12, 13 and 14 px gaps, two near-identical greys) are a defect: use the token.
- **Balanced line breaks.** Text that wraps to two or three lines (titles, headlines, empty-state lines, card titles, centered captions) breaks into lines of near-equal length at a phrase boundary, never one long line over a lone word. Set it by the text box width, not hard returns, so it still works at large text sizes and in a longer language. Note it for developers: Android `breakStrategy="balanced"`, web `text-wrap: balance` (`pretty` for paragraphs, which only avoids a one-word last line). Paragraphs stay ragged-right; centered text is for one to three lines only.
- **Few alignment edges.** Each screen lines up on a few shared edges: the screen margin, one content column, and the center only when the whole group is centered. Text, icons, images and buttons in a stack start on the same edge, and number columns align right. A stray element a few pixels off an edge reads as a mistake.
- **Keyboard-safe action.** When the keyboard is up, the primary action stays visible above it (draw the keyboard state for form screens), and the field in focus is never covered.
- **Haptics with meaning.** Use the platform's system patterns, sparingly, paired with what the screen shows: success at the end of a task, a selection tick on pickers and toggles, a warning before a destructive step, a light impact on snap points. No haptic on every tap or scroll, and never haptics alone (Reduce Motion and silent mode still work). Write it on the flow arrow or the part's Motion line ("Done · Success haptic", references/motion.md).
- **Gestures that follow the finger.** A drag or swipe tracks the finger from the first frame and keeps its momentum on release. Reversible actions may trigger mid-swipe; destructive ones only when the finger lifts. A sheet or popover grows from the element that opened it, and motion can be interrupted. Frequent actions get little or no animation (references/motion.md).
- **Real content.** Judge the finish with realistic data: long names, empty and full lists, large text sizes, real photos. Lorem ipsum and perfect short strings hide the problems.

## Making art consistent

- Write one style prompt block in English per app, approved with the kit, and paste it unchanged into every image prompt (SKILL.md, Images and art). Only the subject changes between prompts.
- Compare each new image with two approved ones before placing it. A different line weight, light or color set is redone, not kept.
- Patterns and motifs are built once as App Components (a tile or a frame part), bound to App Color, and instanced.

## Smart UX (thinking for the user)

Good heuristics also cut text: when the screen does the right thing, it needs no explanation. Existing review rules already cover progressive disclosure (DR-038), done feedback (DR-058), next step after errors (DR-060), alerts only when it matters (DR-066), suggestions (DR-070), help in context (DR-072) and value before asking (DR-075). Add these:
- **Smart defaults.** Preselect the most common or safest option (device language, the popular plan with its billed price clear per DR-080 and DR-081, today's date). The user confirms instead of choosing. Never pre-check consent opt-ins or paid add-ons.
- **Remember.** Keep the last choice, filter, tab and draft. Show recents before an empty search.
- **Fewer decisions.** One primary action per screen, a short list of options, and anything rare behind "More" (Hick's law).
- **Prevent, then forgive.** Constrain input (pickers, steppers, masks, disabled impossible options) instead of explaining rules; offer Undo after a reversible action instead of a confirm dialog. Keep confirm only for actions that can't be undone.
- **Anticipate the next step.** A result or success screen offers the natural next action (share, try again, next item), not only Close.
- **Show state, not instructions.** Progress, selection, limits left ("2 free scans left") and locked items are visible in the UI, not explained in copy.
- **Thumb first.** Frequent actions sit in the bottom reach; destructive ones are away from them.

## Sources

Apple HIG Branding (developer.apple.com/design/human-interface-guidelines/branding), Anthropic "Improving frontend design through Skills" (claude.com/resources/articles/improving-frontend-design-through-skills: distributional convergence, decisive type contrast, one orchestrated motion moment), the Impeccable skill (pbakaus/impeccable: craft floor defaults, iOS and Android slop tests), Fast Company "Big tech is cutewashing its AI agents" (mascots), Superdesign "How to make AI UI look less generic" (concrete specs over adjectives), NN/g ten usability heuristics (nngroup.com/articles/ten-usability-heuristics), Laws of UX: Hick's law and Peak-end rule (lawsofux.com), Apple HIG Undo and redo, Apple HIG Playing haptics, Rauno Freiberg "Invisible Details of Interaction Design" (rauno.me/craft/interaction-design: gestures), David Smith "Changing Corners" and the Apple squircle write-ups (continuous corners), and references/color.md for palette taste. Written 2026-11-27 from the designer's request and online research the same day; Premium finish added 2026-11-28.
