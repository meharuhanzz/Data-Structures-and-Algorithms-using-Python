"""
Problem: Given an array of unique integers, return all possible
subsets (the power set).
Source : LeetCode 78 - Subsets

Example:
    Input:  [1, 2, 3]
    Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

Idea: the template every problem in this folder is built on:
choose -> explore -> un-choose. `path` holds the subset being built;
every recursive call first records the *current* path as a valid
subset (unlike permutations, a subset is valid at every partial
length, not just when full), then tries adding each remaining
candidate in turn, recursing, and removing it again before trying the
next candidate ("un-choose" - this is what makes it backtracking
instead of a single forward walk). `start` ensures each element is
only ever considered *after* the ones already in path, which is what
prevents [1,2] and [2,1] from both appearing (subsets don't care
about order, so only one arrangement of each combination should ever
be generated).
"""


def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


def _normalize(subsets_list):
    return sorted(tuple(s) for s in subsets_list)


if __name__ == "__main__":
    tests = [
        ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
        ([], [[]]),
        ([0], [[], [0]]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = subsets(inp)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
