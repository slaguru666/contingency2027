#!/usr/bin/env bash
# Generate scenario art from tools/art_queue.tsv via the Midjourney bridge.
#
# Idempotent: an asset whose PNG already exists is skipped, so the queue can be
# re-run after a failure or after new rows are appended. Serial on purpose --
# the bridge matches a result message to the job it just sent, and two in
# flight can cross-match.
#
# Columns (tab-separated): asset_id <TAB> out_dir <TAB> prompt
set -uo pipefail
cd "$(dirname "$0")/.."
Q=tools/art_queue.tsv
LOG=promo/art.log
mkdir -p promo
ok=0; skip=0; fail=0
while IFS=$'\t' read -r id dir prompt; do
  [ -z "${id:-}" ] && continue
  case "$id" in \#*) continue ;; esac
  if compgen -G "$dir/$id"*.png > /dev/null 2>&1; then
    skip=$((skip+1)); continue
  fi
  mkdir -p "$dir"
  echo "[$(date +%H:%M:%S)] $id -> $dir" | tee -a "$LOG"
  if mj-gen "$prompt" --out "$dir" --name "$id" >>"$LOG" 2>&1; then
    ok=$((ok+1)); echo "  ok $id" | tee -a "$LOG"
  else
    fail=$((fail+1)); echo "  FAILED $id -- see $LOG" | tee -a "$LOG"
  fi
done < "$Q"
echo "ALL DONE: $ok generated, $skip already present, $fail failed" | tee -a "$LOG"
