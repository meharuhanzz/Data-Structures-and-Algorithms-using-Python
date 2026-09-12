"""
Problem: Rotate an array to the right by k steps, in place, using
O(1) extra space. Solved with the "three reversals" trick.
Source : LeetCode 189 - Rotate Array

Example:
    Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]

Idea: reversing the whole array puts the last k elements at the
front (but each half is internally backwards), then reversing each
half individually fixes the internal order.
    [1,2,3,4,5,6,7]
    -> reverse all:        [7,6,5,4,3,2,1]
    -> reverse first k:    [5,6,7,4,3,2,1]
    -> reverse remaining:  [5,6,7,1,2,3,4]
"""


def _reverse(nums: list[int], left: int, right: int) -> None:
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotate_array(nums: list[int], k: int) -> None:
    n = len(nums)
    if n == 0:
        return

    k %= n
    _reverse(nums, 0, n - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, n - 1)


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2], 3, [2, 1]),
        ([1], 0, [1]),
        ([], 5, []),
    ]

    for i, (inp, k, expected) in enumerate(tests, 1):
        arr = inp[:]
        rotate_array(arr, k)
        status = "PASS" if arr == expected else "FAIL"
        print(f"Test {i}: {status} (got {arr}, expected {expected})")
