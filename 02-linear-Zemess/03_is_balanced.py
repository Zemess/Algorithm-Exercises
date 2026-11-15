"""
Exercise — Topic 3 (Stack, LIFO): Balanced Brackets  (Easy)
=================================================================
A stack exposes only the TOP element.
Use a plain Python list as the backing store:
  stack = []
  stack.append(x)     # push
  stack.pop()         # pop  (raises IndexError if empty)
  stack[-1]           # peek
=================================================================
"""

# Return True if every opening bracket in s has a correctly
# matching closing bracket in the right order.
# Ignore all characters that are not brackets.
#
# Bracket pairs:  ( )   [ ]   { }
#
# Example:
#   is_balanced("([]{})")   -> True
#   is_balanced("([)]")     -> False   (wrong order)
#   is_balanced("{[}")      -> False   (wrong pair)
#   is_balanced("(")        -> False   (unclosed)
#   is_balanced("hello()")  -> True    (non-brackets ignored)

def is_balanced(s: str) -> bool:
    """Return True if all brackets in s are correctly matched."""
    # Time  complexity: O(?)
    # Space complexity: O(?)
    # YOUR CODE HERE
    balanced = True
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_pairs[char]:
                balanced = False
                break
            stack.pop()
    if stack:
        balanced = False
    return balanced


# ═════════════════════════════════════════════════════════════
# Tests — run with:  python 03_is_balanced.py
# ═════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== is_balanced ===")
    assert is_balanced("([]{})")  == True,  "FAIL"
    assert is_balanced("([)]")    == False, "FAIL"
    assert is_balanced("{[}")     == False, "FAIL"
    assert is_balanced("")        == True,  "FAIL"
    assert is_balanced("((()))")  == True,  "FAIL"
    assert is_balanced("(")       == False, "FAIL"
    assert is_balanced("hello()") == True,  "FAIL"
    print(f"  '([]{{}})'  -> {is_balanced('([]{})')}")
    print(f"  '([)]'    -> {is_balanced('([)]')}")
    print(f"  '(('      -> {is_balanced('((')}")
    print(f"  'hello()' -> {is_balanced('hello()')}")

    print("\nAll is_balanced tests passed!")
