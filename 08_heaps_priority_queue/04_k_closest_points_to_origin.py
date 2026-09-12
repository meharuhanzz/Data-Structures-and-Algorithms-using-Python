"""
Problem: Given an array of points on the 2D plane and an integer k,
return the k points closest to the origin (0, 0). Any order is
acceptable.
Source : LeetCode 973 - K Closest Points to Origin

Example:
    Input:  points = [[1, 3], [-2, 2]], k = 1
    Output: [[-2, 2]]

Idea: same size-k heap invariant as 02/03, applied to a derived key
(squared Euclidean distance - no need for an actual sqrt, since it's
monotonic and comparisons care only about relative order) instead of
the raw value. This time it's a *max*-heap of size k holding the k
closest points found so far, so the point that's furthest among
those k (the one to evict if something closer shows up) sits at the
root - achieved via the same negate-for-max-heap trick as 01.
"""

import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []

    for x, y in points:
        dist_sq = x * x + y * y
        heapq.heappush(heap, (-dist_sq, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    tests = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ([[0, 1]], 1, [[0, 1]]),
    ]

    for i, (points, k, expected) in enumerate(tests, 1):
        got = k_closest(points, k)
        got_set = sorted(map(tuple, got))
        expected_set = sorted(map(tuple, expected))
        status = "PASS" if got_set == expected_set else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
