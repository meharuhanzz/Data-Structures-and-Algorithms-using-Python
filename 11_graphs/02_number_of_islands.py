"""
Problem: Given a grid of '1' (land) and '0' (water), return the
number of islands (maximal 4-directionally connected groups of land).
Source : LeetCode 200 - Number of Islands

Example:
    Input:
        11110
        11010
        11000
        00000
    Output: 1

Idea: this is 01's flood fill technique used to *count connected
components* rather than to recolor them. Scan every cell; whenever
land is found that hasn't been visited yet, it's the start of a new
island - increment the count and DFS outward marking every reachable
land cell as visited, so the same island is never counted again from
one of its other cells later in the scan. A `visited` set (rather
than mutating the grid itself, as 01 does) keeps the input
unmodified, which matters here since nothing about "counting" implies
permission to change the input.
"""


def num_islands(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == "0" or (r, c) in visited:
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                dfs(r, c)

    return count


if __name__ == "__main__":
    tests = [
        ([
            list("11110"),
            list("11010"),
            list("11000"),
            list("00000"),
        ], 1),
        ([
            list("11000"),
            list("11000"),
            list("00100"),
            list("00011"),
        ], 3),
        ([list("0")], 0),
    ]

    for i, (grid, expected) in enumerate(tests, 1):
        got = num_islands(grid)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
