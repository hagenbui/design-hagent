# Review rules

Part of the design-hagent-review skill. Read the groups a screen needs, not the whole file at once. SKILL.md still applies.

Each rule: id, title, kind (measure = a number decides; judge = a reasoned call), scope (screen or flow), what to check, when it applies, the exception, source. Ids follow the legacy rulebook (MDR-0xx became DR-0xx), so old Varmeta reports map one to one. The legacy book had no rules 004 to 024, 033, 047, 051 to 053, 061, 062, 064, 093, 094.

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
- **DR-075 Value before asking** (judge, flow). Rating asks and paywalls come after people have seen the value. Except: apps that are paid by nature. Source: apple-onboarding. Matches the rate app rule in design-hagent references/app-flows.md.

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
| apple-buttons | https://developer.apple.com/design/human-interface-guidelines/buttons |
| apple-color | https://developer.apple.com/design/human-interface-guidelines/color |
| apple-dark-mode | https://developer.apple.com/design/human-interface-guidelines/dark-mode |
| apple-feedback | https://developer.apple.com/design/human-interface-guidelines/feedback |
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
| apple-writing | https://developer.apple.com/design/human-interface-guidelines/writing |
| material-navigation | https://github.com/material-components/material-components-android/blob/master/docs/components/BottomNavigation.md |
| material-switch | https://github.com/material-components/material-components-android/blob/master/docs/components/Switch.md |
| nng-heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ |
| nng-placeholders | https://www.nngroup.com/articles/form-design-placeholders/ |
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
