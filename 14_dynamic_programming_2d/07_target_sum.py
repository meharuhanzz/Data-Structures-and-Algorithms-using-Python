"""
Problem: Given an array of non-negative integers and a target, assign
a '+' or '-' sign to each number so the resulting expression equals
target. Return the number of ways to do so.
Source : LeetCode 494 - Target Sum

Example:
    Input:  nums = [1, 1, 1, 1, 1], target = 3
    Output: 5

Idea: not obviously a knapsack problem either, but a small algebra
trick reveals it is one. Split nums into a "positive" subset P and a
"negative" subset N (every number goes to exactly one side, based on
its assigned sign). Then sum(P) - sum(N) = target, and also
sum(P) + sum(N) = total (the sum of all numbers, sign-free). Adding
those two equations: 2*sum(P) = target + total, so
sum(P) = (target + total) / 2 - a fixed, computable number. The
problem has been reduced to "how many subsets of nums sum to exactly
sum(P)" - the *counting* version of 06's feasibility knapsack,
counting ways instead of just checking reachability
(`dp[s] += dp[s-n]`, same shape as
`13_dynamic_programming_1d/06_coin_change_ii`, but 0/1 instead of
unbounded, hence the same backward-iteration requirement as 06). The
upfront parity/bounds check (`(total + target) % 2 != 0 or total <
abs(target)`) catches target values no sign assignment could ever
reach, before running the DP at all.
"""


def find_target_sum_ways(nums: list[int], target: int) -> int:
    total = sum(nums)
    if (total + target) % 2 != 0 or total < abs(target):
        return 0

    subset_sum = (total + target) // 2
    dp = [0] * (subset_sum + 1)
    dp[0] = 1

    for n in nums:
        for s in range(subset_sum, n - 1, -1):
            dp[s] += dp[s - n]

    return dp[subset_sum]


if __name__ == "__main__":
    tests = [
        ([1, 1, 1, 1, 1], 3, 5),
        ([1], 1, 1),
        ([1], 2, 0),
        ([1, 0], 1, 2),
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        got = find_target_sum_ways(nums, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
