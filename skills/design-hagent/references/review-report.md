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

## HTML report (the default output)

Every review ends in one HTML page: each screen's screenshot with numbered dots on the issues, the issues listed beside it with the same numbers, and filters for New, Still open and Solved. A script builds it from a small JSON file, so never write or read the HTML yourself.

1. **Folder.** `~/Design Reviews/<app short name>/`, one folder per app, never inside a repo (screens are confidential). Earlier reports in that folder are what New and Solved are measured against, so always reuse it.
2. **Screenshots.** For each screen in scope: `get_screenshot` with `contentsOnly: true` and `maxDimension: 812`, then `curl -fsSL -o "<folder>/img/<node id with : as ->.png" "<image_url>"`. Never ask for base64.
3. **Boxes.** For each issue, the node's bounds relative to its screen in Figma units: `[x, y, w, h]`, where x and y are the node's absolute position minus the screen's. Read them with the layer data in step 5 of review.md. Use the node on the screen itself (an instance, not an id nested inside one), so the same issue keeps its key next time. A flow issue gets the box on the screen where it shows.
4. **JSON.** Write `<folder>/review.json`:

```
{"app": "Short name", "date": "YYYY-MM-DD", "language": "en or vi", "scope": "what was reviewed",
 "screens": [{"id": "1:2", "name": "1.1 Splash", "size": [375, 812]}],
 "issues": [{"rule": "DR-025", "title": "Touch target size", "severity": "P1", "screen": "1:2", "node": "1:5",
   "box": [236, 160, 24, 28], "evidence": "...", "impact": "...", "fix": "...", "confidence": "high"}]}
```

   `severity` is exactly P1, P2, P3 or UX (UX for suggestions). `size` is the screen frame in Figma units; if content spills past the frame edge, the screenshot is larger and dots drift, so note it. A file rule is named like "App 2.7". Optional: `title`, screen `name`, screen `image` (a PNG path when it isn't img/<id>.png), and `box` (without it the issue shows in the list only). The date is YYYY-MM-DD. Bad input stops the script with a message: fix the JSON and run it again.
5. **Build.** `python3 -I <this skill's folder>/scripts/review_html.py "<folder>/review.json"`. It prints the path of `review-<date>.html`, with the images inside. Each issue is marked New or Still open (same rule and node as last time); issues from the last report on screens in this scope that are gone are marked Solved; issues on screens outside this scope are carried forward as not rechecked, never as solved, and are compared again the next time those screens are in scope. A second run on the same day replaces that day's page and still compares with the earlier one.
6. **Hand over.** Give the designer the path and the chat summary (counts, top three, what is new and solved).

## Mapping to the system's findings

When the designer asks to log results in Figma:
- A gap in a base part (for example Button md under 48 dp) goes to the base AUDIT or ROADMAP as D (defect) or a new roadmap item, with the rule id.
- A pattern worth a rule goes in as P, a clash or open point as Q.
- A gap in one app goes in that file's FINDINGS as a T item.
- A lesson about how agents review goes in SKILL FINDINGS (see references/skill-findings.md).
