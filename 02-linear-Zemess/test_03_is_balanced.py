"""
pytest test suite for Topic 3 (Stack): is_balanced

Run with:
    pytest test_03_is_balanced.py -v
"""

from _helpers import load_module

_mod = load_module("03_is_balanced.py")
is_balanced = _mod.is_balanced


class TestIsBalanced:

    def test_all_bracket_types_balanced(self):
        assert is_balanced("([]{})") is True

    def test_wrong_order_is_unbalanced(self):
        assert is_balanced("([)]") is False

    def test_wrong_pair_is_unbalanced(self):
        assert is_balanced("{[}") is False

    def test_empty_string_is_balanced(self):
        assert is_balanced("") is True

    def test_nested_same_bracket(self):
        assert is_balanced("((()))") is True

    def test_unclosed_bracket_is_unbalanced(self):
        assert is_balanced("(") is False

    def test_non_bracket_characters_are_ignored(self):
        assert is_balanced("hello()") is True
