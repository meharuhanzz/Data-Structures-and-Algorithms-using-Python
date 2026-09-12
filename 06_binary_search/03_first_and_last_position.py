"""
Problem: Given a sorted array that may contain duplicates and a
target, return [first_index, last_index] of target's occurrences,
or [-1, -1] if it's not present. O(log n).
Source : LeetCode 34 - Find First and Last Position of Element in
         Sorted Array

Example:
    Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
    Output: [3, 4]

Idea: run a modified binary search twice. On finding a match, don't
stop - record it, then keep searching in the direction that could
find an *earlier* (or later) match: shrink `right` past mid to look
left for the first occurrence, or push `left` past mid to look right
for the last. Each of the two searches is still O(log n), so the
combined cost stays O(log n), not O(n) (which a linear scan out from
a single found index would cost in the worst case of all-duplicates).
"""


def search_range(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first: bool) -> int:
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return [find_bound(True), find_bound(False)]


if __name__ == "__main__":
    tests = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1, 1, 1, 1], 1, [0, 3]),
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        got = search_range(nums, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
