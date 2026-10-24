# Recovery of the July 2024 NumPy Assignment

The original `HW4/Vocabulary.py` file had been overwritten by a later plotting experiment. The surviving `HW4/__pycache__/Vocabulary.cpython-312.pyc` still contained the earlier text-processing implementation.

Its cache header records:

- Original source timestamp: **17 July 2024, 21:27:12** (local file time).
- Original source size: **7,392 bytes**.
- Cache SHA-256: `dab6000d7bff0dd8cc0fa02ff9b42186b692a6edd18fbedfa8f3e22b762dba7f`.
- Python version: **CPython 3.12**.

Git's local index held empty versions of the overwritten Python files, and the local IDE history did not yield the missing source. A separate copy of the cache was preserved before reconstruction. No original source or cache file was overwritten during recovery.

## What was recovered

The readable `Vocabulary.py` module was reconstructed from the bytecode, preserving the original class names, method names, variable names, constants, algorithms, and behavior.

Using CPython 3.12.2, the recovered source was compiled and compared recursively with the original cache. **All 30 code objects matched**, including the module, four class bodies, their methods, three public functions, and the nested similarity callback. The comparison checks executable bytecode, non-code constants, names, locals, argument counts, closure variables, flags, stack sizes, and exception tables.

Source filenames, source line numbers, and line-position tables are intentionally excluded: reconstructing readable source changes those locations. Original comments and whitespace are absent from Python bytecode and cannot be recovered. This is verified source reconstruction, not a byte-for-byte copy of the lost `.py` text.

The full list of matching code objects is recorded in `recovery_manifest.json`. Newly added demo code, tests, documentation, and this verification utility are distinct from the recovered implementation.

## Reproduce the bytecode comparison locally

If the original cache is available, run with CPython 3.12:

```text
python numpy_text_processing/verify_recovery.py --cache "PATH/TO/Vocabulary.cpython-312.pyc"
```

The utility checks the cache hash and compares code objects without executing the supplied cache. The cache itself is not committed: the repository contains portable readable source, not interpreter-specific cached binaries or their embedded local paths.

The runtime regression tests additionally check normalization, word/index lookup, one-hot and cumulative encodings, round trips, bag-of-words frequencies, unknown words, cosine similarity, and closest-pair selection. These tests preserve historical behavior and do not silently repair unrelated algorithmic edge cases.
