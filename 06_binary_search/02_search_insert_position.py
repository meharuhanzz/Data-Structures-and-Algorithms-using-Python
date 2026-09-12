"""
Problem: Given a sorted array of distinct integers and a target,
return the index where target is found, or the index where it would
be inserted to keep the array sorted.
Source : LeetCode 35 - Search Insert Position

Example:
    Input:  nums = [1, 3, 5, 6], target = 5
    Output: 2   (found at index 2)

    Input:  nums = [1, 3, 5, 6], target = 2
    Output: 1   (would be inserted between 1 and 3)

Idea: this is a "find the first index where nums[i] >= target"
search, a different shape from 01's exact-match search - notice
`right` starts at `len(nums)` (a valid insert position, one past the
last element) rather than `len(nums) - 1`, and the loop uses
`left < right` with `right = mid` (not `mid - 1`) since mid might
itself be the answer and must stay in play. This left-boundary
template is the basis for 03's first/last-occurrence search too.
"""


def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    tests = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([], 5, 0),
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        got = search_insert(nums, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
