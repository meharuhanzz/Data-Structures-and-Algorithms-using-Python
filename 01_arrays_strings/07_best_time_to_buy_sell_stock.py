"""
Problem: Given an array `prices` where prices[i] is the stock price
on day i, find the maximum profit from a single buy followed by a
single sell (buy must happen before sell). Return 0 if no profit is
possible. Single pass, O(1) extra space.
Source : LeetCode 121 - Best Time to Buy and Sell Stock

Example:
    Input:  [7, 1, 5, 3, 6, 4]
    Output: 5   (buy at 1, sell at 6)
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for p in prices[1:]:
        best_profit = max(best_profit, p - min_price)
        min_price = min(min_price, p)

    return best_profit


if __name__ == "__main__":
    tests = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
        ([], 0),
        ([5], 0),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = max_profit(inp[:])
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
