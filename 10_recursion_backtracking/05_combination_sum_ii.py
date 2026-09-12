"""
Problem: Given a collection of candidates that may contain
duplicates and a target, return all unique combinations that sum to
target. Each number may be used at most once (no reuse).
Source : LeetCode 40 - Combination Sum II

Example:
    Input:  candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
    Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

Idea: combines 02's duplicate-skip trick with 04's target-sum
backtracking, minus the reuse. Sort first so duplicates are adjacent
and skip a candidate equal to the previous one *at the same tree
level* (same reasoning as 02: this blocks generating the same
combination twice, not blocks using two equal values together). The
recursive call passes `i + 1` (not `i`, unlike 04) since each element
can only be used once. One extra optimization: since candidates are
sorted, the moment `candidates[i] > remaining`, every later candidate
is even bigger, so the loop can `break` entirely instead of just
`continue`-ing past this one option.
"""


def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates = sorted(candidates)
    result = []
    path: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return result


def _normalize(combos):
    return sorted(tuple(c) for c in combos)  # already in sorted order per combo


if __name__ == "__main__":
    tests = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ]

    for i, (candidates, target, expected) in enumerate(tests, 1):
        got = combination_sum2(candidates, target)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
