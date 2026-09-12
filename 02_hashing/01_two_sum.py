"""
Problem: Given an array of integers `nums` and an integer `target`,
return the indices of the two numbers that add up to target. Exactly
one solution exists; can't use the same element twice.
Source : LeetCode 1 - Two Sum

Example:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]   (2 + 7 == 9)

Idea: brute force is O(n^2) checking every pair. Instead, walk once
and for each number ask "have I already seen its complement
(target - n)?" via a dict — turns the lookup into O(1) amortized.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index

    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i

    return []


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        got = two_sum(nums, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
