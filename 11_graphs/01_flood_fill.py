"""
Problem: Given an image (2D grid of colors) and a starting pixel
(sr, sc), change the color of that pixel and every pixel connected to
it (4-directionally) that shares its *original* color, to a new
color.
Source : LeetCode 733 - Flood Fill

Example:
    Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
    Output: [[2,2,2],[2,2,0],[2,0,1]]

Idea: the simplest possible grid DFS, and the template every other
grid problem in this folder builds on. Recurse to the 4 neighbors,
but only continue into a cell if it's in bounds *and* still has the
original color - both conditions belong in one guard clause at the
top of the recursive call, so every call site (all 4 directions) gets
the same bounds/color check for free rather than repeating it before
each recursive call. The check for `original == color` up front
prevents infinite recursion in the edge case where the fill color
equals the starting color already.
"""


def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    original = image[sr][sc]
    if original == color:
        return image

    rows, cols = len(image), len(image[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


if __name__ == "__main__":
    tests = [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2,
         [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0,
         [[0, 0, 0], [0, 0, 0]]),
        ([[1]], 0, 0, 3, [[3]]),
    ]

    for i, (image, sr, sc, color, expected) in enumerate(tests, 1):
        got = flood_fill([row[:] for row in image], sr, sc, color)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
