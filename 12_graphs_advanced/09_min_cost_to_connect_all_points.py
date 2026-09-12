"""
Problem: Given n points on a 2D plane, the cost to connect two points
is their Manhattan distance. Return the minimum total cost to connect
all points into one network (every pair of points is implicitly a
possible edge - a complete graph).
Source : LeetCode 1584 - Min Cost to Connect All Points

Example:
    Input:  [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20

Idea: Prim's algorithm - the other classic way to build an MST,
better suited than Kruskal's (08) here specifically because the graph
is *complete* (every pair of points is a potential edge, so listing
all edges up front would be O(n^2) edges to sort). Prim's instead
grows a single tree outward one node at a time: start from any point,
and repeatedly add the cheapest edge connecting the tree-so-far to
any point not yet in it, tracked with a min-heap (same "pop cheapest,
skip if stale/already handled" shape as Dijkstra in 05 - Prim's and
Dijkstra are close cousins, differing only in whether the heap key is
"distance from the source" or "distance from the growing tree").
Distances to unvisited points are computed on demand as each new
point joins the tree, rather than requiring the full edge list
upfront - the reason this fits a complete graph better than Kruskal's.
"""

import heapq


def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, point_index)
    total_cost = 0
    edges_used = 0

    while edges_used < n:
        cost, i = heapq.heappop(min_heap)
        if visited[i]:
            continue
        visited[i] = True
        total_cost += cost
        edges_used += 1

        xi, yi = points[i]
        for j in range(n):
            if not visited[j]:
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(min_heap, (dist, j))

    return total_cost


if __name__ == "__main__":
    tests = [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
        ([[0, 0]], 0),
    ]

    for i, (points, expected) in enumerate(tests, 1):
        got = min_cost_connect_points(points)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
