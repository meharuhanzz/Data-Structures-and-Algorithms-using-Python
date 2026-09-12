"""
Problem: Given n cities, directed weighted flight routes, a source,
a destination, and a maximum of k stops (k+1 flights) allowed, return
the cheapest price to get from source to destination within that
limit, or -1 if impossible.
Source : LeetCode 787 - Cheapest Flights Within K Stops

Example:
    Input:  n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
            src=0, dst=3, k=1
    Output: 700   (0 -> 1 -> 3, exactly 1 stop, cost 100+600)

Idea: Dijkstra (05) always finds the *unconstrained* cheapest path,
which could use more stops than allowed here - so it doesn't
directly apply. Bellman-Ford instead relaxes *every* edge, for
exactly k+1 rounds (one round per flight allowed) - round i finds
the cheapest cost reachable using at most i flights. The critical
detail: each round must relax edges using a *snapshot* of the
previous round's distances (`new_dist = dist[:]`, updated separately,
then swapped in after the round), not the array being mutated live -
otherwise a single round could accidentally chain multiple edge
relaxations together, effectively using more flights than that round
is allowed to represent. This snapshot-per-round requirement is
exactly what caps the path length at k+1 edges, which is the whole
reason Bellman-Ford (not Dijkstra) is the right tool whenever a
shortest-path problem comes with a limit on the number of edges used.
"""


def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    dist = [float("inf")] * n
    dist[src] = 0

    for _ in range(k + 1):
        new_dist = dist[:]
        for u, v, w in flights:
            if dist[u] != float("inf") and dist[u] + w < new_dist[v]:
                new_dist[v] = dist[u] + w
        dist = new_dist

    return dist[dst] if dist[dst] != float("inf") else -1


if __name__ == "__main__":
    tests = [
        (4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1, 700),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    ]

    for i, (n, flights, src, dst, k, expected) in enumerate(tests, 1):
        got = find_cheapest_price(n, flights, src, dst, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
