"""
Exercise 1 — Topic 5 (Circular Buffer, Ring Buffer): CircularBuffer  (Easy)
=================================================================
A circular buffer implements a fixed-capacity queue on a plain
array by advancing indices with modulo arithmetic:

    next_index = (current_index + 1) % capacity

This avoids dynamic allocation entirely — ideal for real-time
systems and streaming buffers.

Internal layout (capacity = 4):
  _buf  = [A, B, C, D]
  _head = 0   ← dequeue from here
  _tail = 0   ← enqueue here (wraps after C was placed)
  _count = 4

05b_moving_average.py builds on this class — finish enqueue/dequeue
here first.
=================================================================
"""

# Implement a fixed-capacity queue backed by a Python list.
#
# Rules:
#   • Do NOT use list.append() / list.pop(0) or a dynamically
#     growing list — use the fixed-size _buf with _head/_tail
#     modulo arithmetic only.
#
# Internal state (already provided):
#   _buf      — list pre-filled with None, length == capacity
#   _head     — index to dequeue from (front)
#   _tail     — index to enqueue at (rear)
#   _count    — number of elements currently stored
#
# enqueue(value): raise BufferError("full") if already full.
# dequeue():      raise BufferError("empty") if already empty.
#
# Example (capacity=3):
#   enqueue(A), enqueue(B), enqueue(C)  -> full
#   dequeue() -> A   dequeue() -> B
#   enqueue(D)                          -> D wraps to index 0
#   dequeue() -> C   dequeue() -> D

class CircularBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._buf   = [None] * capacity
        self._head  = 0
        self._tail  = 0
        self._count = 0

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == self.capacity

    def enqueue(self, value) -> None:
        """Add value to the rear. Raise BufferError if full."""
        # Time  complexity: O(?)
        # Space complexity: O(?)
        # YOUR CODE HERE
        bufferFull = self.is_full()
        if bufferFull:
            raise BufferError("full")
        self._buf[self._tail] = value
        self._tail = (self._tail + 1) % self.capacity
        self._count += 1

    def dequeue(self):
        """Remove and return the front value. Raise BufferError if empty."""
        # Time  complexity: O(?)
        # Space complexity: O(?)
        # YOUR CODE HERE
        bufferEmpty = self.is_empty()
        if bufferEmpty:
            raise BufferError("empty")
        value = self._buf[self._head]
        self._head = (self._head + 1) % self.capacity
        self._count -= 1
        return value


# ═════════════════════════════════════════════════════════════
# Tests — run with:  python 05a_circular_buffer.py
# ═════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== CircularBuffer ===")
    cb = CircularBuffer(3)
    cb.enqueue("A"); cb.enqueue("B"); cb.enqueue("C")
    assert cb.is_full(), "FAIL is_full"

    try:
        cb.enqueue("D")
        print("  FAIL: should raise BufferError when full")
    except BufferError:
        print("  BufferError on full  : OK")

    assert cb.dequeue() == "A", "FAIL dequeue A"
    assert cb.dequeue() == "B", "FAIL dequeue B"
    cb.enqueue("D")   # D wraps around to index 0
    assert cb.dequeue() == "C", "FAIL dequeue C"
    assert cb.dequeue() == "D", "FAIL dequeue D"
    assert cb.is_empty(), "FAIL is_empty"

    try:
        cb.dequeue()
        print("  FAIL: should raise BufferError when empty")
    except BufferError:
        print("  BufferError on empty : OK")
    print("  enqueue/dequeue/wrap-around: OK")

    print("\nAll CircularBuffer tests passed!")
