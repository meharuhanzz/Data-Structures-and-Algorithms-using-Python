"""
Problem: An ugly number is a positive integer whose only prime
factors are 2, 3, and 5. Given n, return the nth ugly number (1 is
conventionally the first).
Source : LeetCode 264 - Ugly Number II

Example:
    Input:  n = 10
    Output: 12   (sequence: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12)

Idea: generate ugly numbers in sorted order using a min-heap instead
of testing every integer for ugliness (which would need factoring
each candidate). Start the heap with 1. Repeatedly pop the smallest
ugly number found so far, and push its three "descendants"
(popped * 2, popped * 3, popped * 5) - each of which is also
necessarily ugly, since it's a product of an ugly number and one of
the three allowed primes. A `seen` set prevents the same value being
pushed multiple times (e.g. 2*3 and 3*2 would otherwise both reach
6). Popping n times gives exactly the nth ugly number.
"""

import heapq


def nth_ugly_number(n: int) -> int:
    heap = [1]
    seen = {1}
    ugly = 1

    for _ in range(n):
        ugly = heapq.heappop(heap)
        for factor in (2, 3, 5):
            candidate = ugly * factor
            if candidate not in seen:
                seen.add(candidate)
                heapq.heappush(heap, candidate)

    return ugly


if __name__ == "__main__":
    tests = [
        (10, 12),
        (1, 1),
        (15, 24),
    ]

    for i, (n, expected) in enumerate(tests, 1):
        got = nth_ugly_number(n)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
