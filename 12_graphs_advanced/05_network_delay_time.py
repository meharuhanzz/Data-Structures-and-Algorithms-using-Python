"""
Problem: A network has n nodes (1 to n) and directed weighted edges
times = [[u, v, w], ...] meaning a signal takes w time to travel from
u to v. Given a starting node k, return the time for a signal sent
from k to reach every node (the time when the *last* node receives
it), or -1 if some node is unreachable.
Source : LeetCode 743 - Network Delay Time

Example:
    Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2

Idea: the canonical Dijkstra's algorithm - single-source shortest
paths on a graph with non-negative weights. A min-heap always pops
the currently-closest unfinalized node next, guaranteeing that by the
time a node is popped, its `dist` value is already the true shortest
distance to it (any other path to it would have to go through a node
that's farther away, which can't produce a shorter result with
non-negative weights - this is exactly why Dijkstra breaks with
negative edges, and why 07's Bellman-Ford exists as the fallback for
that case). The `if d > dist[node]: continue` guard skips stale heap
entries left over from a node being reached via a worse path earlier,
before a better path to it was later found and pushed again.
"""

import heapq


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        adj[u].append((v, w))

    dist = {i: float("inf") for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    max_dist = max(dist.values())
    return max_dist if max_dist < float("inf") else -1


if __name__ == "__main__":
    tests = [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ]

    for i, (times, n, k, expected) in enumerate(tests, 1):
        got = network_delay_time(times, n, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
