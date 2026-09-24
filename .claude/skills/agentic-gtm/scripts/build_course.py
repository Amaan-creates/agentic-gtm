#!/usr/bin/env python3
"""Render course.json into a single self-contained course.html.

  python3 build_course.py course.json [-o course.html] [--open]

The template does all the rendering in the browser; this script only checks the
data has the shape the template expects and embeds it safely.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "templates", "course.html")
BLOCK_TYPES = {"text", "cards", "fields", "table", "callout", "signals", "compare",
               "modellab", "pipeline", "code", "steps", "exercise"}
LESSON_KEYS = {"id", "nav", "kicker", "title", "idea", "blocks", "quiz"}
BANNED = ("unlock", "supercharge", "seamless", "game-changer", "game changer", "revolutionise", "revolutionize",
          "leverage", "delve", "cutting-edge", "robust")


def check(course):
    """Return a list of problems; empty means the course will render."""
    problems = []
    if not isinstance(course.get("company"), dict) or not course["company"].get("name"):
        problems.append("company.name is missing")
    lessons = course.get("lessons")
    if not isinstance(lessons, list) or not lessons:
        return problems + ["lessons[] is missing or empty"]
    ids = [s.get("id") for s in course.get("sources", [])]
    source_ids = set(ids)
    for sid in {i for i in ids if ids.count(i) > 1}:
        problems.append(f"source id {sid} is used twice in sources[]")
    blob = json.dumps(course, ensure_ascii=False)
    for group in re.findall(r"\[(s\d+(?:\s*,\s*s\d+)*)\]", blob):
        for sid in re.split(r"\s*,\s*", group):
            if sid not in source_ids:
                problems.append(f"source [{sid}] is cited but not in sources[]")
    glossary = course.get("glossary") or {}
    for term in sorted(set(re.findall(r"\{\{([^}]+)\}\}", blob))):
        if term not in glossary:
            problems.append(f"{{{{{term}}}}} is used but not defined in glossary")
    for i, lesson in enumerate(lessons):
        where = f"lessons[{i}] ({lesson.get('id', '?')})"
        if not lesson.get("id") or not lesson.get("title"):
            problems.append(f"{where}: id and title are required")
        for j, block in enumerate(lesson.get("blocks", [])):
            if block.get("type") not in BLOCK_TYPES:
                problems.append(f"{where}.blocks[{j}]: unknown type {block.get('type')!r}")
        for k, q in enumerate(lesson.get("quiz", [])):
            opts = q.get("options") or []
            if not isinstance(q.get("answer"), int) or not 0 <= q["answer"] < len(opts):
                problems.append(f"{where}.quiz[{k}]: answer must index into options")
    return sorted(set(problems))


def styled_text(course):
    """Yield (where, text) for every prose field the style rules apply to.
    Skips compare.left (the generic message is meant to read badly) and modellab outputs (measured data)."""
    for k in ("title", "lede"):
        if course.get(k): yield k, course[k]
    for lesson in course.get("lessons", []):
        lid = lesson.get("id")
        for k in ("title", "idea"):
            if lesson.get(k): yield lid, lesson[k]
        for b in lesson.get("blocks", []):
            t = b.get("type")
            if t == "compare":
                yield lid, json.dumps(b.get("right", {}), ensure_ascii=False)
            elif t == "modellab":
                yield lid, (b.get("task") or "") + " " + (b.get("takeaway") or "") + " " + " ".join(str(r.get("verdict") or "") for r in b.get("runs", []))
            elif t != "code":
                yield lid, json.dumps(b, ensure_ascii=False)
        for q in lesson.get("quiz", []):
            yield lid, json.dumps(q, ensure_ascii=False)


def warnings(course):
    """Style checks that don't block the build."""
    out = []
    blob = json.dumps(course, ensure_ascii=False)
    for term in (course.get("glossary") or {}):
        if "{{" + term + "}}" not in blob:
            out.append(f"glossary term {term!r} is never used")
    for lesson in course.get("lessons", []):
        extra = set(lesson) - LESSON_KEYS
        if extra:
            out.append(f"{lesson.get('id')}: unknown lesson keys {sorted(extra)} are ignored (exercise is a block, not a lesson field)")
        for block in lesson.get("blocks", []):
            if block.get("type") in ("text", "callout"):
                for para in str(block.get("body", "")).split("\n\n"):
                    n = len(re.findall(r"[.!?](?:\s|$)", para))
                    if n > 3:
                        out.append(f"{lesson.get('id')}: a {block['type']} paragraph has {n} sentences (aim for 3 or fewer)")
            if block.get("type") == "modellab":
                for r in block.get("runs", []):
                    if len(str(r.get("verdict") or "").split()) > 15:
                        out.append(f"{lesson.get('id')}: a model lab verdict is over 15 words; move detail to the takeaway")
    for where, text in styled_text(course):
        if "\u2014" in text:
            out.append(f"{where}: contains an em dash")
        low = text.lower()
        for w in BANNED:
            if w in low:
                out.append(f"{where}: uses {w!r}")
    return sorted(set(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("course_json")
    ap.add_argument("-o", "--out", default=None)
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()

    course = json.load(open(args.course_json))
    problems = check(course)
    if problems:
        print("course.json has problems:\n  - " + "\n  - ".join(problems), file=sys.stderr)
        sys.exit(1)

    # "</" inside a <script> block would end it early; escape it so any text is safe to embed.
    payload = json.dumps(course, ensure_ascii=False).replace("</", "<\\/")
    html = open(TEMPLATE).read().replace("/*COURSE_DATA*/", payload, 1)
    for w in warnings(course):
        print("note:", w, file=sys.stderr)
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(args.course_json)), "course.html")
    open(out, "w").write(html)
    print(f"wrote {out} ({len(course['lessons'])} lessons, {len(course.get('sources', []))} sources)")
    if args.open:
        import shutil
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        if shutil.which(opener) and (sys.platform == "darwin" or os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
            subprocess.run([opener, out], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print(f"open {out} in a browser")


if __name__ == "__main__":
    main()
