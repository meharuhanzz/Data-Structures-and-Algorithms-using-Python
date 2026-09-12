"""
Problem: Given an integer array `nums` and integer k, return the
total number of contiguous subarrays whose sum equals k. Array can
contain negative numbers (rules out a simple sliding window).
Source : LeetCode 560 - Subarray Sum Equals K

Example:
    Input:  nums = [1, 1, 1], k = 2
    Output: 2   (subarrays [1,1] at indices [0,1] and [1,2])

Idea: let prefix[i] = sum(nums[0..i]). A subarray (j, i] sums to k
exactly when prefix[i] - prefix[j] == k, i.e. prefix[j] == prefix[i]
- k. So while scanning and building the running prefix sum, count
how many *earlier* prefix sums equal (current prefix - k) using a
dict of prefix-sum -> occurrence count. Seed the dict with {0: 1} to
correctly count subarrays that start at index 0.
"""


def subarray_sum(nums: list[int], k: int) -> int:
    prefix_counts = {0: 1}
    running_sum = 0
    total = 0

    for n in nums:
        running_sum += n
        total += prefix_counts.get(running_sum - k, 0)
        prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1

    return total


if __name__ == "__main__":
    tests = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 0, 0),
        ([1, -1, 0], 0, 3),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        got = subarray_sum(nums, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
