"""
Problem: Given a grid of 1 (land) and 0 (water), return the area of
the largest island (0 if there is none).
Source : LeetCode 695 - Max Area of Island

Example:
    Input:
        [[0,0,1,0,0],
         [0,1,1,1,0],
         [0,0,1,0,0]]
    Output: 5

Idea: identical scan-and-DFS structure to 02, but the DFS now
*returns a value* (the island's size) instead of just marking cells.
Each call contributes 1 for itself plus the sum of what all 4
neighbors contribute - the same "combine children's answers"
recursive shape from the trees topic, just applied to a grid's
implicit graph instead of an explicit tree. Track the best size seen
across all islands found during the scan.
"""


def max_area_of_island(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if grid[r][c] == 0 or (r, c) in visited:
            return 0
        visited.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                best = max(best, dfs(r, c))

    return best


if __name__ == "__main__":
    tests = [
        ([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]], 5),
        ([[0, 0, 0], [0, 0, 0]], 0),
        ([[1, 1], [1, 1]], 4),
    ]

    for i, (grid, expected) in enumerate(tests, 1):
        got = max_area_of_island(grid)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
