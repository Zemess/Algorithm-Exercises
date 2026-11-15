"""
pytest test suite for Topic 5 (Circular Buffer): CircularBuffer

Run with:
    pytest test_05a_circular_buffer.py -v
"""

import pytest

from _helpers import load_module

_mod = load_module("05a_circular_buffer.py")
CircularBuffer = _mod.CircularBuffer


class TestCircularBuffer:

    def test_enqueue_dequeue_fifo_order(self):
        cb = CircularBuffer(3)
        cb.enqueue("A")
        cb.enqueue("B")
        cb.enqueue("C")
        assert cb.dequeue() == "A"
        assert cb.dequeue() == "B"

    def test_enqueue_on_full_raises(self):
        cb = CircularBuffer(3)
        cb.enqueue("A")
        cb.enqueue("B")
        cb.enqueue("C")
        with pytest.raises(BufferError):
            cb.enqueue("D")

    def test_wrap_around_after_dequeue(self):
        cb = CircularBuffer(3)
        cb.enqueue("A")
        cb.enqueue("B")
        cb.enqueue("C")
        cb.dequeue()
        cb.dequeue()
        cb.enqueue("D")
        assert cb.dequeue() == "C"
        assert cb.dequeue() == "D"
        assert cb.is_empty()

    def test_dequeue_on_empty_raises(self):
        cb = CircularBuffer(2)
        with pytest.raises(BufferError):
            cb.dequeue()
