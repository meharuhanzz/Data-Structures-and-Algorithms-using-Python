"""
Problem: n gas stations arranged in a circle; gas[i] is the fuel
available at station i, cost[i] is the fuel needed to travel from
station i to station i+1. Starting with an empty tank, return the
starting station index that allows completing the full circuit, or
-1 if none exists (the answer is guaranteed unique if it exists).
Source : LeetCode 134 - Gas Station

Example:
    Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3

Idea: two greedy facts combine to solve this in one pass. First: a
solution exists at all if and only if `sum(gas) >= sum(cost)` overall
- if the total fuel available can't cover the total cost, no starting
point can possibly work, no matter where the trip begins. Second, and
less obvious: if the tank goes negative starting from station `start`
by the time it reaches station `i`, then *no* station between `start`
and `i` (inclusive) could have been a valid starting point either -
starting anywhere in that stretch only means arriving at each later
station with *less* surplus than starting from `start` did, since
the earlier stations' gas is what's forfeited. So the moment the
running tank goes negative, jump the candidate start straight to
`i + 1` and reset the tank to 0, skipping the need to separately
retry every station in between.
"""


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    total = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0

    return start if total >= 0 else -1


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),
    ]

    for i, (gas, cost, expected) in enumerate(tests, 1):
        got = can_complete_circuit(gas, cost)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
