"""
Problem: Given coin denominations and a target amount, return the
fewest number of coins needed to make that amount (unlimited supply
of each denomination), or -1 if it can't be made exactly.
Source : LeetCode 322 - Coin Change

Example:
    Input:  coins = [1, 2, 5], amount = 11
    Output: 3   (5 + 5 + 1)

Idea: dp[a] = minimum coins to make amount a, built bottom-up from
dp[0] = 0. For every amount from 1 to target, try every coin
denomination as "the last coin used" - if that coin's value fits
(`c <= a`), the best way to make `a` using it last is 1 (for this
coin) plus the best way to make the remaining `a - c`. Take the
minimum over all coin choices. Unlike 04's fixed two predecessors,
each amount here can be reached from *many* possible previous amounts
(one per coin denomination) - the DP array replaces the two rolling
variables from earlier problems because more than a constant number
of prior states matter.
"""


def coin_change(coins: list[int], amount: int) -> int:
    dp = [0] + [float("inf")] * amount

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    tests = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1, 3, 4], 6, 2),
    ]

    for i, (coins, amount, expected) in enumerate(tests, 1):
        got = coin_change(coins, amount)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
