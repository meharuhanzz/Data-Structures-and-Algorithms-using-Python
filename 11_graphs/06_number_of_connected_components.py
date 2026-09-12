"""
Problem: Given n nodes labeled 0 to n-1 and a list of undirected
edges, return the number of connected components.
Source : LeetCode 323 - Number of Connected Components in an
         Undirected Graph

Example:
    Input:  n = 5, edges = [[0, 1], [1, 2], [3, 4]]
    Output: 2

Idea: 02's island-counting logic, generalized from an implicit grid
graph (neighbors = adjacent cells) to an explicit graph given as an
edge list (neighbors = adjacency list built from those edges). Build
the adjacency list once, then scan every node: whenever an unvisited
node is found, it starts a new component - increment the count and
DFS to mark every node reachable from it. Same "scan + DFS from
unvisited starting points, count how many times a new DFS had to
start" shape as 02, just on a general graph instead of a grid.
"""


def count_components(n: int, edges: list[list[int]]) -> int:
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = set()

    def dfs(node: int) -> None:
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    count = 0
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            count += 1

    return count


if __name__ == "__main__":
    tests = [
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        (4, [], 4),
        (1, [], 1),
    ]

    for i, (n, edges, expected) in enumerate(tests, 1):
        got = count_components(n, edges)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
