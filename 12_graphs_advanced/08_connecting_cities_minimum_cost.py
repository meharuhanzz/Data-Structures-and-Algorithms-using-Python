"""
Problem: Given n cities (1 to n) and a list of possible connections
[city1, city2, cost], return the minimum total cost to connect all
cities (directly or indirectly), or -1 if it's impossible.
Source : classic MST problem (LeetCode 1135 - Connecting Cities With
         Minimum Cost, premium; same shape as Min Cost to Connect
         All Points, problem 09 in this folder)

Example:
    Input:  n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
    Output: 6   (use edges 2-3 (cost 1) and 1-2 (cost 5))

Idea: Kruskal's algorithm - build a Minimum Spanning Tree by
considering edges in order from *cheapest to most expensive*,
greedily accepting any edge that connects two currently-separate
components (rejecting one that would connect two nodes already in
the same component, since that would just create a cycle without
adding connectivity). This is 01's Union-Find used for its most
classic purpose: `union()` returning False is precisely "this edge is
redundant," and a spanning tree needs exactly n-1 accepted edges - if
fewer than that get accepted by the time all edges are considered,
some cities are unreachable from others and no valid connection
exists. Sorting once up front (O(E log E)) dominates the total cost;
every union/find after that is near O(1) amortized.
"""


def min_cost_connect_cities(n: int, connections: list[list[int]]) -> int:
    parent = list(range(n + 1))  # cities are 1-indexed

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    connections = sorted(connections, key=lambda edge: edge[2])
    total_cost = 0
    edges_used = 0

    for u, v, cost in connections:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break

    return total_cost if edges_used == n - 1 else -1


if __name__ == "__main__":
    tests = [
        (3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]], 6),
        (4, [[1, 2, 3], [3, 4, 4]], -1),
        (1, [], 0),
    ]

    for i, (n, connections, expected) in enumerate(tests, 1):
        got = min_cost_connect_cities(n, connections)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
