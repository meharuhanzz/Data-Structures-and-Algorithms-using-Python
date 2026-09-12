"""
Problem: Given a string containing just '(', ')', '{', '}', '[', ']',
determine if the brackets are validly matched and nested.
Source : LeetCode 20 - Valid Parentheses

Example:
    Input:  "{[]}"
    Output: True

Idea: the defining property of a stack (last-in-first-out) matches
exactly how nested brackets must close - the most recently opened
bracket must be the next one closed. Push opening brackets; on a
closing bracket, it must match whatever is on top of the stack right
now, or the string is invalid. A leftover non-empty stack at the end
means something was opened but never closed.
"""


def is_valid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack


if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = is_valid(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
