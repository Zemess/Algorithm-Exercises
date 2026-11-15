"""
pytest test suite for Topic 4 (Deque): sliding_window_max

Run with:
    pytest test_04_sliding_window_max.py -v
"""

from _helpers import load_module

_mod = load_module("04_sliding_window_max.py")
sliding_window_max = _mod.sliding_window_max


class TestSlidingWindowMax:

    def test_typical_case(self):
        assert sliding_window_max([3, 1, 2, 5, 4, 6], k=3) == [3, 5, 5, 6]

    def test_with_negative_numbers(self):
        assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]

    def test_window_of_one_returns_original(self):
        assert sliding_window_max([4, 3, 2, 1], k=1) == [4, 3, 2, 1]

    def test_window_equals_length(self):
        assert sliding_window_max([1, 2, 3], k=3) == [3]
