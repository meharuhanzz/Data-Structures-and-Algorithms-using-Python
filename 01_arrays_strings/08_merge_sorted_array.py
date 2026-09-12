"""
Problem: nums1 and nums2 are sorted arrays. nums1 has length m + n:
the first m elements are the real values, the last n are placeholder
zeros with room for nums2's n elements. Merge nums2 into nums1 in
place so nums1 becomes one sorted array of length m + n.
Source : LeetCode 88 - Merge Sorted Array

Example:
    nums1 = [1, 2, 3, 0, 0, 0], m = 3
    nums2 = [2, 5, 6],          n = 3
    -> nums1 becomes [1, 2, 2, 3, 5, 6]

Idea: merging from the front needs shifting (O(n) per insert). Since
nums1 has empty room at the *back*, merge from the back instead:
compare the largest remaining elements of each array and place the
bigger one at the last open slot, working backwards.
"""


def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1          # last real element in nums1
    j = n - 1           # last element in nums2
    k = m + n - 1       # last write position in nums1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([2, 0], 1, [1], 1, [1, 2]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ]

    for i, (nums1, m, nums2, n, expected) in enumerate(tests, 1):
        arr = nums1[:]
        merge_sorted_array(arr, m, nums2, n)
        status = "PASS" if arr == expected else "FAIL"
        print(f"Test {i}: {status} (got {arr}, expected {expected})")
