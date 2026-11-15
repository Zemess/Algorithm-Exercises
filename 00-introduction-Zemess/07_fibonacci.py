"""
Exercise 6 — Fibonacci Sequence (Easy)
=================================================================
Implement fibonacci(n) that returns the first n numbers of the
Fibonacci sequence, where each number is the sum of the two
before it. There's no built-in for this — write the loop.

Rules:
  • Start the list with [0, 1].
  • Keep appending sequence[-1] + sequence[-2] until the list
    has n elements.

Example:
    fibonacci(8)  ->  [0, 1, 1, 2, 3, 5, 8, 13]
=================================================================
"""

def fibonacci(n: int) -> list:
    """Return the first n Fibonacci numbers."""
    # YOUR CODE HERE
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence[:n]


if __name__ == "__main__":
    print(fibonacci(8))  # Expected: [0, 1, 1, 2, 3, 5, 8, 13]
