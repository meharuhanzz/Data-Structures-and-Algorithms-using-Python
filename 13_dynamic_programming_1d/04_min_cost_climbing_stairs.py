"""
Problem: Given a cost array where cost[i] is the cost to step on
stair i, and you can start from step 0 or step 1 and move 1 or 2
steps at a time, find the minimum cost to reach the top (one step
past the last index).
Source : LeetCode 746 - Min Cost Climbing Stairs

Example:
    Input:  [10, 15, 20]
    Output: 15   (start at step 1, pay 15, jump 2 steps to the top)

Idea: same rolling-pair shape as 01/02, but the recurrence combines
the prior two states with `min` instead of `max`/`+` - reaching step
i costs whichever is cheaper: coming from step i-1 (pay cost[i-1]) or
from step i-2 (pay cost[i-2]). The "top" is a virtual position one
past the last stair, reached for free once its cheaper predecessor
stair has been paid for - so the loop runs through index n (len(cost))
inclusive, not just to n-1.
"""


def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)
    prev2, prev1 = 0, 0  # cost to reach step 0, cost to reach step 1

    for i in range(2, n + 1):
        curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2, prev1 = prev1, curr

    return prev1


if __name__ == "__main__":
    tests = [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 0, 0, 0], 0),
    ]

    for i, (cost, expected) in enumerate(tests, 1):
        got = min_cost_climbing_stairs(cost)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
