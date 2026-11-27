# Report format

Part of the design review (references/review.md). Read when you write the review result. SKILL.md and review.md still apply.

Write the report in the language the designer picked (review.md, step 1), and use the labels of that language below, English or Vietnamese.

## Each issue

- Screen / Màn hình: name and node link (one issue lists every screen it affects, group issues on a shared part)
- Rule / Quy tắc: rule id and title, with its source link from references/review-rules.md
- Evidence / Bằng chứng: what you saw or measured (values, units, screenshot area)
- Impact / Ảnh hưởng: what goes wrong for the user
- Severity / Mức độ: P1 blocks a task, hides cost or fails a measurable minimum; P2 slows or confuses; P3 polish
- Confidence / Độ tin cậy: high, medium, low / cao, trung bình, thấp
- Fix / Cách sửa: one concrete fix, named in the system's terms (which part, token or text style). Never a raw number when a token exists.

## Statuses per rule

pass / đạt, fail / không đạt, needs verification / cần kiểm tra (say what is missing), not applicable / không áp dụng (say why). Every rule in scope ends with one status. Never mark a rule you didn't look at.

## Order of the report

1. Summary / Tóm tắt: scope, platform, unit mapping, counts by P1 to P3, top three issues.
2. Issues / Vấn đề, grouped by priority.
3. UX suggestions / Góp ý UX (taste, not failures).
4. Not checked / Chưa kiểm tra được: rules left as needs verification and what would settle them.
5. Questions / Câu hỏi: clashes between a review rule and a file rule, for the designer.

## Mapping to the system's findings

When the designer asks to log results in Figma:
- A gap in a base part (for example Button md under 48 dp) goes to the base AUDIT or ROADMAP as D (defect) or a new roadmap item, with the rule id.
- A pattern worth a rule goes in as P, a clash or open point as Q.
- A gap in one app goes in that file's FINDINGS as a T item.
- A lesson about how agents review goes in SKILL FINDINGS (see references/skill-findings.md).
