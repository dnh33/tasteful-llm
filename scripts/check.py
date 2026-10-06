#!/usr/bin/env python3
"""Consistency checks for tasteful-llm. Standard library only. Exit 1 on any failure."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_prompt as bp  # noqa: E402

ROOT = bp.ROOT
SKILLS = ROOT / "skills"
ALLOWED_KEYS = {"name", "description", "license", "metadata", "allowed-tools", "compatibility"}

failures: list = []
results: list = []


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def run_check(label, fn):
    errs = fn()
    results.append((label, errs))
    failures.extend("[%s] %s" % (label, e) for e in errs)


def md_files():
    return sorted(SKILLS.rglob("*.md"))


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


# (a) catalog index vs terminal files
def check_codes():
    errs = []
    idx = set(bp.catalog_index())
    term = set(bp.terminal_codes())
    if not idx:
        errs.append("no pattern codes found in anti-pattern-catalog.md")
    if not term:
        errs.append("no pattern headings found under skills/tasteful-output/patterns/")
    for c in sorted(idx - term, key=bp.code_sort_key):
        errs.append("%s is in the catalog index but has no heading in a terminal pattern file" % c)
    for c in sorted(term - idx, key=bp.code_sort_key):
        errs.append("%s has a heading in %s but is missing from the catalog index"
                    % (c, rel(bp.terminal_codes()[c][1])))
    seen = {}
    for e in bp.terminal_entries():
        if e["code"] in seen:
            errs.append("%s is defined twice: %s:%d and %s" % (e["code"], rel(e["file"]), e["line"], seen[e["code"]]))
        else:
            seen[e["code"]] = "%s:%d" % (rel(e["file"]), e["line"])
    cats = {re.match(r"[A-Z]+", c).group(0) for c in idx}
    if len(cats) != 6:
        errs.append("catalog index has %d categories (%s), expected 6" % (len(cats), ", ".join(sorted(cats))))
    for c in sorted(set(bp.router_index()) - idx, key=bp.code_sort_key):
        errs.append("%s is listed in a category router but not in the catalog index" % c)
    return errs


# (b) stated counts
COUNT_RE = re.compile(r"\b(\d+)[- ]patterns?\b", re.I)


def changelog_top(text: str) -> str:
    heads = [m.start() for m in re.finditer(r"^## ", text, re.M)]
    if not heads:
        return text
    end = heads[1] if len(heads) > 1 else len(text)
    return text[heads[0]:end]


def check_counts():
    errs = []
    actual = len(bp.terminal_codes())
    targets = [
        ROOT / "README.md",
        ROOT / ".claude-plugin" / "plugin.json",
        SKILLS / "tasteful-output" / "anti-pattern-catalog.md",
        ROOT / "CHANGELOG.md",
        ROOT / "CONTRIBUTING.md",
    ]
    for path in targets:
        if not path.exists():
            errs.append("%s does not exist" % rel(path))
            continue
        text = path.read_text(encoding="utf-8")
        if path.name == "CHANGELOG.md":
            text = changelog_top(text)
        found = 0
        for line in text.splitlines():
            if path.name == "CHANGELOG.md" and re.search(r"→|->|\bfrom\b|\bwas\b|previous", line, re.I):
                continue
            for m in COUNT_RE.finditer(line):
                found += 1
                if int(m.group(1)) != actual:
                    errs.append("%s says \"%s\" but the catalog defines %d patterns"
                                % (rel(path), m.group(0), actual))
        if found and not re.search(r"\bsix categories\b", text, re.I):
            errs.append("%s states a pattern count but not \"six categories\"" % rel(path))
        if found == 0 and path.name in ("README.md", "plugin.json"):
            errs.append("%s states no pattern count" % rel(path))
    return errs


# (b2) metadata line under every pattern heading
META_RE = re.compile(r"^Status: (consistent|rising|fading|unchecked) · Seen in: .+ · Verified: .+$")


def check_metadata():
    errs = []
    for e in bp.terminal_entries():
        if not META_RE.match(e["meta"]):
            errs.append("%s:%d %s: missing or malformed metadata line (got %r)"
                        % (rel(e["file"]), e["line"], e["code"], e["meta"][:60]))
    return errs


# (c) broken relative links
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links():
    errs = []
    for f in md_files():
        text = strip_code(f.read_text(encoding="utf-8"))
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            if re.match(r"[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith(("#", "<")):
                continue
            path = target.split("#", 1)[0]
            if not path:
                continue
            if not (f.parent / path).resolve().exists():
                errs.append("%s: broken link (%s)" % (rel(f), target))
    return errs


# (d) @file references
AT_RE = re.compile(r"(?<![\w/.@-])@([\w./-]+\.md)\b")


def check_at_refs():
    errs = []
    for f in md_files():
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for m in AT_RE.finditer(line):
                errs.append("%s:%d: '@%s' file reference; use a relative markdown link"
                            % (rel(f), n, m.group(1)))
    return errs


# (e) frontmatter keys, (f) length
def check_frontmatter():
    errs = []
    for f in sorted(SKILLS.glob("*/SKILL.md")):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
        if not m:
            errs.append("%s: missing frontmatter" % rel(f))
            continue
        keys = set(re.findall(r"^([A-Za-z_][\w-]*)\s*:", m.group(1), re.M))
        for k in sorted(keys - ALLOWED_KEYS):
            errs.append("%s: frontmatter key '%s' is not in %s" % (rel(f), k, sorted(ALLOWED_KEYS)))
        for k in ("name", "description"):
            if k not in keys:
                errs.append("%s: frontmatter is missing '%s'" % (rel(f), k))
    return errs


def check_length():
    errs = []
    for f in sorted(SKILLS.glob("*/SKILL.md")):
        n = len(f.read_text(encoding="utf-8").splitlines())
        if n > 500:
            errs.append("%s has %d lines (limit 500)" % (rel(f), n))
    return errs


# (g) dist freshness
def check_dist():
    proc = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_prompt.py"), "--check"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return [l for l in (proc.stdout + proc.stderr).splitlines() if l.strip()]
    return []


# (h0) plugin manifests
def check_plugin_manifests():
    errs = []
    root_p = ROOT / "plugin.json"
    claude_p = ROOT / ".claude-plugin" / "plugin.json"
    try:
        rp = json.loads(root_p.read_text(encoding="utf-8"))
        cp = json.loads(claude_p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return ["cannot read plugin manifests: %s" % e]
    for k in ("name", "version", "description"):
        if not rp.get(k):
            errs.append("plugin.json is missing '%s'" % k)
        elif rp.get(k) != cp.get(k):
            errs.append("plugin.json %s %r differs from .claude-plugin/plugin.json %r" % (k, rp.get(k), cp.get(k)))
    mp = ROOT / ".agents" / "plugins" / "marketplace.json"
    try:
        for pl in json.loads(mp.read_text(encoding="utf-8")).get("plugins", []):
            path = (pl.get("source") or {}).get("path", "")
            if not path.startswith("./") or not (ROOT / path / "plugin.json").exists():
                errs.append("codex marketplace path %r does not contain plugin.json" % path)
    except (OSError, ValueError):
        pass
    return errs


# (h) marketplace JSON
def check_json():
    errs = check_plugin_manifests()
    files = [ROOT / ".claude-plugin" / "marketplace.json",
             ROOT / ".agents" / "plugins" / "marketplace.json",
             ROOT / ".claude-plugin" / "plugin.json"]
    for p in files:
        if not p.exists():
            errs.append("%s does not exist" % rel(p))
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except ValueError as e:
            errs.append("%s is not valid JSON: %s" % (rel(p), e))
            continue
        if p.name == "marketplace.json":
            if not isinstance(data.get("plugins"), list) or not data.get("name"):
                errs.append("%s needs 'name' and a 'plugins' array" % rel(p))
    return errs


# (i) flat prompts must not link to files
def check_flat_links():
    errs = []
    for f in sorted((ROOT / "dist").glob("system-prompt-*.md")):
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if ".md)" in line:
                errs.append("%s:%d contains a .md) link" % (rel(f), n))
    return errs


def main() -> int:
    run_check("pattern codes", check_codes)
    run_check("stated counts", check_counts)
    run_check("pattern metadata", check_metadata)
    run_check("relative links", check_links)
    run_check("@file refs", check_at_refs)
    run_check("frontmatter keys", check_frontmatter)
    run_check("SKILL.md length", check_length)
    run_check("dist up to date", check_dist)
    run_check("marketplace JSON", check_json)
    run_check("flat prompt links", check_flat_links)
    print("tasteful-llm check: %d patterns defined, %d in catalog index"
          % (len(bp.terminal_codes()), len(bp.catalog_index())))
    for label, errs in results:
        print("  %-18s %s" % (label, "ok" if not errs else "FAIL (%d)" % len(errs)))
    if failures:
        print("\nFailures:")
        for f in failures:
            print("  - " + f)
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
