#!/bin/sh
# Tests for done-check-gate.sh. Run: sh hooks/test-done-check-gate.sh
HOOK="$(dirname "$0")/done-check-gate.sh"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
fail=0

skill='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"Skill","input":{"skill":"design-hagent:design-hagent"}}]}}'
write='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"const f = figma.createFrame(); f.name = \"Result\"; page.appendChild(f);"}}]}}'
read='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"return page.children.filter(n => n.name === \"Result\").length"}}]}}'
done='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"const ROOT_ID = \"1:2\"; const APP_PREFIX = \"Kid/\"; /* script */"}}]}}'
log='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"await figma.spec.editContent({specNodeId: b.id, find: \"## Work log\", replace: \"## Work log\\n- added Result\"})"}}]}}'
user='{"type":"user","message":{"role":"user","content":"looks good, thanks"}}'
result='{"type":"user","message":{"role":"user","content":[{"type":"tool_result","tool_use_id":"t1","content":"ok"}]}}'
readobj='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"const r = {}; r.name = n.name; r.fills = n.fills; return r"}}]}}'
quoted='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"t.characters = '"'"'Hello'"'"'"}}]}}'
meta='{"type":"user","isMeta":true,"message":{"role":"user","content":"[Image: original 2260x1980]"}}'
summary='{"type":"user","isCompactSummary":true,"message":{"role":"user","content":"This session is being continued from a previous conversation"}}'
notify='{"type":"user","message":{"role":"user","content":"<task-notification> <status>completed</status> </task-notification>"}}'
token='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"v.setValueForMode(modeId, {r:1,g:0,b:0,a:1})"}}]}}'
rename='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"n.name = \"Header\""}}]}}'
exec='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__figma-console__figma_execute","input":{"code":"page.appendChild(f)"}}]}}'
slash='{"type":"user","message":{"role":"user","content":"<command-name>/design-hagent:design-hagent</command-name>"}}'
prefixonly='{"type":"assistant","message":{"content":[{"type":"tool_use","name":"mcp__abc__use_figma","input":{"code":"const APP_PREFIX = \"Kid/\"; c.name = APP_PREFIX + \"Button\""}}]}}'

# case <name> <expect block|pass> <stop_hook_active> <lines...>
case_() {
  name=$1 expect=$2 active=$3; shift 3
  f="$T/$name.jsonl"; : > "$f"
  for l in "$@"; do printf '%s\n' "$l" >> "$f"; done
  out=$(printf '{"session_id":"s","transcript_path":"%s","hook_event_name":"Stop","stop_hook_active":%s}' "$f" "$active" | sh "$HOOK")
  code=$?
  if [ "$expect" = block ]; then
    echo "$out" | grep -q '"decision": *"block"' && [ $code -eq 0 ] && { echo "ok   $name"; return; }
  else
    [ -z "$out" ] && [ $code -eq 0 ] && { echo "ok   $name"; return; }
  fi
  echo "FAIL $name (exit $code): $out"; fail=1
}

case_ edit_without_check    block false "$skill" "$write"
case_ edit_then_check       pass  false "$skill" "$write" "$done"
case_ check_then_log_only   pass  false "$skill" "$write" "$done" "$log"
case_ check_then_more_edits block false "$skill" "$write" "$done" "$write"
case_ read_only_session     pass  false "$skill" "$read" "$read"
case_ skill_not_loaded      pass  false "$write"
case_ new_turn_no_edits      pass  false "$skill" "$write" "$user" "$read"
case_ new_turn_with_edits    block false "$skill" "$done" "$user" "$write"
case_ tool_result_not_a_turn block false "$skill" "$write" "$result"
case_ spec_block_only        pass  false "$skill" "$log"
case_ result_object_assign   pass  false "$skill" "$readobj"
case_ meta_line_not_a_turn   block false "$skill" "$write" "$meta"
case_ summary_not_a_turn     block false "$skill" "$write" "$summary"
case_ notification_not_turn  block false "$skill" "$write" "$notify"
case_ token_value_edit       block false "$skill" "$token"
case_ rename_only_edit       block false "$skill" "$rename"
case_ figma_execute_tool     block false "$skill" "$exec"
case_ slash_command_load     block false "$slash" "$write"
case_ prefix_alone_not_check block false "$skill" "$write" "$prefixonly"
case_ single_quoted_text   block false "$skill" "$quoted"
case_ already_reminded    pass  true  "$skill" "$write"
case_ missing_transcript    pass  false
rm -f "$T/missing_transcript.jsonl"
out=$(printf '{"transcript_path":"%s/nope.jsonl","stop_hook_active":false}' "$T" | sh "$HOOK"); [ -z "$out" ] && echo "ok   no_file" || { echo "FAIL no_file"; fail=1; }

# speed: a 60 MB transcript of long non-Figma lines must finish well inside the 10 s hook timeout
pad=$(head -c 200000 /dev/zero | tr '\0' 'a')
{ printf '%s\n' "$skill"; i=0; while [ $i -lt 300 ]; do printf '{"type":"assistant","message":{"content":[{"type":"text","text":"%s"}]}}\n' "$pad"; i=$((i+1)); done; printf '%s\n' "$write"; } > "$T/big.jsonl"
start=$(date +%s)
out=$(printf '{"transcript_path":"%s","stop_hook_active":false}' "$T/big.jsonl" | sh "$HOOK")
secs=$(( $(date +%s) - start ))
if echo "$out" | grep -q block && [ $secs -le 2 ]; then echo "ok   big_transcript (${secs}s)"; else echo "FAIL big_transcript (${secs}s)"; fail=1; fi

exit $fail
