"""
pytest test suite for Topic 2 (Doubly Linked List): is_palindrome_values

Run with:
    pytest test_02b_is_palindrome.py -v
"""

from _helpers import load_module

_02a = load_module("02a_push_to_list.py")
DoublyLinkedList = _02a.DoublyLinkedList

_mod = load_module("02b_is_palindrome.py")
is_palindrome_values = _mod.is_palindrome_values


def _make_list(values):
    dll = DoublyLinkedList()
    for v in values:
        dll.push_back(v)
    return dll


class TestIsPalindromeValues:

    def test_odd_length_palindrome(self):
        assert is_palindrome_values(_make_list([1, 2, 3, 2, 1])) is True

    def test_not_a_palindrome(self):
        assert is_palindrome_values(_make_list([1, 2, 3])) is False

    def test_single_element_is_palindrome(self):
        assert is_palindrome_values(_make_list([1])) is True

    def test_even_length_palindrome(self):
        assert is_palindrome_values(_make_list([1, 2, 2, 1])) is True

    def test_even_length_non_palindrome(self):
        assert is_palindrome_values(_make_list([1, 2])) is False
