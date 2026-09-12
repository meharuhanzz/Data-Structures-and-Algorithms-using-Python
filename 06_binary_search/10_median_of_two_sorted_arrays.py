"""
Problem: Given two sorted arrays nums1, nums2, return the median of
the combined sorted array, in O(log(min(m, n))) time.
Source : LeetCode 4 - Median of Two Sorted Arrays

Example:
    Input:  nums1 = [1, 3], nums2 = [2]
    Output: 2.0

    Input:  nums1 = [1, 2], nums2 = [3, 4]
    Output: 2.5

Idea: the hardest problem in this folder. Merging the two arrays and
taking the middle would be O(m+n) - too slow for the required
O(log(min(m,n))). Instead, binary search for a *partition point* `i`
in the smaller array (always search the smaller one, for efficiency):
given `i`, the corresponding partition `j` in the other array is
forced (`j = half - i`, where half is how many elements the
"left side" of the combined median split needs). A valid partition
requires every element left of the cut to be <= every element right
of the cut, across *both* arrays simultaneously - checked with 4
border values (left_a, right_a, left_b, right_b). If left_a > right_b,
the partition in nums1 needs to move left; if left_b > right_a, it
needs to move right. This is binary searching over partition
positions, not over values - a third distinct "shape" of binary
search alongside the array-index searches (01-07) and the
answer-space searches (08-09).
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    half = (m + n + 1) // 2

    while left <= right:
        i = (left + right) // 2
        j = half - i

        left_a = nums1[i - 1] if i > 0 else float("-inf")
        right_a = nums1[i] if i < m else float("inf")
        left_b = nums2[j - 1] if j > 0 else float("-inf")
        right_b = nums2[j] if j < n else float("inf")

        if left_a <= right_b and left_b <= right_a:
            if (m + n) % 2 == 1:
                return float(max(left_a, left_b))
            return (max(left_a, left_b) + min(right_a, right_b)) / 2
        elif left_a > right_b:
            right = i - 1
        else:
            left = i + 1

    raise ValueError("Input arrays must be sorted")


if __name__ == "__main__":
    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([0, 0], [0, 0], 0.0),
    ]

    for i, (a, b, expected) in enumerate(tests, 1):
        got = find_median_sorted_arrays(a, b)
        status = "PASS" if abs(got - expected) < 1e-9 else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
