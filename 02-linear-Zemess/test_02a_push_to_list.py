"""
pytest test suite for Topic 2 (Doubly Linked List): push_back / push_front / to_list

Run with:
    pytest test_02a_push_to_list.py -v
"""

from _helpers import load_module

_mod = load_module("02a_push_to_list.py")
DoublyLinkedList = _mod.DoublyLinkedList


class TestPushAndToList:

    def test_forward_order(self):
        dll = DoublyLinkedList()
        dll.push_back(2)
        dll.push_back(3)
        dll.push_front(1)
        assert dll.to_list(True) == [1, 2, 3]

    def test_backward_order(self):
        dll = DoublyLinkedList()
        dll.push_back(2)
        dll.push_back(3)
        dll.push_front(1)
        assert dll.to_list(False) == [3, 2, 1]

    def test_size_tracks_pushes(self):
        dll = DoublyLinkedList()
        dll.push_back(2)
        dll.push_back(3)
        dll.push_front(1)
        assert dll.size == 3
