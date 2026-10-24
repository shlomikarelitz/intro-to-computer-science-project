# Pokemon Battle Simulator

An object-oriented, console-based Pokemon battle simulator from the 2024 Introduction to Computer Science course. This is a simulation library with runnable battle scenarios, rather than a graphical or interactive game.

## What it demonstrates

- An abstract `Pokemon` base class and elemental `Fire`, `Water`, and `Electric` types.
- Seven concrete Pokemon classes and evolution paths for Charmander and Squirtle.
- Attack/defense calculations, hit points, and battle eligibility.
- A `Trainer` class with capture logic, comparisons, and trainer combination.
- Individual duels and full team battles in `Battle`.
- Copying of trainer/Pokemon state so callers do not mutate a trainer through its getter.

## Run

No third-party dependencies are required. From the repository root:

```text
python pokemon/example1.py
python pokemon/example2.py
python pokemon/example3.py
```

The examples are the recovered original scenarios:

| Example | Scenario |
| --- | --- |
| `example1.py` | Pikachu versus Blastoise; the duel returns `(4, 1)`. |
| `example2.py` | A two-Pokemon team battle. |
| `example3.py` | Two teams of four; Misty wins in 15 rounds. |

Run the regression checks with:

```text
python -m unittest discover -s pokemon -p "test_*.py" -v
```

## Source selection

The thirteen implementation modules and three examples come from the original `pocemon` directory. The selected `Battle.py` and `Charizard.py` are the latest surviving versions, last modified on **7 July 2024**. `Battle2.py`, `adva.py`, IDE configuration, virtual environments, and the commented scratch `main.py` are excluded.

Implementation logic is preserved; only encoding/line endings and trailing whitespace were normalized. The tests and README were added during recovery. Historical behavior includes hit points becoming negative after an attack; the import does not redesign those mechanics.
