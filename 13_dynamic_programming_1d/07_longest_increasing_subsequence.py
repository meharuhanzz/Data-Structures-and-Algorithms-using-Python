"""
Problem: Given an integer array nums, return the length of the
longest strictly increasing subsequence (elements don't need to be
contiguous, just in increasing order and in their original relative
order).
Source : LeetCode 300 - Longest Increasing Subsequence

Example:
    Input:  [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4   (the subsequence [2, 3, 7, 101])

Idea: dp[i] = length of the longest increasing subsequence *ending
exactly at index i*. For each i, check every earlier index j: if
nums[j] < nums[i], then i could extend whatever subsequence ends at
j, giving a candidate length dp[j] + 1. Taking the best such
candidate over all valid j (or just 1, if no earlier element is
smaller - the subsequence containing just nums[i] itself) gives
dp[i]. The answer is the best dp[i] across the whole array, not
necessarily dp[n-1], since the longest subsequence doesn't have to
end at the last element. This is O(n^2) - there's a well-known
O(n log n) alternative using binary search (patience sorting), but
the O(n^2) version here is the one to have completely solid first,
since it's what most interviewers expect to see derived live.
"""


def length_of_lis(nums: list[int]) -> int:
    if not nums:
        return 0

    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
        ([], 0),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = length_of_lis(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
