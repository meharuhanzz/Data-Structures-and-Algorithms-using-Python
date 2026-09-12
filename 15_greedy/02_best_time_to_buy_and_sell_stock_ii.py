"""
Problem: Given daily stock prices, find the maximum profit achievable
with as many buy/sell transactions as you like (must sell before
buying again, no holding two positions at once).
Source : LeetCode 122 - Best Time to Buy and Sell Stock II

Example:
    Input:  [7, 1, 5, 3, 6, 4]
    Output: 7   (buy at 1, sell at 5: +4; buy at 3, sell at 6: +3)

Idea: unlike `01_arrays_strings/07_best_time_to_buy_sell_stock`
(single transaction only), unlimited transactions turn this into a
greedy one-liner: capture *every* positive day-to-day price increase
as its own tiny transaction. This is provably equivalent to the
optimal answer - any longer buy-low-sell-high stretch decomposes
exactly into the sum of its individual daily gains anyway (buying at
the start and selling at the end of an upward run gives the same
total as buying/selling at every up-day along the way), so there's no
benefit to trying to identify longer runs explicitly.
"""


def max_profit(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


if __name__ == "__main__":
    tests = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
    ]

    for i, (prices, expected) in enumerate(tests, 1):
        got = max_profit(prices)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
