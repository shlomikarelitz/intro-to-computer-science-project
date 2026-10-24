**#intro to computer science project**

**Introduction to Computer Science projects - Ben-Gurion University, Semester B, 2024.**

Two Python coursework projects: a Pokemon battle simulator built with object-oriented programming, and a NumPy library that represents text as matrices and compares sentences.

| Project | Focus | Run |
| --- | --- | --- |
| [Pokemon battles](pokemon/) | Inheritance, abstract classes, evolution, trainers, and team battles | `python pokemon/example3.py` |
| [NumPy text processing](numpy_text_processing/) | Vocabularies, one-hot/cumulative encodings, bag of words, and cosine similarity | `python numpy_text_processing/demo.py` |

Both projects are available on `main` in two separate folders. Each has its own README and runnable examples.

## Quick start

The reference environment is **Python 3.12 and NumPy 2.0.0**, matching the surviving 2024 NumPy environment. The Pokemon project uses only the Python standard library.

```powershell
git clone https://github.com/shlomikarelitz/intro-to-computer-science-project.git
cd intro-to-computer-science-project
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

python pokemon/example3.py
python numpy_text_processing/demo.py
```

On macOS/Linux, create the environment with `python3.12 -m venv .venv` and activate it with `source .venv/bin/activate`.

## Run the tests

```text
python -m unittest discover -s pokemon -p "test_*.py" -v
python -m unittest discover -s numpy_text_processing -p "test_*.py" -v
```

The tests check the original Pokemon battle examples, trainer state isolation, vocabulary normalization, encoding/decoding, frequency calculations, and sentence similarity. These are targeted regression checks, not a claim that every historical edge case is correct.

## Structure

```text
pokemon/
  Pokemon.py, Fire.py, Water.py, Electric.py
  Charmander.py, Charmeleon.py, Charizard.py
  Squirtle.py, Wartortle.py, Blastoise.py, Pikachu.py
  Trainer.py, Battle.py
  example1.py, example2.py, example3.py
  test_pokemon.py, README.md
numpy_text_processing/
  Vocabulary.py
  demo.py, test_vocabulary.py
  verify_recovery.py, recovery_manifest.json
  README.md, RECOVERY.md
requirements.txt
```

## Source history and recovery

The Pokemon source files were recovered from the original `pocemon` project directory, with the active battle implementation last updated on **7 July 2024**. Duplicate battle drafts and the scratch `main.py` are excluded; the three original examples are retained.

The NumPy project was located in the original **HW4** directory. Its `Vocabulary.py` source had subsequently been overwritten, but a compiled CPython cache from **17 July 2024** survived. The readable module was reconstructed and checked against that cache: **all 30 code objects match in executable bytecode and execution-relevant metadata**. Comments and original formatting cannot be recovered. Details and a local verification utility are in [RECOVERY.md](numpy_text_processing/RECOVERY.md).

The historical algorithms and APIs are preserved. Newly added demos, tests, documentation, and project setup are separate from the recovered implementation. The original files on disk were left unchanged.

The local course directory contained **at least four identifiable coursework sets**:

| Recovered set | Evidence | Included here |
| --- | --- | --- |
| Introductory exercises | `pythonProject/my first project.py`, May 2024 | No |
| Recursion and backtracking | `HW2/main.py`, June 2024 | No |
| Pokemon OOP project | `pocemon/`, July 2024 | Yes |
| NumPy text encoders | `HW4/` surviving July 2024 cache | Yes |

The Pokemon assignment number could not be confirmed from an original assignment sheet. Later practice files and unrelated scripts are not counted as additional 2024 Semester B assignments.
