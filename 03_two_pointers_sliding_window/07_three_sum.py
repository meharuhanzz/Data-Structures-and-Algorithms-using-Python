"""
Problem: Given an integer array nums, return all unique triplets
[a, b, c] such that a + b + c == 0. No duplicate triplets in the
result.
Source : LeetCode 15 - 3Sum

Example:
    Input:  [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Idea: sort first. Fix one element (nums[i]), then the remaining
"find two numbers that sum to -nums[i]" is exactly the converging
two-pointer from 06_two_sum_sorted, run once per choice of i. Sorting
also makes duplicate-skipping trivial (identical values end up
adjacent, so just compare to the previous element/pointer position).
Break early once nums[i] > 0, since the array is sorted and three
non-negative numbers (with at least one positive) can't sum to zero.
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


def _normalize(triplets: list[list[int]]) -> list[list[int]]:
    return sorted(triplets)


if __name__ == "__main__":
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = three_sum(inp)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
