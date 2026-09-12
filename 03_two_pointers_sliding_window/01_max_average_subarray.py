"""
Problem: Given an integer array nums and integer k, find the maximum
average value of any contiguous subarray of length k.
Source : LeetCode 643 - Maximum Average Subarray I

Example:
    Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
    Output: 12.75   (subarray [12, -5, -6, 50], sum 51 / 4)

Idea: fixed-size sliding window, the simplest window shape. Compute
the sum of the first k elements once, then slide the window one step
at a time: add the element entering on the right, subtract the one
leaving on the left. Avoids recomputing the sum from scratch at every
position (which would be O(n*k)).
"""


def find_max_average(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


if __name__ == "__main__":
    tests = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([-1], 1, -1.0),
        ([0, 1, 1, 3, 3], 4, 2.0),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        got = find_max_average(nums, k)
        status = "PASS" if abs(got - expected) < 1e-9 else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
