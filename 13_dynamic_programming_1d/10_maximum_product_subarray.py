"""
Problem: Given an integer array nums, find the contiguous subarray
with the largest product, and return that product.
Source : LeetCode 152 - Maximum Product Subarray

Example:
    Input:  [2, 3, -2, 4]
    Output: 6   (subarray [2, 3])

Idea: looks like `01_arrays_strings/04_max_subarray` (Kadane's
algorithm) with multiplication instead of addition, but that
substitution alone is broken - a single running "best product ending
here" isn't enough, because a *very negative* running product can
become the new *maximum* the instant it's multiplied by another
negative number. The fix: track both a running max and a running min
product ending at each position. At every step, the new max is the
best of (current element alone, running max * current element,
running min * current element) - that third option is what correctly
captures "two negatives about to cancel out into a big positive."
The running min needs the same three-way comparison, symmetrically,
since a small-but-currently-minimal product could itself flip into
the new maximum on the *next* step if another negative shows up.
"""


def max_product(nums: list[int]) -> int:
    result = nums[0]
    curr_max = curr_min = nums[0]

    for n in nums[1:]:
        candidates = (n, curr_max * n, curr_min * n)
        curr_max = max(candidates)
        curr_min = min(candidates)
        result = max(result, curr_max)

    return result


if __name__ == "__main__":
    tests = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2, 3, -4], 24),
        ([5], 5),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = max_product(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
