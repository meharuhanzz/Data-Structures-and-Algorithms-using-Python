"""
Problem: Given an integer array `nums`, find the contiguous subarray
(containing at least one number) with the largest sum, and return
that sum. Classic intro to Kadane's algorithm / 1D DP-as-single-pass.
Source : LeetCode 53 - Maximum Subarray

Example:
    Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6   (subarray [4, -1, 2, 1])
"""


def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]

    for n in nums[1:]:
        # either extend the running subarray, or start fresh at n -
        # whichever gives a bigger sum ending exactly at this index
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    tests = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
        ([-2, -1], -1),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = max_subarray(inp[:])
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
