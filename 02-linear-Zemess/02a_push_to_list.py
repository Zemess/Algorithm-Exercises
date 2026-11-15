"""
Exercise 1 — Topic 2 (Doubly Linked List): Push & to_list  (Easy)
=================================================================
Each node has a .prev AND a .next pointer.
Key advantages over singly linked:
  • Traverse in both directions.
  • Delete a node given only its reference — the .prev pointer
    gives direct access to the predecessor.

02b_is_palindrome.py builds on the DoublyLinkedList class defined
here — finish push_back/push_front/to_list in this file first.
=================================================================
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev  = None
        self.next  = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None   # first node
        self.tail = None   # last node
        self.size = 0

    # Implement three methods:
    #
    # push_back(value)        — add a new node at the TAIL.
    # push_front(value)       — add a new node at the HEAD.
    # to_list(forward=True)   — return values in traversal order,
    #                            head->tail if forward, tail->head
    #                            otherwise.
    #
    # Rules:
    #   • Keep both .prev and .next consistent on every node you
    #     touch, and handle the empty-list case (self.head is None).
    #
    # Example:
    #   push_back(1), push_back(2), push_front(0)
    #   to_list(True)   -> [0, 1, 2]
    #   to_list(False)  -> [2, 1, 0]

    def push_back(self, value) -> None:
        """Add a new node at the tail."""
        # Time  complexity: O(?)
        # Space complexity: O(?)
        # YOUR CODE HERE
        pushBack = Node(value)
        if self.head is None:
            self.head = pushBack
            self.tail = pushBack
        else:
            pushBack.prev = self.tail
            self.tail.next = pushBack
            self.tail = pushBack
        self.size += 1

    def push_front(self, value) -> None:
        """Add a new node at the head."""
        # Time  complexity: O(?)
        # Space complexity: O(?)
        # YOUR CODE HERE
        pushFront = Node(value)
        if self.head is None:
            self.head = pushFront
            self.tail = pushFront
        else:
            pushFront.next = self.head
            self.head.prev = pushFront
            self.head = pushFront
        self.size += 1

    def to_list(self, forward: bool = True) -> list:
        """Return all values as a list (forward head->tail or backward tail->head)."""
        # Time  complexity: O(?)
        # Space complexity: O(?)
        # YOUR CODE HERE
        result = []
        current = self.head if forward else self.tail
        while current is not None:
            result.append(current.value)
            current = current.next if forward else current.prev
        return result


# ═════════════════════════════════════════════════════════════
# Tests — run with:  python 02a_push_to_list.py
# ═════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== push_front / push_back / to_list ===")
    dll = DoublyLinkedList()
    dll.push_back(2)
    dll.push_back(3)
    dll.push_front(1)
    assert dll.to_list(True)  == [1, 2, 3], f"FAIL forward: {dll.to_list(True)}"
    assert dll.to_list(False) == [3, 2, 1], f"FAIL backward: {dll.to_list(False)}"
    assert dll.size == 3, f"FAIL size: {dll.size}"
    print(f"  forward  : {dll.to_list(True)}")
    print(f"  backward : {dll.to_list(False)}")

    print("\nAll push/to_list tests passed!")
