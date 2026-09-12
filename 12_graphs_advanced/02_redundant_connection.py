"""
Problem: A tree with n nodes had one extra edge added, making it a
graph with exactly one cycle. Given the edges in the order they were
added, return the edge that, if removed, restores a valid tree (if
several edges could be removed, return the one that appears last in
the input).
Source : LeetCode 684 - Redundant Connection

Example:
    Input:  [[1,2], [1,3], [2,3]]
    Output: [2, 3]

Idea: the first direct application of 01's Union-Find. Process edges
in order, union-ing each pair's endpoints. The moment an edge's two
endpoints are *already* in the same set (`find` gives the same root
for both), that edge doesn't connect anything new - it's the one
closing the cycle, and since edges are processed in input order, it's
automatically the last such edge (the answer the problem wants). No
separate cycle-detection DFS needed - Union-Find's own union()
return value *is* the cycle check.
"""


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    parent = list(range(n + 1))  # nodes are 1-indexed

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for a, b in edges:
        root_a, root_b = find(a), find(b)
        if root_a == root_b:
            return [a, b]
        parent[root_a] = root_b

    return []


if __name__ == "__main__":
    tests = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ]

    for i, (edges, expected) in enumerate(tests, 1):
        got = find_redundant_connection(edges)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
