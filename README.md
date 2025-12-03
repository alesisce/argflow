# Argflow

**Argflow** is a fast, lightweight, and modular argument parser for Python.
It is designed as a **simpler alternative to `argparse`**, ideal for small to medium CLI scripts.


## Features

* Minimal and easy-to-use API.
* Modular callbacks for each argument-
* Extremely fast parsing (\~70 lines of code).
* Built-in helper.
* Super flexible.

## Argflow vs Argparse

> Note: `argparse` has more features, so its execution time is naturally higher.

Benchmark for a single argument:

| Parser   | Parse Time |
| -------- | ---------- |
| argparse | 0.009876 s |
| argflow  | 0.000215 s |

* **Argflow is \~98% faster** than `argparse` for parsing.
* Demonstrates how a compact library can create **powerful and fast CLIs**.

## Reliability

* Argflow is **relatively new** and still in active development.
* Suitable for personal projects and experiments, but **use with caution in critical production environments**.

## Example Usage

```python
from argflow import argflow

ag = argflow()

@ag.new_argument(flag="--hello", helper="Just, welcoming...", example="--hello=Jack") # Adding new argument
def hello(name):
    print("Hello, " name + "!")

ag.parse() # Parsing
```

Command line:

```bash
python script.py --hello=Alice
# Output: Hello, Alice!
```


## License

MIT License – free to use, modify, and distribute.
