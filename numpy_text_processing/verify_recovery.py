"""Compare the recovered source to the original cache without executing it."""

import argparse
import hashlib
import importlib.util
import json
import marshal
import sys
import types
from pathlib import Path


def code_objects(code):
    objects = {code.co_qualname: code}
    for value in code.co_consts:
        if isinstance(value, types.CodeType):
            objects.update(code_objects(value))
    return objects


def signature(code):
    fields = (
        "co_code", "co_names", "co_varnames", "co_freevars", "co_cellvars",
        "co_argcount", "co_posonlyargcount", "co_kwonlyargcount", "co_flags",
        "co_stacksize", "co_exceptiontable",
    )
    constants = tuple(value for value in code.co_consts if not isinstance(value, types.CodeType))
    return tuple(getattr(code, field) for field in fields) + (constants,)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True, help="Original CPython 3.12 cache")
    args = parser.parse_args()
    if sys.version_info[:2] != (3, 12):
        parser.error("Use CPython 3.12 for the bytecode comparison.")
    directory = Path(__file__).resolve().parent
    manifest = json.loads((directory / "recovery_manifest.json").read_text(encoding="utf-8"))
    raw = args.cache.read_bytes()
    if hashlib.sha256(raw).hexdigest() != manifest["cache_sha256"]:
        parser.error("The supplied cache does not match the recorded original SHA-256.")
    if raw[:4] != importlib.util.MAGIC_NUMBER:
        parser.error("The original cache is incompatible with this Python interpreter.")
    original = code_objects(marshal.loads(raw[16:]))
    recovered = code_objects(compile((directory / "Vocabulary.py").read_text(encoding="utf-8"), "<recovered>", "exec"))
    differences = [
        name for name in original.keys() | recovered.keys()
        if name not in original or name not in recovered
        or signature(original[name]) != signature(recovered[name])
    ]
    if differences:
        raise SystemExit("Different code objects: " + ", ".join(sorted(differences)))
    print(f"All {len(original)} code objects match the original cache.")


if __name__ == "__main__":
    main()
