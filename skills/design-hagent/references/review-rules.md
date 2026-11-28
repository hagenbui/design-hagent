# Review rules

Part of the design review (references/review.md). Read the groups a screen needs, not the whole file at once. SKILL.md and review.md still apply.

Each rule: id, title, kind (measure = a number decides; judge = a reasoned call), scope (screen or flow), what to check, when it applies, the exception, source. Ids follow the legacy rulebook (MDR-0xx became DR-0xx), so old Varmeta reports map one to one. Ids from DR-101 up are new in this skill and have no legacy match. The legacy book had no rules 004 to 024, 033, 047, 051 to 053, 061, 062, 064, 093, 094.

A rule in the file's RULES block wins over these. Check platform rules (iOS only, Android only) only once the platform is known.

## Accessibility

- **DR-001 Text contrast** (measure, screen). Text stays legible on its real background. Pick the normal or large threshold only after checking size and weight. WCAG: 4.5:1 normal, 3:1 large (18 pt regular or 14 pt bold; 1 pt = 1.333 px). Android: same ratios in sp. iOS: Apple HIG Accessibility contrast table. When: informative text. Except: logos, incidental text, inactive controls, text that is part of an image. Sources: wcag-contrast-minimum, android-accessibility, apple-accessibility, wcag2ict.
- **DR-002 Non-text contrast** (measure, screen). The parts needed to see a control, its state or a meaningful graphic reach 3:1 against neighbors. When: control edges, states, meaningful icons. Except: inactive controls, unmodified system controls. Sources: wcag-non-text-contrast, wcag2ict.
- **DR-003 Not color alone** (judge, screen). Selected, error and status states carry a cue beyond hue (icon, text, weight, check). When: color shows a state. Except: decoration. Sources: wcag-use-of-color, wcag2ict.

## Controls

- **DR-025 Touch target size** (measure, screen). Measure the tappable wrapper after the unit mapping is known. iOS: 44 x 44 pt recommended (28 pt accessibility minimum). Android: 48 x 48 dp recommended. When: a control with a clear tap area. Except: these are recommendations, not WCAG certification. Sources: android-accessibility, apple-buttons, apple-accessibility.
- **DR-045 Action button labels** (judge, screen). A label says what will happen. Except: familiar icons may stand alone. Source: apple-buttons.
- **DR-046 Clear main action** (judge, screen). Emphasis follows task priority so the next step is obvious. Except: equal actions may look equal. Source: apple-buttons.
- **DR-048 Destructive emphasis** (judge, screen). Delete and data-loss actions look as risky as they are. Except: on a confirm the user already chose, judge in that context. Source: apple-buttons.
- **DR-049 Space between controls** (judge, screen). Neighboring tap areas are far enough apart to avoid wrong taps. Except: no universal 12 or 24 pt rule. Source: apple-accessibility.
- **DR-089 Switch means on or off** (judge, screen). A switch has a label and a clear current state. A row that opens a screen is not a switch. Source: material-switch.
- **DR-090 Picker order** (judge, screen). Values follow an order people expect (number, date, A to Z). Except: an explained priority order. Source: apple-pickers.
- **DR-091 Exact slider value** (judge, screen). A wide-range slider where precision matters offers another way to set an exact value. Except: feel-based values like volume. Source: apple-sliders.

## Typography

- **DR-026 Readable size, iOS** (measure, screen). iOS default 17 pt, minimum 11 pt, judged by text role, after units are confirmed. Except: don't apply 17 pt to captions or to Android. Source: apple-typography.
- **DR-027 Readable weight** (judge, screen). Thin type at small sizes hurts legibility; judge with size and background. Except: a brand font is not a defect by itself. Source: apple-typography.
- **DR-028 Type hierarchy** (judge, screen). Size, weight and color separate headings, content and support text. Except: no universal scale. Source: apple-typography.
- **DR-029 Purposeful typefaces** (judge, screen). Each typeface has a role. Except: no hard maximum. Source: apple-typography.
- **DR-030 Keep important text** (judge, screen). Long labels and large-text versions stay understandable; check clipping. Except: ellipsis is fine when the full text is reachable. Source: apple-typography.

