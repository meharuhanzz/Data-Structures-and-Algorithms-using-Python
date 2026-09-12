"""
Problem: Given an array `nums` with only values 0, 1, 2 (representing
red, white, blue), sort it in place in one pass, without using a
library sort. (Dutch National Flag problem.)
Source : LeetCode 75 - Sort Colors

Example:
    Input:  [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

Idea: three-pointer partition instead of a two-pointer mirror. `low`
and `mid` start at the front, `high` at the back.
- Everything before `low` is known to be 0.
- Everything from `low` to `mid-1` is known to be 1.
- Everything after `high` is known to be 2.
- `mid` is the current element being classified.
A 0 at `mid` swaps to the `low` boundary and both advance (the
swapped-in value at `mid` is already known-good, a 1, since region
[low, mid) was all 1s - safe to move mid too). A 2 swaps to the
`high` boundary and only `high` shrinks, because the value swapped in
from `high` hasn't been classified yet and still needs to be checked.
"""


def sort_colors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


if __name__ == "__main__":
    tests = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        arr = inp[:]
        sort_colors(arr)
        status = "PASS" if arr == expected else "FAIL"
        print(f"Test {i}: {status} (got {arr}, expected {expected})")
