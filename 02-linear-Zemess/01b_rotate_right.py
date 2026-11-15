"""
Exercise 2 — Topic 1 (Arrays): Array Rotation  (Challenging)
=================================================================
Arrays store elements in consecutive memory locations. Random
access uses direct indexing, but insert/delete requires shifting
all elements after the target position.
=================================================================
"""

# Rotate arr to the right by k positions. Modify arr directly —
# do not return a new list, and do not use slicing or temporary
# lists.
#
# Implement the helper reverse_segment(arr, lo, hi) first — it
# reverses arr[lo..hi] inclusive, modifying it directly.
#
# Handle k >= len(arr) and k == 0 correctly.
#
# Example:
#   arr = [1, 2, 3, 4, 5],  k = 2  ->  [4, 5, 1, 2, 3]
#   arr = [1, 2, 3, 4, 5],  k = 7  ->  [4, 5, 1, 2, 3]  (7 % 5 == 2)
#   arr = [1, 2, 3],        k = 3  ->  [1, 2, 3]         (full rotation)

def reverse_segment(arr: list, lo: int, hi: int) -> None:
    """Reverse arr[lo..hi] directly."""
    # Time  complexity: O(?)
    # Space complexity: O(?)
    # YOUR CODE HERE
    rotate = hi - lo + 1
    for i in range(rotate // 2):
        arr[lo + i], arr[hi - i] = arr[hi - i], arr[lo + i]
    pass


def rotate_right(arr: list, k: int) -> None:
    """Rotate arr right by k steps, modifying it directly."""
    # Time  complexity: O(?)
    # Space complexity: O(?)
    # YOUR CODE HERE
    if not arr or k == 0:
        return
    k = k % len(arr)  # Handle k >= len(arr)
    reverse_segment(arr, 0, len(arr) - 1)  # Reverse the entire array
    reverse_segment(arr, 0, k - 1)  # Reverse the first k elements
    reverse_segment(arr, k, len(arr) - 1)  # Reverse the remaining elements

# ═════════════════════════════════════════════════════════════
# Tests — run with:  python 01b_rotate_right.py
# ═════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== rotate_right ===")
    g = [1, 2, 3, 4, 5]
    rotate_right(g, 2)
    assert g == [4, 5, 1, 2, 3], f"FAIL: {g}"
    print(f"  k=2                : {g}")

    h = [1, 2, 3, 4, 5]
    rotate_right(h, 7)
    assert h == [4, 5, 1, 2, 3], f"FAIL: {h}"
    print(f"  k=7 (7%5==2)       : {h}")

    i = [1, 2, 3]
    rotate_right(i, 3)
    assert i == [1, 2, 3], f"FAIL: {i}"
    print(f"  k==n (no change)   : {i}")

    j = [42]
    rotate_right(j, 5)
    assert j == [42], f"FAIL: {j}"
    print(f"  single element     : {j}")

    print("\nAll rotate_right tests passed!")
