# Python

## Set up venv

```sh
python -m venv venv
source venv/bin/activate
pip install -e .
```

The editable install puts the `aoc` package on `sys.path`, so solutions can
`from aoc import graph, grid, ints, letter, screen, intcode` from any directory.
Re-run `pip install -e .` after recreating the venv; new modules added under
`aoc/` need no reinstall.

## Run a solution

Solutions read `input.txt` from the working directory:

```sh
cd 2019/02 && python 02.py
```
