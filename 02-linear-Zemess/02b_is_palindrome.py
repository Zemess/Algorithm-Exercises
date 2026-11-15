"""
Exercise 2 — Topic 2 (Doubly Linked List): Palindrome Value Check  (Easy)
=================================================================
Builds on 02a_push_to_list.py's DoublyLinkedList — push_back must
already work there, since the tests below use it to build a list to
check.
=================================================================
"""

from _helpers import load_module

_02a = load_module("02a_push_to_list.py")
DoublyLinkedList = _02a.DoublyLinkedList

# Check whether the list values form a palindrome by comparing
# from BOTH ends inward — possible in a doubly linked list because
# self.head and self.tail are both known.
#
# Rules:
#   • Do NOT call dll.to_list() and compare it against its
#     reverse (e.g. dll.to_list() == dll.to_list()[::-1]) —
#     walk the head/tail pointers directly.
#   • Do not build an auxiliary list.
#
# Example:
#   [1, 2, 3, 2, 1]  ->  True
#   [1, 2, 3]        ->  False
#   [1, 1]           ->  True
#   [7]              ->  True

def is_palindrome_values(dll: DoublyLinkedList) -> bool:
    """Return True if the list values read the same forwards and backwards."""
    # Time  complexity: O(?)
    # Space complexity: O(?)
    # YOUR CODE HERE
    palCheck = True
    left = dll.head
    right = dll.tail
    while left is not None and right is not None and left != right and left.prev != right:
        if left.value != right.value:
            palCheck = False
            break
        left = left.next
        right = right.prev
    return palCheck


# ═════════════════════════════════════════════════════════════
# Tests — run with:  python 02b_is_palindrome.py
# ═════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== is_palindrome_values ===")
    def _dll(values):
        d = DoublyLinkedList()
        for v in values:
            d.push_back(v)
        return d

    assert is_palindrome_values(_dll([1, 2, 3, 2, 1])) == True,  "FAIL"
    assert is_palindrome_values(_dll([1, 2, 3]))        == False, "FAIL"
    assert is_palindrome_values(_dll([1]))              == True,  "FAIL"
    assert is_palindrome_values(_dll([1, 1]))           == True,  "FAIL"
    assert is_palindrome_values(_dll([1, 2, 2, 1]))     == True,  "FAIL"
    assert is_palindrome_values(_dll([1, 2]))           == False, "FAIL"
    print(f"  [1,2,3,2,1] -> {is_palindrome_values(_dll([1,2,3,2,1]))}")
    print(f"  [1,2,3]     -> {is_palindrome_values(_dll([1,2,3]))}")
    print(f"  [1,2,2,1]   -> {is_palindrome_values(_dll([1,2,2,1]))}")

    print("\nAll is_palindrome_values tests passed!")
