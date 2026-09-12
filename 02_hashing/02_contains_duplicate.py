"""
Problem: Given an integer array `nums`, return True if any value
appears at least twice, False if every element is distinct.
Source : LeetCode 217 - Contains Duplicate

Example:
    Input:  [1, 2, 3, 1]
    Output: True

Idea: a set gives O(1) average membership checks. Walk once; if the
current element is already in the set, a duplicate has been found.
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = contains_duplicate(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
