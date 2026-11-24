---
name: "design-hagent-review"
description: "Read-only UX and accessibility review of mobile app screens in Hagen's design system (the base 'Design System Base' MRoPpfFSMqPoSPd7LO8kOS, the Tier 2 Template snpHcKTKy0rzuFnC9h4570, or any app file built on it, such as the first app or the trial app), or of any mobile design given as a Figma link, PDF or image. Use when the designer asks to review, audit, critique or check screens or flows for usability, accessibility, contrast, touch targets, paywall, onboarding, permissions, search or consistency, also in Vietnamese (review, đánh giá, kiểm tra UX). Gives a Vietnamese report with sourced rules, evidence and fixes. Not for token, style or binding checks: that is the done check in design-hagent."
---

# Hagen design review

**Skill version 1.0 (2026-11-24).** Rewritten from the legacy Varmeta skill mobile-design-review (rulebook 2.0.0, verified 2026-09-20).

This skill judges whether screens work for people: legibility, tap areas, navigation, states, errors, paywall honesty, permissions. It never changes the design.

## How it fits with design-hagent

- The done check (design-hagent) asks "is it built right": tokens, text styles, bindings, wraps, structure. Run it first.
- This review asks "does it work for the user". Run it after a flow section is done, or when the designer asks.
- In a file of this system, load design-hagent first and follow its read order (RULES block in full). A file rule wins over a review rule. If they clash, report it as a question, not a failure.

## Boundaries

- Read only. Never edit the file, never post Figma comments, never move findings into a Figma block unless the designer asks.
- Report in Vietnamese unless the designer asks otherwise, since the team reads it. Rule names may stay in English. A lesson for SKILL FINDINGS is written in English (design-hagent, Languages).
- Static design only. Never report on focus order, screen readers, animation, speed, keyboard, network or real error recovery: Figma can't show them.
- No accessibility score or "compliant" claim from Figma.
- Taste is not a failure. Label it "Góp ý UX" and keep it separate.

## Steps

1. **Scope.** A node link means that node only. A file link means listing pages first and asking which flows. A PDF or image means visual review only: rules that need layer data become "cần kiểm tra".
2. **Inventory.** List the screens in scope by node id (names are labels only, duplicates stay separate). Mark each as screen, overlay (dialog, sheet), part, art or system UI. Write down every item left out and why. Say the inventory is complete only after the count matches the scope.
3. **Context.** Read the file's text styles, color variables, the shared parts and the flow arrows or jump tags. Flows come from arrows, jump tags, prototype links or notes, never from where frames sit on the canvas.
4. **Units.** Find out the target platform and how Figma units map to pt (iOS) or dp (Android). Until that is known, size rules are "cần kiểm tra", not fail.
5. **Batches of five.** Per screen: a readable screenshot, then the layer data you need (sizes of tap wrappers, text size and weight, fills, hidden layers, clipping). Walk the rules in references/rules.md that apply. Keep a short note per screen so the work can resume.
6. **Flow rules.** Check the "flow" rules once per flow and point to that from each affected screen.
7. **Report.** Follow references/report.md. Give the designer the summary in chat first; write a file or doc only if asked.

## Evidence

- No evidence means "cần kiểm tra" (needs verification), never pass.
- A missing state on the canvas does not mean the rule doesn't apply.
- Tap size: measure the tappable wrapper, not the icon glyph.
- Contrast: only on flat fills you can read. Gradients, images, transparency or blends need a pixel check, otherwise "cần kiểm tra". WCAG sizes are in pt (1 pt = 1.333 px), not Figma pixels.
- Ignore hidden layers. Respect clipping that is on purpose. A chip cut at the edge may mean scrolling: check before calling it lost text.
- One screen failing to load is logged and the review goes on. If access or quota stops the run, report what was done and what is left.

## Talking to the designer

Plain language, no code talk, no em dashes. Lead with the count of issues by priority, then the top three. Say what was not checked and why.
