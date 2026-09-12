"""
Problem: A robot starts at the top-left of an m x n grid and can only
move right or down. Return the number of distinct paths to the
bottom-right corner.
Source : LeetCode 62 - Unique Paths

Example:
    Input:  m = 3, n = 7
    Output: 28

Idea: the simplest possible 2D DP - dp[r][c] = number of ways to
reach cell (r, c). Every cell can only be entered from directly above
or directly left (the only two allowed moves), so the number of ways
to reach it is simply the sum of the ways to reach those two
neighbors: dp[r][c] = dp[r-1][c] + dp[r][c-1]. The entire first row
and first column are seeded with 1 (there's exactly one way to reach
any cell along an edge - keep moving in the only direction available)
rather than needing a special case in the main loop.
"""


def unique_paths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    tests = [
        (3, 7, 28),
        (3, 2, 3),
        (1, 1, 1),
        (7, 3, 28),
    ]

    for i, (m, n, expected) in enumerate(tests, 1):
        got = unique_paths(m, n)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
