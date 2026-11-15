# 02-linear — Linear Data Structures

Five linear data structures: arrays, doubly linked lists, stacks,
deques, and circular buffers. In most files, exercises are Easy except
the last one, which is Challenging (a few files are Easy throughout).
Each file has a function with `# YOUR CODE HERE` for you to fill in,
and a matching `test_*.py` file you can use to check your work as you
go. You don't need to touch the test files — they're just there to
help you see how you're doing.

Right above each `# YOUR CODE HERE`, you'll also find:
```python
# Time  complexity: O(?)
# Space complexity: O(?)
```
Replace the `O(?)` with your own analysis of the function you just
wrote — this is part of the exercise, not optional decoration.

Once you've filled one in and pushed, pull your repo and look for
`COMPLEXITY_FEEDBACK.md`: for any exercise whose tests are passing, it
shows the correct time/space complexity so you can compare it against
your own answer. This is purely informational — it doesn't check
whether your answer is right and has no effect on your score, it's
just there so you get feedback on your reasoning.

Common complexity classes, fastest to slowest:

| Complexity | Name | Typical example |
|---|---|---|
| `O(1)` | Constant | array index access, push/pop on a stack, one arithmetic step |
| `O(log n)` | Logarithmic | binary search, walking down a balanced tree |
| `O(n)` | Linear | a single pass over a list or string |
| `O(n log n)` | Linearithmic | efficient sorting (merge sort, heapsort) |
| `O(n^2)` | Quadratic | a nested loop over the same input (e.g. comparing every pair) |

## The files

Each exercise gets its own file (rather than several exercises sharing
one file per topic), so you can run and test one exercise at a time.

| File | Topic | Exercise | Points |
|---|---|---|---|
| `01a_insert_delete.py` | Arrays | 1 — `insert_at` + `delete_at` | 1 |
| `01b_rotate_right.py` | Arrays | 2 — `rotate_right` | 1 |
| `02a_push_to_list.py` | Doubly Linked List | 1 — `push_back`/`push_front`/`to_list` | 1 |
| `02b_is_palindrome.py` | Doubly Linked List | 2 — `is_palindrome_values` | 1 |
| `03_is_balanced.py` | Stack (LIFO) | 1 — `is_balanced` | 1 |
| `04_sliding_window_max.py` | Deque | 1 — `sliding_window_max` | 1 |
| `05a_circular_buffer.py` | Circular Buffer | 1 — `CircularBuffer` | 1 |
| `05b_moving_average.py` | Circular Buffer | 2 — `MovingAverage` | 1 |
| **Total** | | | **8** |

A few files depend on an earlier one in the same topic — finish
`02a_push_to_list.py` before `02b`, and `05a_circular_buffer.py`
before `05b_moving_average.py`. Each such file says so at the top.

## Step by step

1. **Clone this repo**:
   ```
   git clone <this repo's URL>
   cd <the folder that creates>
   ```
2. **Set up a virtual environment and install dependencies**:
   ```
   python -m venv .venv
   .venv\Scripts\activate      # Windows — use "source .venv/bin/activate" on macOS/Linux
   pip install -r requirements.txt
   ```
3. **Open the folder in VS Code**: `code .` (or File -> Open Folder). If
   prompted "This workspace has extension recommendations", click
   **Install** — this adds a beaker-shaped **Testing** icon to the left
   sidebar.
4. **Run the tests before changing anything**, just to see where you're
   starting from. Click the beaker icon, then the play button at the top
   of the Test Explorer panel — everything will be red at first, and
   that's completely normal.
5. **Implement each exercise** in its source file, one at a time — start
   with `01a_insert_delete.py` and work through to `05b_moving_average.py`.
   Each file has exactly one exercise, so you can run it on its own
   (`python 01a_insert_delete.py`) without needing the rest finished.
6. **Re-run the tests** after each change to see your progress. Prefer a
   terminal? `pytest -v` does the same check for all exercises at once.
7. **Work locally** until all tests pass.
8. **Push your work back** to the GitHub organization when you're ready:
   ```
   git add -A
   git commit -m "Exercises done"
   git push
   ```
9. **Assignment completed — good job!**

---

## Topic 1: Arrays

Arrays store elements in **consecutive memory locations**. Random access uses direct indexing, but insert/delete requires shifting all elements after the target position.

### Exercise 1 — Insert and Delete at Index `(Easy)`

Implement two functions:

**`insert_at(arr, index, value)`** — inserts `value` at the given index.

**Rules:**
- Do **not** use `list.insert()` or slicing.

**Example:**
```
arr = [10, 20, 30, 40]
insert_at(arr, 1, 99)  ->  arr becomes [10, 99, 20, 30, 40]
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

- First grow the list with `arr.append(None)`.
- Then shift elements from the last position down to `index + 1` one step to the right using a loop.
- Finally set `arr[index] = value`.

</details>

**`delete_at(arr, index)`** — removes the element at `index` and returns it.

**Rules:**
- Do **not** use `del`, `list.remove()`, or `list.pop(index)`.
- `arr.pop()` with no argument is the only pop allowed.

**Example:**
```
arr = [10, 20, 30, 40]
val = delete_at(arr, 2)  ->  val == 30,  arr becomes [10, 20, 40]
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

- Shift elements leftward with a loop, closing the gap at `index`.
- Shrink the list with `arr.pop()` — used solely to discard the now-duplicate last slot.

</details>

### Exercise 2 — Array Rotation `(Challenging)`

Rotate `arr` to the right by `k` positions. Modify `arr` directly — do not return a new list, and do not use slicing or temporary lists. Implement the helper `reverse_segment(arr, lo, hi)` first.

