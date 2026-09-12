"""
Problem: Given an integer array nums and integer k, return the kth
largest element (kth largest, not kth distinct).
Source : LeetCode 215 - Kth Largest Element in an Array

Example:
    Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5

Idea: sorting the whole array is O(n log n). Instead, maintain a
*min*-heap of exactly size k containing the k largest values seen so
far - its smallest element (the heap's root) is then, by definition,
the kth largest overall. Seed the heap with the first k elements,
then for every remaining element: if it's bigger than the heap's
smallest, it belongs in the top-k and should replace that smallest
element (`heapreplace` does pop+push in one O(log k) operation).
Total cost O(n log k), better than a full sort when k is small.
"""

import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)

    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)

    return heap[0]


if __name__ == "__main__":
    tests = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        got = find_kth_largest(nums, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
