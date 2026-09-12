"""
Problem: Given a sorted array of distinct integers and a target,
return its index, or -1 if not present.
Source : LeetCode 704 - Binary Search

Example:
    Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4

Idea: the baseline binary search. At each step, comparing the target
to the middle element eliminates *half* the remaining search space,
regardless of which half - that halving is what gives O(log n)
instead of O(n). `left <= right` (not `<`) is correct here because
we're searching for an exact match and need to check the last
remaining single element too.
"""


def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    tests = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([], 1, -1),
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        got = binary_search(nums, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
