"""
Problem: Given a sorted array `nums`, remove duplicates in place so
each unique element appears once. Return k, the number of unique
elements; the first k slots of nums must hold those elements (order
preserved). O(1) extra space, no new list.
Source : LeetCode 26 - Remove Duplicates from Sorted Array

Example:
    Input:  [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: k = 5, nums[:5] == [0, 1, 2, 3, 4]
"""


def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    tests = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([], 0, []),
        ([1], 1, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
    ]

    for i, (inp, expected_k, expected_prefix) in enumerate(tests, 1):
        arr = inp[:]
        k = remove_duplicates(arr)
        got_prefix = arr[:k]
        status = "PASS" if (k == expected_k and got_prefix == expected_prefix) else "FAIL"
        print(f"Test {i}: {status} (k={k}, prefix={got_prefix}, expected k={expected_k}, prefix={expected_prefix})")
