"""
Problem: Design a class that, given an initial array and integer k,
supports add(val) - adding a new value to the stream and returning
the kth largest element among all values added so far (including the
initial array).
Source : LeetCode 703 - Kth Largest Element in a Stream

Example:
    kth = KthLargest(3, [4, 5, 8, 2])
    kth.add(3)   -> 4
    kth.add(5)   -> 5
    kth.add(10)  -> 5
    kth.add(9)   -> 8
    kth.add(4)   -> 8

Idea: the streaming version of 02 - same size-k min-heap invariant
(heap always holds exactly the k largest values seen so far, root is
the kth largest), but now the heap needs to *persist* across calls
instead of being built once. Every add() just pushes the new value
and, if that grows the heap past size k, pops the smallest -
O(log k) per call, rather than re-running a fresh O(n log k) pass
over the whole history each time.
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    ops = [
        (kth.add, (3,), 4),
        (kth.add, (5,), 5),
        (kth.add, (10,), 5),
        (kth.add, (9,), 8),
        (kth.add, (4,), 8),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (add{args} -> got {got}, expected {expected})")
