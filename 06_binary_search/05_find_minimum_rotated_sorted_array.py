"""
Problem: A sorted array with distinct values has been rotated at an
unknown pivot. Find the minimum element in O(log n).
Source : LeetCode 153 - Find Minimum in Rotated Sorted Array

Example:
    Input:  [4, 5, 6, 7, 0, 1, 2]
    Output: 0

Idea: the minimum is exactly the "break point" of the rotation - the
one place where a larger value is immediately followed by a smaller
one. Compare nums[mid] to nums[right]: if nums[mid] > nums[right],
the break point (and thus the minimum) must be somewhere to the
*right* of mid, since the right portion contains the wrap-around. If
nums[mid] <= nums[right], the right portion from mid onward is
already sorted, so the minimum is at mid or to its left. Note `mid`
itself is never eliminated in the second branch (`right = mid`, not
`mid - 1`) since mid could BE the minimum.
"""


def find_min(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


if __name__ == "__main__":
    tests = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = find_min(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
