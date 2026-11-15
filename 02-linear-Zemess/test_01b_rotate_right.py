"""
pytest test suite for Topic 1 (Arrays): rotate_right

Run with:
    pytest test_01b_rotate_right.py -v
"""

from _helpers import load_module

_mod = load_module("01b_rotate_right.py")
reverse_segment = _mod.reverse_segment
rotate_right = _mod.rotate_right


class TestRotateRight:

    def test_reverse_segment_helper(self):
        a = [1, 2, 3, 4, 5]
        reverse_segment(a, 0, 4)
        assert a == [5, 4, 3, 2, 1]

    def test_rotate_by_two(self):
        a = [1, 2, 3, 4, 5]
        rotate_right(a, 2)
        assert a == [4, 5, 1, 2, 3]

    def test_rotate_wraps_around(self):
        a = [1, 2, 3, 4, 5]
        rotate_right(a, 7)
        assert a == [4, 5, 1, 2, 3]

    def test_rotate_full_length_is_noop(self):
        a = [1, 2, 3]
        rotate_right(a, 3)
        assert a == [1, 2, 3]

    def test_rotate_single_element(self):
        a = [42]
        rotate_right(a, 5)
        assert a == [42]
