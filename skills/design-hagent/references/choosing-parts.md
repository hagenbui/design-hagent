# Choosing a part

Part of the design-hagent skill. Read when you pick a part for a screen or decide a button group. SKILL.md still applies.

Visual first (base 7.13): before you add a text, pick the part or state that shows it. Progress: a progress bar or step dots, not "3 of 5 completed". Start or open: a play button, chevron or tappable card, not "Tap to start". Whose content: an avatar or picker, not a subtitle. Reorder or delete: a handle or swipe action, not a tip. Status: a badge, check or tint, not a sentence.

Pick a part by the job it does, never by which one looks closest. If the job isn't below or in the file's rules, ask. If the base RULES block has a table for choosing a part, it wins over this list. Otherwise use this:
- Navigate into a screen, a settings item, a saved record, a long single-choice list in a form: list row.
- Do something: button. Secondary action: ghost or secondary button, never a list row.
- Toggle: switch or checkbox. Never a row with nothing on the right.
- Status: a checklist item, not tappable.
- Two big choices: picture cards. Short picks and survey answers: option cards. Suggestions: chips.
- Share on a result: an icon button in the header.
- Choose a language: base Language Option cards (flag, native name, check when selected), five or more stacked with group-gap. On first run: a Continue button in the bottom bar. In Settings: the choice applies right away, no Save button. The Settings row is a list row with the current language as trailing text. Never write a language name in another language.

Button groups (a button rule in the base or app RULES block wins over this list):
- One action on an empty or error screen: Primary, hugging its label.
- Two or more actions: stacked, the main action first. Full width on most screens. On empty states, follow the base empty state rule (6.5) for their width.
- Destructive is the main action: Destructive + Secondary.
- Primary plus a destructive choice plus cancel: Primary, Destructive Secondary, Ghost. One red button per group.
- A row that opens a delete confirm stays a row. The red appears on the confirm button.
