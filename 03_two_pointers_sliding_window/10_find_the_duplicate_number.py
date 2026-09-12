"""
Problem: Given an array nums of n+1 integers where every value is in
[1, n], exactly one value repeats (possibly more than once). Find it
without modifying the array and using O(1) extra space.
Source : LeetCode 287 - Find the Duplicate Number

Example:
    Input:  [1, 3, 4, 2, 2]
    Output: 2

Idea: fast-slow pointers (Floyd's cycle detection) - a preview of the
technique this repo will reuse constantly in 04_linked_list for cycle
detection. Treat the array as a linked list where index i points to
nums[i]. Because a value repeats, two different indices point to the
same next index, which creates a cycle. Two-phase algorithm:
  1. Move slow one step (nums[slow]) and fast two steps
     (nums[nums[fast]]) until they meet inside the cycle.
  2. Reset one pointer to the start; move both one step at a time -
     they meet again exactly at the cycle's entrance, which is the
     duplicate value. (Standard Floyd's algorithm property.)
"""


def find_duplicate(nums: list[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = nums[0]
    while slow2 != slow:
        slow2 = nums[slow2]
        slow = nums[slow]

    return slow


if __name__ == "__main__":
    tests = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = find_duplicate(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
