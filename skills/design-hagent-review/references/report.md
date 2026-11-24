# Report format

Part of the design-hagent-review skill. Read when you write the review result. SKILL.md still applies.

## Each issue

- Màn hình: name and node link (one issue lists every screen it affects, group issues on a shared part)
- Quy tắc: rule id and title, with its source link from references/rules.md
- Bằng chứng: what you saw or measured (values, units, screenshot area)
- Ảnh hưởng: what goes wrong for the user
- Mức độ: P1 blocks a task, hides cost or fails a measurable minimum; P2 slows or confuses; P3 polish
- Độ tin cậy: cao, trung bình, thấp
- Cách sửa: one concrete fix, named in the system's terms (which part, token or text style). Never a raw number when a token exists.

## Statuses per rule

đạt (pass), không đạt (fail), cần kiểm tra (needs verification, say what is missing), không áp dụng (not applicable, say why). Every rule in scope ends with one status. Never mark a rule you didn't look at.

## Order of the report

1. Tóm tắt: scope, platform, unit mapping, counts by P1 to P3, top three issues.
2. Vấn đề, grouped by priority.
3. Góp ý UX (taste, not failures).
4. Chưa kiểm tra được: rules left as cần kiểm tra and what would settle them.
5. Câu hỏi: clashes between a review rule and a file rule, for the designer.

## Mapping to the system's findings

When the designer asks to log results in Figma:
- A gap in a base part (for example Button md under 48 dp) goes to the base AUDIT or ROADMAP as D (defect) or a new roadmap item, with the rule id.
- A pattern worth a rule goes in as P, a clash or open point as Q.
- A gap in one app goes in that file's FINDINGS as a T item.
- A lesson about how agents review goes in SKILL FINDINGS (see design-hagent references/skill-findings.md).
