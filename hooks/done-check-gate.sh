#!/bin/sh
# Stop hook for design-hagent: when this turn changed a Figma file and the DONE CHECK SCRIPT
# has not run since the last change, ask the agent once to run it before it finishes.
# Plain sh + awk so it runs without jq, python or node. Silent and exit 0 in every other case.

input=$(cat)
case $input in *'"stop_hook_active":true'*|*'"stop_hook_active": true'*) exit 0 ;; esac
transcript=$(printf '%s' "$input" | sed -n 's/.*"transcript_path": *"\([^"]*\)".*/\1/p')
[ -f "$transcript" ] || exit 0
grep -q 'design-hagent' "$transcript" || exit 0

# grep first: macOS awk is slow on long lines (tool results hold whole screenshots), and only
# these lines matter below
unchecked=$(grep -E '"type": *"user"|use_figma"|figma_execute"|design-hagent' "$transcript" | grep -v '"tool_result"' | awk '
  # the skill was loaded: Skill tool call, slash command, or its loaded body
  /"skill": *"[^"]*design-hagent/ || /command-name>\/?design-hagent/ || /skills\/design-hagent\/SKILL\.md/ { skill = 1 }
  # a new designer prompt starts a new turn (tool results, meta lines, summaries and
  # background task notifications are not prompts)
  /"type": *"user"/ && !/"tool_result"|"isMeta": *true|"isCompactSummary": *true|<task-notification>/ { wrote = 0; next }
  /"name": *"mcp__[^"]*(use_figma|figma_execute)"/ {
    line = $0
    gsub(/createOnCanvasAsync/, "", line)   # adding an agent spec block is not a design change
    # shortcut: assignments count only with a literal or figma.* value, so result objects built
    # by read scripts (r.fills = n.fills) are not edits; widen if real edits slip through
    if (line ~ /\.(appendChild|insertChild|create[A-Z][A-Za-z]*|remove|clone|group|flatten|swapComponent|resize|resizeWithoutConstraints|setProperties|resetOverrides|detachInstance|combineAsVariants|setValueForMode|addComponentProperty|editComponentProperty|deleteComponentProperty|setRange[A-Za-z]*|setBoundVariable|setBoundVariableForPaint|setTextStyleIdAsync|setFillStyleIdAsync|setStrokeStyleIdAsync|setEffectStyleIdAsync)\(/ ||
        line ~ /\.(name|x|y|characters|fills|strokes|strokeWeight|effects|cornerRadius|itemSpacing|padding[A-Za-z]*|layoutMode|layoutSizing[A-Za-z]*|primaryAxisAlignItems|counterAxisAlignItems|textAlignHorizontal|textAlignVertical|fontSize|fontName|textStyleId|fillStyleId|opacity|visible)[ ]*=[ ]*(\[|\\"|\x27|[0-9]|figma\.|true|false|\{)/)
      wrote = 1
    if (line ~ /ROOT_ID/ && line ~ /APP_PREFIX/) wrote = 0   # the done check script ran (it sets both)
  }
  END { if (skill && wrote) print "yes" }
')

[ "$unchecked" = yes ] || exit 0
cat <<'EOF'
{"decision": "block", "reason": "design-hagent: you changed the Figma file in this turn and the DONE CHECK SCRIPT has not run since the last change. Before you finish, run the done check as SKILL.md says (Done check: read the script, run it with ROOT_ID and APP_PREFIX, report non-zero counts, then a small screenshot). If the designer told you to skip it, or this turn only edited agent blocks, say that in one line and stop."}
EOF
exit 0
