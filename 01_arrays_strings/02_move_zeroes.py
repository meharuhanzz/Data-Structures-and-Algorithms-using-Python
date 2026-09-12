"""
Problem: Move all zeroes in an array to the end, in place, while
keeping the relative order of the non-zero elements. Must be done
in O(1) extra space (no new list, no sorting).
Source : LeetCode 283 - Move Zeroes

Example:
    Input:  [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]
"""


def move_zeroes(nums: list[int]) -> None:
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1


if __name__ == "__main__":
    tests = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
        ([], []),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        arr = inp[:]
        move_zeroes(arr)
        status = "PASS" if arr == expected else "FAIL"
        print(f"Test {i}: {status} (got {arr}, expected {expected})")
