"""
Problem: Given the amount of money at each house along a street,
find the maximum amount that can be robbed without robbing two
adjacent houses.
Source : LeetCode 198 - House Robber

Example:
    Input:  [1, 2, 3, 1]
    Output: 4   (rob house 0 and house 2: 1 + 3)

Idea: at each house, there are exactly two choices - skip it (best
so far is whatever the best was up to the previous house), or rob it
(this house's value plus the best achievable up to *two* houses ago,
since the immediately preceding house can't also be robbed). The
"best up to here" only ever depends on the best-up-to-previous and
best-up-to-two-before, the same rolling-pair shape as 01's `climb_
stairs`, just with `max` combining the two prior states through an
adjacency constraint instead of adding them unconditionally.
"""


def rob(nums: list[int]) -> int:
    prev2, prev1 = 0, 0  # best up to two houses ago, best up to previous house

    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)

    return prev1


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([], 0),
        ([5], 5),
        ([2, 1, 1, 2], 4),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = rob(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
