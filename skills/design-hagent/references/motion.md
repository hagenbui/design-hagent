# Motion

Part of the design-hagent skill. Read when a task names an animation, a transition, a duration or an easing, when you label flow arrows, or when you write the Motion line of a part description. SKILL.md still applies.

## Where the values live

- Motion values live in the base file, never in this skill. Look for the block MOTION on page AGENT RULES and the variable collection Motion (duration-* as Number, easing-* as String). If they exist, they win over everything below.
- Until they exist, motion is a proposal: board "Motion proposal board (2026-11-24)" on base page Design. Use its token names in notes and descriptions, mark them "pending", and never put raw milliseconds or curves into rules, parts or screens.
- Tier 2 files mirror the base Motion collection. An app never adds its own durations or easings; a gap goes to the base as a finding, like any missing token.

## Proposed scale (pending, Material 3 values)

| Token | Value | Use for |
|---|---|---|
| duration-xs | 100 ms | pressed feedback, state color change |
| duration-sm | 200 ms | selection controls, toast, fade; exit of dialog and sheet |
| duration-md | 300 ms | dialog and sheet enter, expand, content change in one screen |
| duration-lg | 500 ms | custom screen transitions, result screens; the maximum for UI |
| easing-standard | 0.2, 0, 0, 1 | moves that stay on screen; the default |
| easing-enter | 0.05, 0.7, 0.1, 1 | things entering the screen |
| easing-exit | 0.3, 0, 0.8, 0.15 | things leaving the screen, always one duration step shorter than enter |

Open question for the designer: Material 3 Expressive moved components to springs. The base keeps cubic curves until the designer decides.

## Transition types on flows

Every arrow and jump tag on a flows page names its trigger and its transition type, as "Trigger · Type" (for example "Start · Push"). Types:
- Push: one level deeper, with Back. Use the platform transition.
- Dialog: scrim fades, dialog fades and scales in.
- Sheet: bottom sheet slides up, scrim fades, drag down closes.
- Replace: the screen is swapped with no Back (onboarding done, splash). Cross-fade.
- Tab: bottom navigation tab change. Cross-fade only, no slide.
- None: instant change.

Prefer the iOS and Android system transitions. Motion tokens are for custom motion only.

## Draft rules to apply (pending in the base)

- Motion has a purpose: where you went, what changed, that a tap registered. No motion on frequent interactions beyond pressed feedback. (Apple HIG Motion)
- Motion never carries meaning alone: the end state shows it in text, icon or state. (Apple HIG Motion)
- Reduce Motion (iOS) or Remove animations (Android): slides and scales become a duration-sm fade, or no motion. A rule, not a Figma mode.
- Never block input while motion plays; the person can tap or cancel. (Apple HIG Motion)
- Close controls on paywalls, ads and dialogs appear at once, with no delayed fade and no motion that moves the tap area.
- Haptics: system patterns only (notification success, warning, error; impact light, medium, heavy; selection), paired with a visible change and used sparingly: task success, picker and toggle ticks, before a destructive step, snap points. Never on every tap or scroll, never the only signal. Name it with the transition, "Done · Push · Success haptic". (Apple HIG Playing haptics)
- Gestures follow the finger from the first frame and keep momentum on release; reversible swipe actions may fire mid-swipe, destructive ones only on release; sheets and popovers grow from the element that opened them. (references/identity.md, "Premium finish")
- Waits: under 1 s nothing, 1 to 10 s a looping spinner or skeleton (linear), over 10 s progress and a Cancel. (NN/g response times)

## Building motion in Figma

- Load the figma-use-motion skill before any keyframe or animation style work. Motion and custom animation styles were available in the base file on 2026-11-24; if a call says "not a supported API", stop and tell the designer, never fall back silently.
- Reusable motion is a local custom animation style named Motion/<Part> <enter or exit> (for example Motion/Sheet enter), built from the approved tokens. Never keyframe each screen by hand when a style exists.
- Keyframes go on children, never on a top-level frame. A screenshot shows only the resting state; exporting video is slow, so check timing by reading the keyframes unless the designer asks for a video.
- Motion follows the Approval loop like any token, style or rule.

Sources: Material 3 motion specs (m3.material.io/styles/motion/overview/specs), Material 3 easing and duration tokens, Apple HIG Motion (developer.apple.com/design/human-interface-guidelines/motion), Apple HIG Playing haptics (developer.apple.com/design/human-interface-guidelines/playing-haptics), Rauno Freiberg "Invisible Details of Interaction Design" (rauno.me/craft/interaction-design), NN/g response time limits.
