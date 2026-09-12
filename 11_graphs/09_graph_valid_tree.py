"""
Problem: Given n nodes labeled 0 to n-1 and a list of undirected
edges, determine if these edges form a valid tree (connected, and no
cycles).
Source : LeetCode 261 - Graph Valid Tree

Example:
    Input:  n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: True

    Input:  n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: False  (1-2-3-1 is a cycle)

Idea: a tree with n nodes has exactly n-1 edges, and any connected
graph with exactly n-1 edges is automatically acyclic (and vice
versa) - so checking the edge count up front is a cheap O(1) filter
that rules out most invalid cases before any traversal. What's left
to verify is connectivity, via DFS from node 0: track the `parent`
each node was reached from, and treat re-encountering an *already
visited, non-parent* neighbor as a cycle (revisiting the parent
itself is expected and fine in an undirected graph - the edge back to
where you came from isn't a real cycle, just how undirected edges
work). If the DFS completes without finding a cycle and reaches every
node, it's a valid tree.
"""


def valid_tree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = set()

    def dfs(node: int, parent: int) -> bool:
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return False
            if not dfs(neighbor, node):
                return False
        return True

    if not dfs(0, -1):
        return False

    return len(visited) == n


if __name__ == "__main__":
    tests = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
        (4, [[0, 1], [2, 3]], False),
        (1, [], True),
    ]

    for i, (n, edges, expected) in enumerate(tests, 1):
        got = valid_tree(n, edges)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
