"""
Problem: A grid contains 0 (empty), 1 (fresh orange), or 2 (rotten
orange). Every minute, every rotten orange rots its 4-directional
fresh neighbors. Return the minimum minutes until no fresh orange
remains, or -1 if that's impossible.
Source : LeetCode 994 - Rotting Oranges

Example:
    Input:
        [[2,1,1],
         [1,1,0],
         [0,1,1]]
    Output: 4

Idea: multi-source BFS - the first pattern in this folder needing a
queue instead of DFS. All initially-rotten oranges start in the
queue *simultaneously* (multiple sources, not one), each tagged with
its rot-time (0 for the initial ones). BFS naturally processes cells
in order of distance-from-a-source, which here directly corresponds
to time-elapsed, so the last cell popped off the queue gives the
total time needed. This is why BFS (not DFS) is required whenever a
problem asks for shortest-path/minimum-time on an unweighted grid or
graph - DFS would explore in the wrong order to track "time" cleanly.
"""

from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while queue:
        r, c, t = queue.popleft()
        minutes = max(minutes, t)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, t + 1))

    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    tests = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
        ([[0, 0, 0]], 0),
    ]

    for i, (grid, expected) in enumerate(tests, 1):
        got = oranges_rotting([row[:] for row in grid])
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
