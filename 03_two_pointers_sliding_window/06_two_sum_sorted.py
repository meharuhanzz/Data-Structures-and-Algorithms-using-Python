"""
Problem: Given a sorted array `numbers` and integer target, return
the 0-indexed positions of the two numbers that add up to target.
(LeetCode's original returns 1-indexed positions - this version
returns 0-indexed to stay consistent with the rest of this repo.)
Source : LeetCode 167 - Two Sum II - Input Array Is Sorted

Example:
    Input:  numbers = [2, 7, 11, 15], target = 9
    Output: [0, 1]

Idea: because the array is sorted, a converging two-pointer beats the
hashmap approach from 02_hashing/01_two_sum on space - O(1) instead
of O(n). If the current pair's sum is too small, the only way to
increase it is to move `left` right (larger value). If too big, move
`right` left. Sortedness is what guarantees this greedy move is safe.
"""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([2, 3, 4], 6, [0, 2]),
        ([-1, 0], -1, [0, 1]),
    ]

    for i, (numbers, target, expected) in enumerate(tests, 1):
        got = two_sum_sorted(numbers, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
