# Extended Introduction to Computer Science - Homework 3

A 2017 CS BSc Python assignment covering integer root search, selection-sorted blocks and pairwise merging, bounded-triplet sorting, finite-difference derivatives, Newton-Raphson root approximation, and numerical inverse functions.

## Algorithms

- Search linearly for a positive integer root, search a bounded interval by integer binary search, and discover a search interval through exponential expansion.
- Sort fixed-size blocks with selection sort and merge the blocks in a balanced sequence.
- Sort bounded integer triplets through coordinate-space enumeration and through a non-mutating selection sort.
- Approximate derivatives, function intersections, source values, and inverse functions numerically.

## Setup

```bash
git clone https://github.com/KobieHazon/bsc-extended-intro-cs-hw3.git
cd bsc-extended-intro-cs-hw3
uv sync --dev
```

The maintained package supports Python 3.10 or newer and has no runtime dependencies.

## Usage

```bash
uv run extended-intro-hw3 block-sort 3 610 906 308 759 15 389
uv run extended-intro-hw3 triplet-selection-sort 10 4,2,1 1,4,3 4,2,0
```

The commands print sorted lists while leaving their inputs unchanged. The numerical routines are intended for direct Python use:

```python
from extended_intro_hw3 import inverse, source

source(lambda value: value + 3, 5)
inverse(lambda value: value**3)(-27)
```

## Testing

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

The tests cover all maintained algorithms, invalid inputs, duplicate triplets, empty blocks, deterministic numerical behavior, command-line output, and the complete supplied tester. The untouched recovered solution passes that tester under a fixed random seed before modernization.

## Repository Structure

- `assignment/hw3_tester.py`: supplied tester preserved in its original form
- `assignment/score-key.pdf`: supplied grading key
- `solution/written-answers.pdf`: my six-page written submission with identifying metadata reduced to the author's name
- `src/extended_intro_hw3/`: maintained algorithms and command-line interface
- `tests/`: portable pytest regression suite, including the supplied tester

## Implementation notes

The recovered source combines my implementations with the distributed scaffold. The scaffold comments remain in the historical solution commit and are not presented as authored work.

## Numerical Scope

These routines are educational implementations, not general-purpose numerical-analysis software. The integer-root functions rely on monotonicity assumptions described by their interfaces, and Newton-Raphson can return no result when it encounters a near-zero derivative, invalid arithmetic, non-finite values, or the iteration limit. The maintained default starting value is deterministic so results do not depend on process-global randomness.

## License

No repository-wide license is declared because the repository combines original work with supplied material whose reuse terms were not recorded.
