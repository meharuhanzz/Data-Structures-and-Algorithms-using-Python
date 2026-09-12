"""
Problem: Given n cities and weighted undirected edges, find the city
that has the smallest number of *other* cities reachable within
distance_threshold. If tied, return the city with the largest index.
Source : LeetCode 1334 - Find the City With the Smallest Number of
         Neighbors at a Threshold Distance

Example:
    Input:  n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],
            distance_threshold=4
    Output: 3

Idea: 05's Dijkstra and 07's Bellman-Ford both find shortest paths
*from a single source*. This problem needs shortest paths *between
every pair* of cities (to count, for each city, how many others are
reachable) - running Dijkstra n separate times (once per city) would
work, but Floyd-Warshall solves all pairs at once with a different
approach: a dist[i][j] matrix, initialized directly from the edges,
then repeatedly improved by asking "does routing through city k make
i to j shorter?" (`dist[i][j] = min(dist[i][j], dist[i][k] +
dist[k][j])`) for every possible intermediate city k, one k at a
time, over the *entire* matrix. After considering all n candidate
intermediate cities, dist[i][j] is guaranteed to be the true shortest
path, since any shortest path's full sequence of intermediate cities
will have been "discovered" by the time every single city has been
tried as an intermediate hop. The O(n^3) cost is the trade-off for
getting every pair's answer in one pass instead of n separate
single-source runs.
"""


def find_the_city(n: int, edges: list[list[int]], distance_threshold: int) -> int:
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    best_city = -1
    best_count = float("inf")
    for i in range(n):
        count = sum(1 for j in range(n) if i != j and dist[i][j] <= distance_threshold)
        if count <= best_count:
            best_count = count
            best_city = i

    return best_city


if __name__ == "__main__":
    tests = [
        (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4, 3),
        (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2, 0),
    ]

    for i, (n, edges, threshold, expected) in enumerate(tests, 1):
        got = find_the_city(n, edges, threshold)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
