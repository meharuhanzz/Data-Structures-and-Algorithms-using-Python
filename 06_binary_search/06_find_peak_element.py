"""
Problem: A peak element is one strictly greater than its neighbors
(treat out-of-bounds neighbors as -infinity). Given nums (not
necessarily sorted, adjacent elements never equal), find the index
of *any* peak in O(log n).
Source : LeetCode 162 - Find Peak Element

Example:
    Input:  [1, 2, 3, 1]
    Output: 2   (nums[2] = 3 is greater than both neighbors)

Idea: binary search doesn't require full sortedness, only a way to
eliminate half the space each step - here that comes from slope, not
order. Compare nums[mid] to nums[mid+1]: if the slope is downward
(nums[mid] > nums[mid+1]), a peak is guaranteed to exist somewhere at
or to the *left* of mid (values must have risen from -infinity to
get there, so a local max exists on that side). If the slope is
upward, a peak is guaranteed to the *right*. Either way, a peak
provably exists in the kept half, so the search always terminates on
a valid answer.
"""


def find_peak_element(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


def _is_peak(nums: list[int], i: int) -> bool:
    left_ok = i == 0 or nums[i - 1] < nums[i]
    right_ok = i == len(nums) - 1 or nums[i] > nums[i + 1]
    return left_ok and right_ok


if __name__ == "__main__":
    tests = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1],
        [1, 2],
        [2, 1],
    ]

    for i, nums in enumerate(tests, 1):
        idx = find_peak_element(nums)
        status = "PASS" if _is_peak(nums, idx) else "FAIL"
        print(f"Test {i}: {status} (nums={nums}, got index {idx} -> value {nums[idx]})")
