"""
Exercise 2 — Topic 5 (Circular Buffer, Ring Buffer): MovingAverage  (Easy)
=================================================================
Builds on 05a_circular_buffer.py's CircularBuffer — enqueue/dequeue
must already work there.
=================================================================
"""

from _helpers import load_module

_05a = load_module("05a_circular_buffer.py")
CircularBuffer = _05a.CircularBuffer

# Use CircularBuffer to track the last window_size readings and
# compute their running average.
#
# Rules:
#   • Do NOT recompute the sum from scratch on each call (e.g.
#     sum(...) over the buffer) — maintain _sum incrementally as
#     values are added and dropped.
#
# count() is already implemented (returns _buf._count).
#
# Example (window_size=3):
#   add(10) -> avg 10.0
#   add(20) -> avg 15.0
#   add(30) -> avg 20.0
#   add(40) -> avg 30.0   (10 was dropped)
#   add(50) -> avg 40.0   (20 was dropped)

class MovingAverage:
    def __init__(self, window_size: int):
        self._buf = CircularBuffer(window_size)
        self._sum = 0.0

    def add(self, value: float) -> None:
        """Add a new reading, dropping the oldest when the window is full."""
        # Time  complexity: O(?)
        # Space complexity: O(?)
        # YOUR CODE HERE
        addedValue = value
        if self._buf.is_full():
            droppedValue = self._buf.dequeue()
            self._sum -= droppedValue
        self._buf.enqueue(addedValue)
        self._sum += addedValue
        pass

    def average(self) -> float:
        """Return the mean of the stored readings (0.0 if empty)."""
        # Time  complexity: O(?)
        # Space complexity: O(?)
        # YOUR CODE HERE
        if self._buf.is_empty():
            return 0.0
        return self._sum / self._buf._count

    def count(self) -> int:
        return self._buf._count


# ═════════════════════════════════════════════════════════════
# Tests — run with:  python 05b_moving_average.py
# ═════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== MovingAverage ===")
    ma = MovingAverage(3)
    ma.add(10); assert ma.average() == 10.0 and ma.count() == 1, "FAIL after 10"
    ma.add(20); assert ma.average() == 15.0 and ma.count() == 2, "FAIL after 20"
    ma.add(30); assert ma.average() == 20.0 and ma.count() == 3, "FAIL after 30"
    ma.add(40); assert ma.average() == 30.0 and ma.count() == 3, "FAIL after 40"
    ma.add(50); assert ma.average() == 40.0 and ma.count() == 3, "FAIL after 50"
    print(f"  window=3, add [10..50]: avg after 50 = {ma.average()}")

    ma2 = MovingAverage(2)
    assert ma2.average() == 0.0, "FAIL empty average"
    print("  empty average = 0.0 : OK")

    print("\nAll MovingAverage tests passed!")
