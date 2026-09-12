"""
Problem: Given an array nums and a window size k, return the maximum
value in each sliding window of size k as it moves left to right.
Source : LeetCode 239 - Sliding Window Maximum

Example:
    Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Output: [3, 3, 5, 5, 6, 7]

Idea: monotonic (decreasing) deque of *indices*. Before adding the
current index, pop any indices from the back whose values are
smaller than the current value - they can never be the max of any
future window while a bigger, more-recent value is also in play, so
they're permanently useless and safe to discard. The front of the
deque is always the index of the current window's maximum; if that
index has fallen outside the window (`dq[0] <= i - k`), pop it from
the front. Combines the monotonic-stack idea from 04/05/06 with a
deque instead of a stack, because elements need to be removed from
*both* ends (back for the "useless smaller values" rule, front for
the "fell out of the window" rule).
"""

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq: deque = deque()  # indices, values decreasing front to back
    result = []

    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)

        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    tests = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        got = max_sliding_window(nums, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
