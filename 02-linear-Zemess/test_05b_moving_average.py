"""
pytest test suite for Topic 5 (Circular Buffer): MovingAverage

Run with:
    pytest test_05b_moving_average.py -v
"""

from _helpers import load_module

_mod = load_module("05b_moving_average.py")
MovingAverage = _mod.MovingAverage


class TestMovingAverage:

    def test_average_grows_within_window(self):
        ma = MovingAverage(3)
        ma.add(10)
        assert ma.average() == 10.0
        ma.add(20)
        assert ma.average() == 15.0
        ma.add(30)
        assert ma.average() == 20.0

    def test_oldest_reading_dropped_once_full(self):
        ma = MovingAverage(3)
        for v in [10, 20, 30, 40]:
            ma.add(v)
        assert ma.average() == 30.0
        assert ma.count() == 3

    def test_empty_average_is_zero(self):
        ma = MovingAverage(2)
        assert ma.average() == 0.0
