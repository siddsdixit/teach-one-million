#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent

errors: list[str] = []


def rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def check_day_files() -> None:
    expected = {
        "learn.md",
        "build.md",
        "loom.md",
        "resources.md",
    }
    for day_dir in sorted(ROOT.glob("week-*/*")):
        if not day_dir.is_dir() or not day_dir.name.startswith("day-"):
            continue
        files = {p.name for p in day_dir.glob("*.md")}
        ai_files = [p.name for p in day_dir.glob("ai-instructions-day-*.md")]
        missing = expected - files
        if missing:
            errors.append(f"{rel(day_dir)} missing files: {sorted(missing)}")
        if len(ai_files) != 1:
            errors.append(f"{rel(day_dir)} expected exactly one ai-instructions file, found {ai_files}")


def check_links() -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    href_re = re.compile(r'href="([^"]+)"')
    for file in ROOT.rglob("*.md"):
        text = file.read_text()
        for raw in link_re.findall(text) + href_re.findall(text):
            if re.match(r"^(https?:|mailto:|#)", raw):
                continue
            target = raw.split("#", 1)[0].replace("%20", " ")
            if not (file.parent / target).resolve().exists():
                errors.append(f"{rel(file)} has missing link: {raw}")


def check_forbidden_public_text() -> None:
    forbidden = [
        "Sprint 2",
        "Sprint 3",
        "Sprint 4",
        "Embedded Loom",
        "placeholder for Sprint",
        "link added Sprint",
        "cost-transparency.md",
        "tools/README.md",
        "github.com/siddsdixit/onemillion-builder",
        "codespaces-fallback-last-resort",
    ]
    for file in ROOT.rglob("*.md"):
        text = file.read_text()
        for term in forbidden:
            if term in text:
                errors.append(f"{rel(file)} contains forbidden text: {term}")


def check_learning_frames() -> None:
    for file in ROOT.glob("week-*/*/learn.md"):
        text = file.read_text()
        for heading in [
            "## Learning Frame",
            "**Mental model:**",
            "**What can go wrong:**",
            "**What to ignore today:**",
        ]:
            if heading not in text:
                errors.append(f"{rel(file)} missing learning frame item: {heading}")


def check_stuck_prompts() -> None:
    for file in ROOT.glob("week-*/*/build.md"):
        text = file.read_text()
        if "## If You Are Stuck" not in text:
            errors.append(f"{rel(file)} missing stuck-rescue prompt")


def check_progress_tracker() -> None:
    for file in ROOT.glob("week-*/*/build.md"):
        text = file.read_text()
        if "## Update Your Progress Tracker" not in text:
            errors.append(f"{rel(file)} missing progress tracker update")


def check_day_navigation() -> None:
    required = [
        "Course Home</a>",
        "Week Overview</a>",
        "./learn.md",
        "./build.md",
        "./resources.md",
        "./loom.md",
    ]
    for file in ROOT.glob("week-*/*/*.md"):
        if file.name.startswith("ai-instructions-day-"):
            continue
        text = file.read_text()
        for item in required:
            if item not in text:
                errors.append(f"{rel(file)} missing day navigation item: {item}")


def main() -> int:
    check_day_files()
    check_links()
    check_forbidden_public_text()
    check_learning_frames()
    check_stuck_prompts()
    check_progress_tracker()
    check_day_navigation()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Course quality check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
