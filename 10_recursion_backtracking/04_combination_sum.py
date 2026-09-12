"""
Problem: Given distinct candidates and a target, return all unique
combinations where the chosen numbers sum to target. The same number
may be used an unlimited number of times.
Source : LeetCode 39 - Combination Sum

Example:
    Input:  candidates = [2, 3, 6, 7], target = 7
    Output: [[2, 2, 3], [7]]

Idea: subsets-shaped backtracking (01's `start` index prevents using
earlier elements again as *siblings*), but with the target sum as
the stopping condition instead of subset-at-every-node, and with
*reuse allowed* - the recursive call passes `i` (not `i + 1`) as the
next start, meaning the same candidate can be picked again
immediately after itself. Two base cases: `remaining == 0` is success
(record the path), `remaining < 0` is failure (prune - no need to
keep exploring a sum that already overshot).
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    path: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])  # i, not i+1: reuse allowed
            path.pop()

    backtrack(0, target)
    return result


def _normalize(combos):
    return sorted(tuple(sorted(c)) for c in combos)


if __name__ == "__main__":
    tests = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ]

    for i, (candidates, target, expected) in enumerate(tests, 1):
        got = combination_sum(candidates, target)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
