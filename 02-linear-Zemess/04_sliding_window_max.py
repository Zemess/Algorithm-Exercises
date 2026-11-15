"""
Exercise — Topic 4 (Deque, Double-Ended Queue): Sliding Window Maximum  (Challenging)
=================================================================
A deque supports insert and remove at BOTH ends.
It generalises Stack (one-end) and Queue (two-end, FIFO).

collections.deque quick reference:
  d = deque()
  d.append(x)         # add to RIGHT (rear)
  d.appendleft(x)     # add to LEFT  (front)
  d.pop()             # remove from RIGHT
  d.popleft()         # remove from LEFT
  d[0]  / d[-1]       # peek front / rear (read-only here)
=================================================================
"""

from collections import deque
from unittest import result


# Given arr and window size k, return the maximum of each
# contiguous window of size k as a list.
#
# Rules:
#   • Do NOT call max() over a fresh slice for each window —
#     process the array in a single pass instead.
#
# Example:
#   arr = [3, 1, 2, 5, 4, 6],  k = 3
#   windows: [3,1,2]->3  [1,2,5]->5  [2,5,4]->5  [5,4,6]->6
#   returns: [3, 5, 5, 6]

def sliding_window_max(arr: list, k: int) -> list:
    """Return the maximum of each sliding window of size k."""
    # Time  complexity: O(?)
    # Space complexity: O(?)
    # YOUR CODE HERE
    if not arr or k <= 0:
        return []
    result = []
    dq = deque()  # stores indices of potential max elements
    for i in range(len(arr)):
        # Remove indices that are out of the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove indices whose corresponding values are less than arr[i]
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        # Append the maximum for the current window to the result
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result

# ═════════════════════════════════════════════════════════════
# Tests — run with:  python 04_sliding_window_max.py
# ═════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== sliding_window_max ===")
    r1 = sliding_window_max([3, 1, 2, 5, 4, 6], k=3)
    assert r1 == [3, 5, 5, 6], f"FAIL: {r1}"
    print(f"  [3,1,2,5,4,6] k=3   -> {r1}")

    r2 = sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], k=3)
    assert r2 == [3, 3, 5, 5, 6, 7], f"FAIL: {r2}"
    print(f"  [1,3,-1,-3,5,3,6,7] -> {r2}")

    r3 = sliding_window_max([4, 3, 2, 1], k=1)
    assert r3 == [4, 3, 2, 1], f"FAIL k=1: {r3}"
    print(f"  k=1 (each element)  -> {r3}")

    r4 = sliding_window_max([1, 2, 3], k=3)
    assert r4 == [3], f"FAIL full window: {r4}"
    print(f"  k==n (one window)   -> {r4}")

    print("\nAll sliding_window_max tests passed!")
