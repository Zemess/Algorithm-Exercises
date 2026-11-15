"""
Shared helper for this repo's test files, and for the few exercise
files that build on an earlier exercise (e.g. 02b_is_palindrome.py
loading DoublyLinkedList from 02a_push_to_list.py).

Exercise files are named like "02a_push_to_list.py" -- a leading
digit makes that an invalid Python identifier, so they can't be
imported with a normal `import` statement. load_module() loads them
by file path instead.
"""

import importlib.util
import pathlib


def load_module(filename: str):
    """Load and execute filename (relative to this directory) as a module."""
    path = pathlib.Path(__file__).parent / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
