"""
Problem: Given an array of unique integers, return all possible
permutations (every arrangement, order matters).
Source : LeetCode 46 - Permutations

Example:
    Input:  [1, 2, 3]
    Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Idea: unlike 01's subsets, order matters here, so there's no `start`
index to prevent revisiting earlier elements - every still-unused
element is a valid next choice at every position, tracked with a
`used` array instead. A path only counts as a complete result once
it reaches the full length (unlike subsets, a partial permutation
isn't itself a valid answer - it must be recorded only at the leaves
of the recursion tree, not at every node).
"""


def permute(nums: list[int]) -> list[list[int]]:
    result = []
    path: list[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result


def _normalize(perms):
    return sorted(tuple(p) for p in perms)


if __name__ == "__main__":
    tests = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([5], [[5]]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = permute(inp)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
