# Figma gotchas

Part of the design-hagent skill. Read before your first use_figma call in a session. SKILL.md still applies.

- Gotchas for building and extending parts are in references/wraps.md, and adding a spec block is in references/new-app.md.
- `figma.getNodeByIdAsync(id)` reaches nodes on other pages without switching the current page, so one call can read or set many parts.
- `figma.spec.setContent` on a block that has a table can fail with "ambiguous table column correspondence". Write the block with a placeholder line, then put the table in with `editContent`.
- Set `figma.skipInvisibleInstanceChildren = false` before touching hidden instance children.
- The base screen size collection is "Device" (renamed from "_Device" on 2026-11-17) and is published, so tier 2 screens can bind screen-width and screen-height to it. Older notes that say "_Device" mean the same collection.
- The DONE CHECK SCRIPT is still a text node in Inter Regular: load the font before editing it, edit by exact string replace, and re-read afterward.
- When swapping an instance to another variant or part, call `resetOverrides()` first, then set only what you need. Old fills and hidden icons survive a swap otherwise. A reset puts every property back to its default, not only the wrong one: before it, save the label, icon booleans, visibility, layout sizing (FILL) and links; after it, restore each one, find the nodes again, and look at a screenshot before saying it is done (SF-2).
- A paint bound to a color variable still stores a raw color, the fallback. Never write black or a placeholder there. Set it to the variable's value for that node: `const { r, g, b } = variable.resolveForConsumer(node).value`, then bind. A wrong fallback looks right in screenshots and only shows when the file is opened or the binding breaks.
- Never make a tint with paint or layer opacity on a variable-bound paint: it doesn't reach instances. Bind a real token or ask for one.
- A screen with FILL content inside a hugging root collapses. Give the screen root the device minHeight and let Content hug.
- Not available in this context: `figma.loadAllPagesAsync`, `figma.createConnector`, connector bend points. `findAll` doesn't exist on text nodes: check `'findAll' in node` first.
- Keep reads of big files small (compact JSON, small screenshots). Large responses break.
- One use_figma call returns at most five `node.screenshot()` images; a sixth is dropped without an error. Take screenshots five per call (review.md, Batches of five).
