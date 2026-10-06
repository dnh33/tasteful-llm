#!/bin/sh
# Copy the tasteful-llm skill folders into a Codex skills directory.
# Usage: scripts/install-codex.sh [target-dir]   (default: $HOME/.agents/skills)
# Safe to re-run: each skill folder is replaced with the current copy.
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(dirname "$script_dir")
src="$repo_root/skills"
dest=${1:-${HOME:?HOME is not set}/.agents/skills}

if [ ! -d "$src" ]; then
  echo "error: no skills directory at $src" >&2
  exit 1
fi

mkdir -p "$dest"
count=0
for dir in "$src"/*/; do
  [ -f "${dir}SKILL.md" ] || continue
  name=$(basename "$dir")
  if [ -e "$dest/$name" ]; then
    rm -rf "${dest:?}/$name"
    action="updated"
  else
    action="installed"
  fi
  cp -R "${dir%/}" "$dest/$name"
  echo "$action $name -> $dest/$name"
  count=$((count + 1))
done

echo "done: $count skill folder(s) in $dest"
echo "Next: add a line to AGENTS.md telling Codex when to use them (see README)."
