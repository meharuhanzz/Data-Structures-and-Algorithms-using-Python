"""
Problem: Given two integer arrays, return their intersection - each
element in the result must be unique, order doesn't matter.
Source : LeetCode 349 - Intersection of Two Arrays

Example:
    Input:  nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    Output: [2]

Idea: convert both arrays to sets and use set intersection directly -
this is the hashing topic's version of "know when the stdlib
operation already IS the optimal algorithm." Set intersection is
O(min(len(a), len(b))) on average.
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    tests = [
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([], [1, 2, 3], []),
    ]

    for i, (nums1, nums2, expected) in enumerate(tests, 1):
        got = sorted(intersection(nums1, nums2))
        status = "PASS" if got == sorted(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {sorted(expected)})")
