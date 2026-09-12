"""
Problem: Given an array where nums[i] is the maximum jump length from
index i, determine if the last index is reachable starting from
index 0.
Source : LeetCode 55 - Jump Game

Example:
    Input:  [2, 3, 1, 1, 4]
    Output: True

Idea: track the single greedy quantity "farthest index reachable so
far," updated at every position: `farthest = max(farthest, i +
nums[i])`. There's no need to try every possible jump length from
every position (which is what a backtracking/DP-over-every-choice
approach would do) - only the *farthest* reach matters, since any
jump length shorter than the max at a given index can never do better
than the max jump already accounted for. If the current index `i`
is ever beyond `farthest`, the walk has hit a gap no earlier jump
could cross, so the end is unreachable.
"""


def can_jump(nums: list[int]) -> bool:
    farthest = 0
    for i, n in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + n)
    return True


if __name__ == "__main__":
    tests = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 0, 1], False),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        got = can_jump(nums)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