## Color

- **DR-031 Same color, same meaning** (judge, screen). Functional colors keep one meaning across screens. Except: decoration. Source: apple-color.
- **DR-032 Dark appearance** (judge, screen). Art, logos and surfaces work in each supported appearance. Except: missing dark frames don't prove the app lacks dark mode. Source: apple-dark-mode.
- **DR-034 Increased contrast** (judge, screen). Functional colors have a higher-contrast variant or use system colors. Except: custom colors with suitable variants. Source: apple-color.

## Layout

- **DR-035 System bars and cutouts** (judge, screen). Taps and key content stay clear of status bar, cutouts and the gesture area. Except: backgrounds may run edge to edge. Source: android-insets.
- **DR-036 Alignment** (judge, screen). Equal items align so lists scan easily. Except: deliberate offsets for hierarchy. Source: apple-layout.
- **DR-037 Grouping** (judge, screen). Spacing, dividers and containers show what belongs together. Except: no mandatory 8 pt grid (the file's spacing tokens decide). Source: apple-layout.
- **DR-038 Progressive disclosure** (judge, screen). Secondary choices don't compete with the main task. Except: never hide what a safe or informed decision needs. Source: apple-layout.
- **DR-039 Art proportions** (judge, screen). Scaled images keep their proportions. Except: deliberate crops. Source: apple-layout.

## Navigation

- **DR-040 Clear nav labels** (judge, screen). Nav icons and labels name their destination. Source: material-navigation.
- **DR-041 Tabs are places** (judge, screen). A tab bar switches areas, never saves or deletes. Except: an action toolbar is not a tab bar. Source: apple-tab-bars.
- **DR-042 Stable tabs** (judge, flow). The shared tab bar keeps its destinations and order across screens. Except: full modals may cover it. Source: apple-tab-bars.
- **DR-043 Tab count, Android** (judge, screen). A Material navigation bar holds 3 to 5 frequent destinations. Except: not for iOS or other nav patterns. Source: material-navigation.
- **DR-044 Visible active tab** (judge, screen). The current destination is clearly marked. Source: material-navigation.

## Forms

- **DR-050 Labels that stay** (judge, screen). A field is still identifiable after typing; a placeholder alone is not enough. Except: floating labels; simple search. Source: nng-placeholders.
- **DR-054 Field fits the text** (judge, screen). Short input gets a field, long input a multi-line area. Source: apple-text-fields.

## States

- **DR-055 Loading is clear** (judge, screen). People see that something loads and what for. Except: a state not in scope is "cần kiểm tra". Source: apple-loading.
- **DR-056 Honest progress** (judge, screen). A percentage bar only when completion can be estimated; otherwise a spinner. Source: apple-progress-indicators.
- **DR-057 Cancel long waits** (judge, screen). A long task can be stopped, with its result explained. Except: tasks that can't stop explain why. Source: apple-progress-indicators.
- **DR-058 Done feedback** (judge, screen). Save, apply and finish show a visible result. Except: an obvious result needs no extra toast. Source: apple-feedback.

## Errors

- **DR-059 Name the error** (judge, screen). The message points at the field and says what is wrong. Source: wcag-error-identification, wcag2ict.
- **DR-060 Next step** (judge, screen). A recoverable error offers a concrete action (Try again, edit). Source: wcag-error-suggestion, wcag2ict.

## Dialogs and sheets

- **DR-063 Clear exit** (judge, screen). A task sheet has Cancel, Close or Back. Except: required flows (for example Update required) need a stated reason. Source: apple-sheets.
- **DR-065 No stacked sheets** (judge, flow). Sheets don't pile up into an unclear return path; check real links, not canvas position. Source: apple-sheets.
- **DR-066 Interrupt only when it matters** (judge, screen). Alerts are for risk or importance; routine info goes inline. Source: apple-alerts.

## Search

- **DR-067 Search scope** (judge, screen). People know what the field searches. Source: apple-search-fields.
- **DR-068 Relevant results** (judge, screen). Results match the query. Except: needs a real query, not mock data. Source: apple-search-fields.
- **DR-069 Visible filters** (judge, screen). Active scope and filters are shown. Source: apple-search-fields.
- **DR-070 Suggestions** (judge, screen). Suggestions or recents help when recall or typing is hard. Except: not every app needs them. Source: apple-search-fields.

## Onboarding

- **DR-071 Short and skippable** (judge, flow). The intro teaches only what matters and can be skipped. Except: safety steps. Source: apple-onboarding.
- **DR-072 Help in context** (judge, screen). Tips appear at the feature, when needed. Source: apple-onboarding.
- **DR-073 Learn by doing** (judge, screen). New gestures are taught with a safe try. Source: apple-onboarding.
- **DR-074 Setup later** (judge, flow). Setup that isn't needed for first use doesn't delay it. Source: apple-onboarding.
- **DR-075 Value before asking** (judge, flow). Rating asks and paywalls come after people have seen the value. Except: apps that are paid by nature. Source: apple-onboarding. Matches the rate app rule in references/app-flows.md.

## Privacy

- **DR-076 Ask in context** (judge, flow). A permission is asked when its link to the task is clear. Except: permissions the app can't start without. Source: apple-privacy.
- **DR-077 Say why** (judge, screen). Pre-permission copy names the access and its purpose. Source: apple-privacy.
- **DR-078 Ask for less** (judge, flow). Permissions match what the task needs. Except: proving over-collection needs technical checks. Source: apple-privacy.
- **DR-079 No misleading pre-permission** (judge, screen). The screen before the system prompt doesn't misstate the choices. Source: apple-privacy.

## Paywall

- **DR-080 Billed amount first** (judge, screen). The amount actually charged per period is clear and bigger than any per-week or per-month equivalent. Source: apple-subscriptions.
- **DR-081 Price after trial** (judge, screen). A free trial states its length and the price that follows. Source: apple-subscriptions.
- **DR-082 Restore** (judge, flow, iOS). Existing subscribers can restore or sign in. Except: one paywall frame can't prove it's missing. Source: apple-subscriptions.
- **DR-083 What and how long** (judge, screen). The offer states what people get and for how long. Source: apple-subscriptions.
- **DR-084 Terms and privacy** (judge, screen, iOS). Terms and privacy are findable in the purchase flow. Source: apple-subscriptions.

## Accounts

- **DR-085 Sign in only when needed** (judge, flow). Source: apple-managing-accounts.
- **DR-086 Right auth names** (judge, screen). Face ID, Touch ID and others match the device. Source: apple-managing-accounts.
- **DR-087 Delete account** (judge, flow). Apps with account creation offer a findable way to delete it. Source: apple-managing-accounts.
- **DR-088 Delete and subscriptions** (judge, flow). Deleting explains what happens to a subscription. Source: apple-managing-accounts.

## Scrolling and content

- **DR-092 Visible scrolling** (judge, screen). People can tell there is more below or beside. Except: a cut-off item can be the cue. Source: apple-scroll-views.
- **DR-095 People's words** (judge, screen). Labels use the audience's words. Source: apple-writing.
- **DR-096 Not by shape or place alone** (judge, screen). Instructions name controls, not only "the round button on the right". Source: wcag-sensory-characteristics, wcag2ict.
- **DR-097 Descriptive headings** (judge, screen). Headings and labels say what follows. Source: wcag-headings-and-labels, wcag2ict.

## Consistency

- **DR-098 Same function, same name** (judge, flow). A repeated function keeps its label and icon. Source: wcag-consistent-identification, wcag2ict.
- **DR-099 Same part, same look** (judge, flow). Parts with the same job follow the design system. In this system the wraps and the reapply rule decide. Source: nng-heuristics.
- **DR-100 Help in the same place** (judge, flow). Repeated help sits in the same relative spot. Source: wcag-consistent-help, wcag2ict.

## Color palette

Color audit rules, added in skill 2.20 (2026-11-26). The craft behind them is in references/color.md. Contrast itself stays DR-001 and DR-002. Read the app's palette rule in its RULES block first: an approved choice there wins. Count what you see (hues, where the primary appears, area share) and report the counts as evidence.

- **DR-101 Color is scarce** (judge, screen). Neutrals carry most of the screen; strong color marks the main action, the selected state or one highlight. Fail when three or more large saturated areas compete, or nothing stands out. Except: art, photos, games, kids screens with a rule allowing more. Sources: apple-color, refactoring-ui-color.
- **DR-102 One action color** (judge, flow). The primary color marks what can be tapped or what is selected, and is not used for plain headings, body text or decoration. Except: brand art. Source: apple-color.
- **DR-103 Few hues** (judge, screen). Count UI hues outside art (a hue counts when it is clearly a different color, not a tint of one already counted): one primary, at most one accent, plus semantic colors where a state is shown. Each extra hue needs a job no role does. Except: category colors with a rule (tags, calendars). Source: refactoring-ui-color.
- **DR-104 One neutral family** (judge, flow). Greys, surfaces and borders share one temperature and lean toward the brand hue. Cool and warm greys mixed on one screen, or a pure neutral grey beside a tinted one, is a fail. Except: base colors inside wraps that are logged as known limits in FINDINGS (Switch, Radio, CheckBox, overlay scrim, finding T2): point to the T item, don't fail again. Sources: refactoring-ui-color, radix-scale.
- **DR-105 States from the ramp** (judge, screen). Pressed, selected, disabled and hover fills are steps of their role's ramp or the neutral ramp, not new hues or ad hoc opacities. Except: the same known limits as DR-104. Sources: radix-scale, material-color.
- **DR-106 Chroma by area** (judge, screen). Large areas (backgrounds, headers, big cards) are low chroma; full chroma stays on small areas. In dark, primary and accent are lighter and less saturated, and surfaces are dark grey, not pure black. Except: hero art, full-screen media. Sources: material-dark-theme, material-color.
- **DR-107 Works in grayscale** (judge, screen). In a grayscale screenshot, the main action, the selected state and errors still stand out by lightness, icon or text. Pairs with DR-003. Source: appstore-color-alone.
- **DR-108 Semantic colors keep meaning** (judge, flow). Error, warning and success differ from the primary and from each other, and keep one meaning across screens (DR-031). Fail when the error red matches a red brand button, or success green is also used for decoration. Sources: apple-color, wcag-use-of-color.
- **DR-109 Premium color is reserved** (judge, flow, IAA/IAP; candidate, report as "Góp ý UX" until the designer approves it). The premium or gold color appears only on paywall, Premium badges and locked markers. Except: an app whose brand is gold, which then marks premium with another cue (icon, label). Source: references/color.md rule 9.
- **DR-110 Text on gradients and art** (measure, screen). Text over a gradient, image or tint passes DR-001 at its worst point; otherwise "cần kiểm tra" with a pixel check. Source: wcag-contrast-minimum.

## Distinctive look and smart UX

Added in skill 2.21 (2026-11-27). The craft behind them is in references/identity.md. Read the app's signature rules first: approved style and art rules in RULES and any block it points to for art (such as ART DIRECTION), whatever their heading (references/identity.md, "What counts as the app's signature rules"). DR-121 and DR-122 check the finish (references/identity.md, "Premium finish"). DR-111 to DR-114 fail only against such an approved rule or a countable tell; with none, report them as "Góp ý UX" and suggest a kit. Count what you see (tells, signature elements per moment screen, text layers) and report the counts.

- **DR-111 Not generic** (judge, screen). Fail when three or more generic tells from references/identity.md show with no app rule choosing them, or the base placeholder typeface or colors still show. Except: wireframes (new app stage 4), base colors logged as known limits in FINDINGS (finding T2, as in DR-104), and a typeface or color an app rule chose. Source: apple-branding.
- **DR-112 Signature on moment screens** (judge, flow). Splash, onboarding, empty, result, success and paywall use the app's signature elements (art, motif, display type); a flat, art-less moment screen fails. Except: system UI. Sources: apple-branding, lawsofux-peak-end.
- **DR-113 One art style** (judge, flow). Illustrations, motifs and icons share one medium, line weight, palette and perspective; icons come from one set. Except: photos and user content. Source: apple-branding.
- **DR-114 Signature stays quiet where people work** (judge, screen). Patterns, motifs and display type don't sit behind body text, lists or forms, and never lower legibility (DR-001, DR-110). Source: apple-branding.
- **DR-115 Within the text level** (judge, screen). Text stays within the app's Text level (base 7.13): no eyebrows, repeated subtitles, "Tap to" captions or tips; a line that art, an icon or a visible state could carry is a fail. Except: screens raised to Guided in the app's RULES, legal and price text. Source: apple-writing.
- **DR-116 Smart defaults and memory** (judge, flow). The most common or safest option is preselected, the last choice, filter or tab is kept, and search shows recents before results. Evidence is static: a drawn preselected or recents state, or a note on the canvas; without it, "cần kiểm tra", not fail. Except: consent opt-ins and paid add-ons, which are never pre-checked (a preselected paywall plan is fine when DR-080 and DR-081 pass). Source: nng-heuristics.
- **DR-117 Prevent, then undo** (judge, flow). Input is constrained (pickers, steppers, disabled impossible options) instead of explained; a reversible action offers Undo instead of a confirm dialog; confirm stays for what can't be undone. Evidence is static: a drawn Undo snackbar or constrained control, or a note; without it, "cần kiểm tra", not fail. Sources: nng-heuristics, apple-undo.
- **DR-118 One next step** (judge, screen). One primary action per screen; result and success screens offer the natural next action, not only Close; rare options sit behind More. Sources: lawsofux-hick, nng-heuristics.
- **DR-119 Native controls** (judge, screen). Switches, pickers, steppers, segmented controls, alerts, action sheets, sheets, navigation bars, tab bars and back keep the platform's shape and behavior; a control redrawn for flavor fails (references/identity.md, "Native first"). Except: game screens and controls with no platform equivalent. Sources: nng-heuristics, apple-layout.
- **DR-120 One focal point** (judge, screen). Each screen has one element that leads (the main content or the one primary action) and the rest steps back; equal weight everywhere, or several primary-styled buttons, fails. Pairs with DR-028 and DR-118. Sources: apple-layout, apple-buttons.
- **DR-121 Finish details** (measure, screen). Added in skill 2.25. iOS wraps use continuous corners (corner smoothing about 60%, read from the node); an inner corner equals the outer corner minus the padding between them (zero as the floor); one depth method per app (background step, one soft shadow or a hairline border, not a border plus a shadow); times, prices, timers and counters use one format and tabular digits; gaps and colors a step apart from a token (12, 13 and 14 px) fail as off-token. Report the node and the measured values. Except: Android screens for corner smoothing, user content, and what an app rule chose. Where the file can't show it (tabular digits not readable), "cần kiểm tra", not fail. Sources: apple-layout, apple-typography.
- **DR-122 Haptics and gestures noted** (judge, flow). Added in skill 2.25. Task success, pickers, destructive steps and snap points name their haptic on the flow arrow or the part's Motion line, using the system patterns and paired with a visible change; swipe actions say whether they trigger mid-swipe (reversible only) or on release (destructive); sheets and popovers open from the element that opened them. A haptic on every tap, a destructive action firing mid-swipe, or a haptic as the only signal fails. With no notes at all, "cần kiểm tra", not fail. Sources: apple-haptics, apple-feedback.

## Candidate rules from Varmeta DESIGN.md (to confirm, not approved)

Report these as "Góp ý UX" until the designer approves them into a RULES block.

- **H-01 One nav shell.** Every top-level screen shows the same bottom nav: count, order, labels, icons, spacing. Only the active tab changes. Hidden on splash, onboarding, language, permissions, camera, search and full-screen modals.
- **H-02 Search screen.** Bottom nav hidden. States drawn: idle, typing, results, no results. No clear icon before text is typed.
- **H-03 Paywall focus.** Pricing plans are the focal point. Benefits stay smaller and quieter.
- **H-04 Three type sizes.** Most screens use three type sizes or fewer.
- **H-05 Onboarding shape.** 3 to 4 steps, an art area, a title and a subtitle only, Skip and Next.
- **H-06 Minimal splash.** Logo, app name, one short line, a loading line. No other controls.
- **H-07 Ads fit in.** Ads (banner, native small, medium, large, square, interstitial) use the system's spacing and radius and never push the main task out of view.

## Sources

| id | link |
|---|---|
| android-accessibility | https://developer.android.com/guide/topics/ui/accessibility/apps |
| android-insets | https://developer.android.com/design/ui/mobile/guides/layout-and-content/edge-to-edge |
| apple-accessibility | https://developer.apple.com/design/human-interface-guidelines/accessibility |
| apple-alerts | https://developer.apple.com/design/human-interface-guidelines/alerts |
| apple-branding | https://developer.apple.com/design/human-interface-guidelines/branding |
| apple-buttons | https://developer.apple.com/design/human-interface-guidelines/buttons |
| apple-color | https://developer.apple.com/design/human-interface-guidelines/color |
| apple-dark-mode | https://developer.apple.com/design/human-interface-guidelines/dark-mode |
| apple-feedback | https://developer.apple.com/design/human-interface-guidelines/feedback |
| apple-haptics | https://developer.apple.com/design/human-interface-guidelines/playing-haptics |
| apple-layout | https://developer.apple.com/design/human-interface-guidelines/layout |
| apple-loading | https://developer.apple.com/design/human-interface-guidelines/loading |
| apple-managing-accounts | https://developer.apple.com/design/human-interface-guidelines/managing-accounts |
| apple-onboarding | https://developer.apple.com/design/human-interface-guidelines/onboarding |
| apple-pickers | https://developer.apple.com/design/human-interface-guidelines/pickers |
| apple-privacy | https://developer.apple.com/design/human-interface-guidelines/privacy |
| apple-progress-indicators | https://developer.apple.com/design/human-interface-guidelines/progress-indicators |
| apple-scroll-views | https://developer.apple.com/design/human-interface-guidelines/scroll-views |
| apple-search-fields | https://developer.apple.com/design/human-interface-guidelines/search-fields |
| apple-sheets | https://developer.apple.com/design/human-interface-guidelines/sheets |
| apple-sliders | https://developer.apple.com/design/human-interface-guidelines/sliders |
| apple-subscriptions | https://developer.apple.com/app-store/subscriptions/ |
| apple-tab-bars | https://developer.apple.com/design/human-interface-guidelines/tab-bars |
| apple-text-fields | https://developer.apple.com/design/human-interface-guidelines/text-fields |
| apple-typography | https://developer.apple.com/design/human-interface-guidelines/typography |
| apple-undo | https://developer.apple.com/design/human-interface-guidelines/undo-and-redo |
| apple-writing | https://developer.apple.com/design/human-interface-guidelines/writing |
| appstore-color-alone | https://developer.apple.com/help/app-store-connect/manage-app-accessibility/differentiate-without-color-alone-evaluation-criteria |
| lawsofux-hick | https://lawsofux.com/hicks-law/ |
| lawsofux-peak-end | https://lawsofux.com/peak-end-rule/ |
| material-color | https://m3.material.io/styles/color/system/overview |
| material-dark-theme | https://m2.material.io/design/color/dark-theme |
| material-navigation | https://github.com/material-components/material-components-android/blob/master/docs/components/BottomNavigation.md |
| material-switch | https://github.com/material-components/material-components-android/blob/master/docs/components/Switch.md |
| nng-heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ |
| nng-placeholders | https://www.nngroup.com/articles/form-design-placeholders/ |
| radix-scale | https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale |
| refactoring-ui-color | https://www.refactoringui.com/previews/building-your-color-palette |
| wcag-consistent-help | https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html |
| wcag-consistent-identification | https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html |
| wcag-contrast-minimum | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html |
| wcag-error-identification | https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html |
| wcag-error-suggestion | https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html |
| wcag-headings-and-labels | https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html |
| wcag-non-text-contrast | https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html |
| wcag-sensory-characteristics | https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html |
| wcag-use-of-color | https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html |
| wcag2ict | https://www.w3.org/TR/wcag2ict/ |

Legacy rulebook verified these links on 2026-09-20. Recheck before quoting a number in a report.
