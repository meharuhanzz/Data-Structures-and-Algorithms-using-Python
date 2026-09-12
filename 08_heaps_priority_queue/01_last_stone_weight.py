"""
Problem: You're given stone weights. Repeatedly smash the two
heaviest stones together: if equal, both are destroyed; otherwise the
lighter is destroyed and the heavier becomes a new stone with weight
(heavy - light). Return the weight of the last stone left, or 0 if
none remain.
Source : LeetCode 1046 - Last Stone Weight

Example:
    Input:  [2, 7, 4, 1, 8, 1]
    Output: 1

Idea: "repeatedly grab the two largest" is exactly what a max-heap is
for. Python's heapq only implements a *min*-heap, so the standard
trick is to push negated values - the smallest negated value is the
largest original value, which is what heappop then returns. Simulate
directly: pop the two largest, and if they weren't equal, push the
difference back in as a new stone.
"""

import heapq


def last_stone_weight(stones: list[int]) -> int:
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        if first != second:
            heapq.heappush(heap, -(first - second))

    return -heap[0] if heap else 0


if __name__ == "__main__":
    tests = [
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
        ([], 0),
        ([2, 2], 0),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = last_stone_weight(inp[:])
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
