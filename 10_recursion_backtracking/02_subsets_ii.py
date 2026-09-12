"""
Problem: Given an integer array that may contain duplicates, return
all possible subsets, with no duplicate subsets in the result.
Source : LeetCode 90 - Subsets II

Example:
    Input:  [1, 2, 2]
    Output: [[], [1], [1,2], [1,2,2], [2], [2,2]]

Idea: same shape as 01, plus one guard against duplicate output.
Sort first, so equal values become adjacent. At each level of the
loop, skip a candidate if it's equal to the *previous* candidate at
that same level (`i > start and nums[i] == nums[i-1]`) - the
`i > start` check is what distinguishes "two equal values used
together in one subset" (allowed - that's just consuming both 2s)
from "two equal values both starting a sibling subset at this
level" (not allowed - that would generate the same subset twice).
"""


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    result = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


def _normalize(subsets_list):
    return sorted(tuple(s) for s in subsets_list)


if __name__ == "__main__":
    tests = [
        ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        ([0], [[], [0]]),
        ([2, 2], [[], [2], [2, 2]]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = subsets_with_dup(inp)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
