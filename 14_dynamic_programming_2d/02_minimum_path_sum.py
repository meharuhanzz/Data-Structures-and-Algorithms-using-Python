"""
Problem: Given a grid of non-negative numbers, find a path from
top-left to bottom-right (only moving right or down) that minimizes
the sum of numbers along the path.
Source : LeetCode 64 - Minimum Path Sum

Example:
    Input:  [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7   (path 1 -> 3 -> 1 -> 1 -> 1)

Idea: same shape as 01, `min` instead of `+` for combining the two
possible predecessors, and this time the *cost* of each cell (not
just a count of 1 way per step) has to be folded in. dp[r][c] = the
grid's own cost at (r, c), plus whichever predecessor (above or left)
had the cheaper path to reach it. The first row and column are seeded
by accumulating along the only available direction, same reasoning as
01's "only one way in along an edge," just summing costs instead of
counting paths.
"""


def min_path_sum(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = grid[0][0]
    for c in range(1, cols):
        dp[0][c] = dp[0][c - 1] + grid[0][c]
    for r in range(1, rows):
        dp[r][0] = dp[r - 1][0] + grid[r][0]

    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

    return dp[rows - 1][cols - 1]


if __name__ == "__main__":
    tests = [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
        ([[5]], 5),
    ]

    for i, (grid, expected) in enumerate(tests, 1):
        got = min_path_sum(grid)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
