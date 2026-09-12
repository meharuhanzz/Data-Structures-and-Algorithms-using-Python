"""
Problem: Given item weights, item values, and a knapsack capacity,
choose a subset of items (each item used at most once - "0/1"
meaning include-or-don't, no fractions or repeats) that maximizes
total value without exceeding capacity.
Source : classic 0/1 Knapsack (foundational DP problem, underlies
         06 and 07 in this folder)

Example:
    Input:  weights = [1, 3, 4, 5], values = [1, 4, 5, 7], capacity = 7
    Output: 9   (take items of weight 3 and 4, value 4 + 5)

Idea: dp[i][cap] = the best value achievable using only the first i
items, with capacity cap. For each item, there are exactly two
choices: skip it (value = dp[i-1][cap], unchanged) or take it (only
possible if it fits: value = dp[i-1][cap - weight] + value, since
taking it uses up `weight` capacity and this item can't be taken
again - the "0/1" constraint is exactly why the lookup goes to row
i-1, not row i, unlike `13_dynamic_programming_1d/05_coin_change`'s
unbounded version, which reuses row i because coins can repeat).
dp[i][cap] is the better of those two choices. This "skip or take,
constrained by remaining capacity" table is the base every
0/1-knapsack-*shaped* problem (06, 07) reduces down to, even when the
problem statement doesn't mention weights/values/capacity at all.
"""


def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = weights[i - 1], values[i - 1]
        for cap in range(capacity + 1):
            dp[i][cap] = dp[i - 1][cap]
            if weight <= cap:
                dp[i][cap] = max(dp[i][cap], dp[i - 1][cap - weight] + value)

    return dp[n][capacity]


if __name__ == "__main__":
    tests = [
        ([1, 3, 4, 5], [1, 4, 5, 7], 7, 9),
        ([2, 3, 4, 5], [3, 4, 5, 6], 5, 7),
        ([10], [100], 5, 0),
        ([], [], 10, 0),
    ]

    for i, (weights, values, capacity, expected) in enumerate(tests, 1):
        got = knapsack(weights, values, capacity)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
