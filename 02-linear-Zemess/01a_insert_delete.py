"""
Exercise 1 — Topic 1 (Arrays): Insert and Delete at Index  (Easy)
=================================================================
Arrays store elements in consecutive memory locations. Random
access uses direct indexing, but insert/delete requires shifting
all elements after the target position.
=================================================================
"""

# insert_at(arr, index, value) — inserts value at the given
#   index by manually shifting elements to the right.
#
# Rules:
#   • Do NOT use list.insert() or slicing.
#
# Example:
#   arr = [10, 20, 30, 40]
#   insert_at(arr, 1, 99)  ->  arr becomes [10, 99, 20, 30, 40]

def insert_at(arr: list, index: int, value) -> None:
    """Insert value at index by shifting elements right."""
    # Time  complexity: O(?)
    # Space complexity: O(?)
    # YOUR CODE HERE
    index = max(0, min(index, len(arr))) # clamp index to valid range
    arr.append(None) # add a placeholder to increase the size of the array
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1] # shift elements to the right
    arr[index] = value # insert the new value at the specified index
    return None


# delete_at(arr, index) — removes the element at index by
#   manually shifting elements to the left, then returns it.
#
# Rules:
#   • Do NOT use del, list.remove(), or list.pop(index).
#   • arr.pop() with no argument is the only pop allowed.
#
# Example:
#   arr = [10, 20, 30, 40]
#   val = delete_at(arr, 2)  ->  val == 30,  arr becomes [10, 20, 40]

def delete_at(arr: list, index: int):
    """Delete element at index by shifting elements left. Return the removed value."""
    # Time  complexity: O(?)
    # Space complexity: O(?)
    # YOUR CODE HERE
    index = max(0, min(index, len(arr) - 1)) # clamp index to valid range
    value = arr[index] # store the value to be removed
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1] # shift elements to the left
    arr.pop() # remove the last element (which is now a duplicate)
    return value


# ═════════════════════════════════════════════════════════════
# Tests — run with:  python 01a_insert_delete.py
# ═════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== insert_at ===")
    a = [10, 20, 30, 40]
    insert_at(a, 1, 99)
    assert a == [10, 99, 20, 30, 40], f"FAIL: {a}"
    print(f"  insert at index 1  : {a}")

    b = [10, 20, 30, 40]
    insert_at(b, 0, 5)
    assert b == [5, 10, 20, 30, 40], f"FAIL: {b}"
    print(f"  insert at index 0  : {b}")

    c = [10, 20, 30, 40]
    insert_at(c, 4, 99)
    assert c == [10, 20, 30, 40, 99], f"FAIL: {c}"
    print(f"  insert at end      : {c}")

    print("\n=== delete_at ===")
    d = [10, 20, 30, 40]
    v = delete_at(d, 2)
    assert v == 30 and d == [10, 20, 40], f"FAIL: val={v} arr={d}"
    print(f"  delete index 2     : removed {v}, arr={d}")

    e = [10, 20, 30, 40]
    v2 = delete_at(e, 0)
    assert v2 == 10 and e == [20, 30, 40], f"FAIL: val={v2} arr={e}"
    print(f"  delete index 0     : removed {v2}, arr={e}")

    f = [10, 20, 30, 40]
    v3 = delete_at(f, 3)
    assert v3 == 40 and f == [10, 20, 30], f"FAIL: val={v3} arr={f}"
    print(f"  delete last index  : removed {v3}, arr={f}")

    print("\nAll insert/delete tests passed!")
