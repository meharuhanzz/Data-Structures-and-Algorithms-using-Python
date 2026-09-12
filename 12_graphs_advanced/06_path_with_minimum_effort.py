"""
Problem: Given a grid of heights, find a path from the top-left to
the bottom-right (4-directional moves) that minimizes the *maximum*
absolute height difference between any two consecutive cells along
the path. Return that minimized maximum difference.
Source : LeetCode 1631 - Path With Minimum Effort

Example:
    Input:  [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2

Idea: a "minimax" variant of Dijkstra - instead of summing edge
weights along the path (like 05), the cost of a path is its single
*worst* step, and the goal is to minimize that worst step across all
possible paths. The algorithm structure barely changes: still a
min-heap keyed by the best-known cost to reach each cell, still
relaxing neighbors and pushing improvements. The one change is the
relaxation formula itself - `new_cost = max(current_cost,
abs(height_diff))` instead of `current_cost + weight` - because
extending a path by one step doesn't accumulate effort, it only
raises the effort if this new step is worse than every step so far.
This same swap (replace `+` with `max` in the relaxation) turns
Dijkstra into a minimax-shortest-path algorithm for any problem
framed as "minimize the worst edge on the path" instead of "minimize
the total path weight."
"""

import heapq


def minimum_effort_path(heights: list[list[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    effort = [[float("inf")] * cols for _ in range(rows)]
    effort[0][0] = 0
    heap = [(0, 0, 0)]  # (effort_so_far, row, col)

    while heap:
        e, r, c = heapq.heappop(heap)
        if e > effort[r][c]:
            continue
        if r == rows - 1 and c == cols - 1:
            return e
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_effort = max(e, abs(heights[nr][nc] - heights[r][c]))
                if new_effort < effort[nr][nc]:
                    effort[nr][nc] = new_effort
                    heapq.heappush(heap, (new_effort, nr, nc))

    return 0


if __name__ == "__main__":
    tests = [
        ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
        ([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1),
        ([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1],
          [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]], 0),
    ]

    for i, (heights, expected) in enumerate(tests, 1):
        got = minimum_effort_path(heights)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
