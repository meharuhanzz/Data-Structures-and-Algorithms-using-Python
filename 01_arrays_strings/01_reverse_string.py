"""
Problem: Reverse a list of characters in place.
Source : LeetCode 344 - Reverse String

Given a list of characters `s`, reverse it in place using O(1) extra
space (don't return a new list, don't use s[::-1] or list(reversed(s))
- the point is to practice the two-pointer technique by hand).

Example:
    Input:  ['h','e','l','l','o']
    Output: ['o','l','l','e','h']
"""


def reverse_string(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    tests = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        ([], []),
        (["a"], ["a"]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        arr = inp[:]  # copy, since we mutate in place
        reverse_string(arr)
        status = "PASS" if arr == expected else "FAIL"
        print(f"Test {i}: {status} (got {arr}, expected {expected})")
