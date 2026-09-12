"""
Problem: Given an n x n adjacency matrix is_connected where
is_connected[i][j] = 1 means cities i and j are directly connected,
return the number of provinces (connected groups of cities).
Source : LeetCode 547 - Number of Provinces

Example:
    Input:  [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

Idea: `11_graphs/06_number_of_connected_components` solved this exact
question with DFS. Here it's solved with Union-Find instead, to make
the comparison concrete: union every directly-connected pair, then
the number of *distinct roots* remaining across all nodes is the
number of provinces. Both approaches are O(n^2) here (the matrix
itself forces an O(n^2) scan), so this problem doesn't demonstrate a
speed advantage for Union-Find - it's here to build the pattern-
matching instinct for recognizing "count connected components" as a
Union-Find-shaped problem, not just a DFS-shaped one.
"""


def find_circle_num(is_connected: list[list[int]]) -> int:
    n = len(is_connected)
    parent = list(range(n))

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> None:
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                union(i, j)

    return len({find(i) for i in range(n)})


if __name__ == "__main__":
    tests = [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
    ]

    for i, (matrix, expected) in enumerate(tests, 1):
        got = find_circle_num(matrix)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
