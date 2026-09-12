"""
Problem: Given coin denominations and a target amount, return the
number of distinct *combinations* of coins that make up that amount
(order doesn't matter - using a 1 then a 2 is the same combination as
a 2 then a 1, so both shouldn't be counted separately).
Source : LeetCode 518 - Coin Change II

Example:
    Input:  amount = 5, coins = [1, 2, 5]
    Output: 4   ({5}, {2,2,1}, {2,1,1,1}, {1,1,1,1,1})

Idea: same dp[a]-over-amounts idea as 05, counting instead of
minimizing (dp[a] += dp[a-c] instead of dp[a] = min(...)), but the
loop order is now the entire point of the problem, not a stylistic
choice. Coins must be the *outer* loop, amounts the inner loop:
processing one coin denomination fully (updating dp for every amount)
before moving to the next coin means, by the time coin c2 is being
considered, dp[a] already reflects "ways using only coins seen so
far" - so a combination like {1, 2} only ever gets counted once (built
in the order the coins loop visits them), never once as "1 then 2"
and again as "2 then 1". Swapping the loop order (amount outer, coin
inner - as in 05) instead counts *permutations*, a different
question entirely; this is the single most important detail to get
right in this problem, and worth being able to explain, not just
recite.
"""


def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]

    return dp[amount]


if __name__ == "__main__":
    tests = [
        (5, [1, 2, 5], 4),
        (3, [2], 0),
        (10, [10], 1),
        (0, [1, 2], 1),
    ]

    for i, (amount, coins, expected) in enumerate(tests, 1):
        got = change(amount, coins)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