**Example:**
```
arr = [1, 2, 3, 4, 5],  k = 2  ->  [4, 5, 1, 2, 3]
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

What happens if you reverse the *entire* array first? The elements end up roughly in the right place, except each of the two halves that should stay in order is now itself backwards. What would undo just that part?

1. Reverse the entire array.
2. Reverse only the first `k` elements.
3. Reverse the remaining elements.

Start by normalising: `k = k % len(arr)`.

</details>

Exercise 1's stub is `01a_insert_delete.py`; Exercise 2's is `01b_rotate_right.py`.

---

## Topic 2: Doubly Linked List

Each node has a `.prev` **and** a `.next` pointer. Key advantages over a singly linked list: traverse in both directions, and delete a node given only its reference.

### Exercise 1 — Push & to_list `(Easy)`

Implement `push_back`, `push_front`, and `to_list(forward=True)` on `DoublyLinkedList`.

**Rules:**
- Keep both `.prev` and `.next` consistent on every node you touch, and handle the empty-list case.

**Example:**
```
push_back(1), push_back(2), push_front(0)
to_list(True)   ->  [0, 1, 2]
to_list(False)  ->  [2, 1, 0]
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

**`push_back(value)`**
- Set `new_node.prev = self.tail`.
- If the list is non-empty, set `self.tail.next = new_node`.
- Update `self.tail = new_node` (and `self.head` too, if the list was empty).

**`push_front(value)`** — mirror image of `push_back`, at the head.

**`to_list(forward=True)`** — start at `self.head` (or `self.tail` if not `forward`) and follow the links.

</details>

### Exercise 2 — Palindrome Value Check `(Easy)`

Compare from both ends inward using `head`/`tail`, no extra memory.

**Rules:**
- Do **not** call `to_list()` and compare it against its reverse — walk the `head`/`tail` pointers directly.
- Do not build an auxiliary list.

**Examples:**
```
[1, 2, 3, 2, 1]  ->  True
[1, 2, 3]        ->  False
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

You don't need to build a copy of the list to check this — you already have direct access to both ends. What if you compared them and then moved each one a step closer to the middle?

Start `left` at `head` and `right` at `tail`, compare values, then step `left` forward and `right` backward, for `size // 2` iterations.

</details>

Exercise 1's stub is `02a_push_to_list.py`; Exercise 2's is `02b_is_palindrome.py`
(imports `DoublyLinkedList` from `02a_push_to_list.py` — finish that one first).

---

## Topic 3: Stack (LIFO)

A stack exposes only the **top** element. Last In — First Out.

### Balanced Brackets `(Easy)`

Return `True` if every opening bracket has a correctly matching closing bracket in the right order.

**Examples:**
```
is_balanced("([]{})")   ->  True
is_balanced("([)]")     ->  False   (wrong order)
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

- On an opening bracket, push it.
- On a closing bracket: if the stack is empty or the popped top doesn't match, return `False`.
- At the end, the stack must be empty.

</details>

The stub to fill in is `03_is_balanced.py`.

---

## Topic 4: Deque (Double-Ended Queue)

A deque supports **insert and remove at both ends**. It generalises Stack (one-end) and Queue (two-end, FIFO).

### Exercise 1 — Sliding Window Maximum `(Challenging)`

Return the maximum of each contiguous window of size `k`.

**Rules:**
- Do **not** call `max()` over a fresh slice for each window — process the array in a single pass instead.

**Example:**
```
sliding_window_max([3, 1, 2, 5, 4, 6], k=3)  ->  [3, 5, 5, 6]
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

As the window slides, most values you've seen could never become a future maximum once a bigger value shows up after them — so why keep them around at all? Think about what's left if you only ever keep the values that could *still* win.

Maintain a deque of **indices** whose values stay in decreasing order — the front is always the current window's maximum. On each step: drop front indices that fell out of the window, drop rear indices whose value is ≤ the new value (they can never win), then push the new index.

</details>

The stub to fill in is `04_sliding_window_max.py`.

---

## Topic 5: Circular Buffer (Ring Buffer)

A circular buffer implements a **fixed-capacity queue** on a plain array by advancing indices with modulo arithmetic. This avoids dynamic allocation entirely.

### Exercise 1 — CircularBuffer `(Easy)`

Implement a fixed-capacity queue backed by a Python list, using `_head`/`_tail`/`_count` and modulo arithmetic. Raise `BufferError` on overflow/underflow.

**Rules:**
- Do **not** use `list.append()` / `list.pop(0)` or a dynamically growing list.

**Example (capacity = 3):**
```
enqueue(A), enqueue(B), enqueue(C)  ->  full
dequeue()  ->  A
dequeue()  ->  B
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

`enqueue`: store at `_buf[_tail]`, then `_tail = (_tail + 1) % capacity`, then increment `_count`.
`dequeue`: read `_buf[_head]`, then `_head = (_head + 1) % capacity`, then decrement `_count`.

</details>

The stub to fill in is `05a_circular_buffer.py`.

### Exercise 2 — MovingAverage `(Easy)`

Use `CircularBuffer` (Exercise 1) to track the last `window_size` readings and compute their running average, maintaining a running `_sum`.

**Rules:**
- Do **not** recompute the sum from scratch on each call — maintain `_sum` incrementally.

**Example (`window_size = 3`):**
```
add(10)  ->  avg 10.0
add(20)  ->  avg 15.0
add(30)  ->  avg 20.0
```

<details>
<summary>Hint: algorithm walkthrough (click if stuck)</summary>

`add`: if the buffer is full, dequeue the oldest and subtract it from `_sum` first; then enqueue the new value and add it to `_sum`.
`average`: `_sum / count()`, or `0.0` if empty.

</details>

The stub to fill in is `05b_moving_average.py` (imports `CircularBuffer` from `05a_circular_buffer.py` — finish that one first).
