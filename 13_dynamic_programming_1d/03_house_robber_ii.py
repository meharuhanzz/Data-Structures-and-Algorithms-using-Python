"""
Problem: Same as 02, but the houses are arranged in a circle (the
first and last houses are also adjacent).
Source : LeetCode 213 - House Robber II

Example:
    Input:  [2, 3, 2]
    Output: 3   (robbing both house 0 and house 2 isn't allowed -
                  they're adjacent in the circle - so the best is
                  just house 1 alone)

Idea: the circular adjacency between first and last house is the
only thing standing between this and 02's exact solution. Rather
than writing new DP logic to handle that wraparound case directly,
sidestep it: a valid robbery plan on a circle can never include
*both* the first and last house, so it must fit entirely within
either "all houses except the last" or "all houses except the first"
- two ordinary *linear* (non-circular) subproblems, each solvable
with 02's unchanged logic. The answer is just the better of those two
results. This "reduce a harder variant to two calls of the easier
version" move is a common way to handle a small structural wrinkle
(circularity, here) without rederiving the whole recurrence.
"""


def rob_linear(houses: list[int]) -> int:
    prev2, prev1 = 0, 0
    for n in houses:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1


def rob_circular(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    tests = [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
        ([5], 5),
        ([1, 3, 1, 3, 100], 103),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = rob_circular(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
