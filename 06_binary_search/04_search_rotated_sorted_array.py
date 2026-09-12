"""
Problem: An array, originally sorted ascending with distinct values,
has been rotated at some unknown pivot. Given the rotated array and
a target, find its index in O(log n), or -1 if absent.
Source : LeetCode 33 - Search in Rotated Sorted Array

Example:
    Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

Idea: the array as a whole isn't sorted, but at every step, *at
least one* of the two halves around `mid` is guaranteed to be a
contiguous sorted run (rotation only breaks sortedness at one point).
Figure out which half is sorted by comparing nums[left] to nums[mid];
if target falls within that sorted half's value range, search there;
otherwise it must be in the other half. Either way, half the search
space is eliminated every step, preserving O(log n).
"""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:  # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    tests = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([3, 1], 1, 1),
        ([5, 1, 3], 5, 0),
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        got = search(nums, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
