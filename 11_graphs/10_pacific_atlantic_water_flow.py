"""
Problem: Given a grid of heights representing an island (Pacific
ocean borders the top and left edges, Atlantic borders the bottom
and right edges), water flows from a cell to a 4-directional neighbor
only if the neighbor's height is <= the current height. Return every
cell from which water can reach *both* oceans.
Source : LeetCode 417 - Pacific Atlantic Water Flow

Example:
    Given a 5x5 height grid, return the list of [row, col] cells that
    can reach both the Pacific and Atlantic borders.

Idea: checking "can water starting here reach both oceans" for every
single cell independently would mean running a full flood-fill from
every one of the grid's O(rows*cols) cells - too slow. Reverse the
question instead: start from the ocean borders and ask "which cells
could water flow *backward* into, from here" - since flow requires
non-increasing height forward, flowing backward from an ocean means
walking to neighbors with height >= the current cell (the exact
reverse condition). Running one multi-source DFS/BFS from all
Pacific-adjacent cells marks every cell that can reach the Pacific;
same from all Atlantic-adjacent cells marks Atlantic-reachable cells.
The answer is simply the intersection of those two visited sets -
two multi-source traversals total, not one traversal per cell.
"""


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific: set[tuple[int, int]] = set()
    atlantic: set[tuple[int, int]] = set()

    def dfs(r: int, c: int, visited: set, prev_height: int) -> None:
        if (r, c) in visited:
            return
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if heights[r][c] < prev_height:
            return
        visited.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, visited, heights[r][c])

    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows - 1, c, atlantic, heights[rows - 1][c])
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])

    return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pacific and (r, c) in atlantic]


if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    expected = {(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)}

    got = {(r, c) for r, c in pacific_atlantic(heights)}
    status = "PASS" if got == expected else "FAIL"
    print(f"Test 1: {status} (got {sorted(got)}, expected {sorted(expected)})")
