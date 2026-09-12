"""
Problem: Given a positive-integer array nums and a positive integer
target, return the minimal length of a contiguous subarray whose sum
is >= target. Return 0 if no such subarray exists.
Source : LeetCode 209 - Minimum Size Subarray Sum

Example:
    Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
    Output: 2   (subarray [4, 3])

Idea: variable-size window, but shrinking instead of growing to find
the extreme. Grow the window by moving `right` and adding to a
running sum; whenever the sum is already >= target, that's a
candidate window, so shrink from the left (removing elements, moving
`left` forward) for as long as the sum stays >= target, recording the
window length at every valid shrink step.
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    total = 0
    min_len = float("inf")

    for right, n in enumerate(nums):
        total += n
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float("inf") else min_len


if __name__ == "__main__":
    tests = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
    ]

    for i, (target, nums, expected) in enumerate(tests, 1):
        got = min_subarray_len(target, nums)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
