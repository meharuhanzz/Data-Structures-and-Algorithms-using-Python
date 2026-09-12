"""
Problem: Given an integer array `nums`, return an array `output`
where output[i] is the product of every element except nums[i].
Must run in O(n) time, without using division.
Source : LeetCode 238 - Product of Array Except Self

Example:
    Input:  [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

Idea: output[i] = (product of everything to the left of i)
                 * (product of everything to the right of i)
Build the left-products in one left-to-right pass, then fold in the
right-products in one right-to-left pass, reusing the same output
array (so only O(1) *extra* space beyond the output itself).
"""


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([5], [1]),
        ([0, 0], [0, 0]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = product_except_self(inp[:])
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
