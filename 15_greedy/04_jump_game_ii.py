"""
Problem: Same setup as 03 (nums[i] = max jump length from index i,
starting at index 0, guaranteed reachable this time), but return the
*minimum* number of jumps needed to reach the last index.
Source : LeetCode 45 - Jump Game II

Example:
    Input:  [2, 3, 1, 1, 4]
    Output: 2   (jump 0 -> 1 (index 0 to 1, len 1... actually 0->1 to
                 index1, then jump 3 to index4): [2,3,1,1,4] -> jump
                 to index 1, then jump 3 more to index 4)

Idea: an implicit BFS, expressed without an explicit queue - "one
jump" covers an entire *range* of indices at once, like one level of
a BFS frontier. `curr_end` marks the farthest index reachable with the
jumps taken *so far*; `farthest` tracks the farthest reachable if one
*more* jump were taken from anywhere within the current range. Walking
through positions, the moment `i` reaches `curr_end` means every
position in the current "level" has been considered - a jump must be
taken to progress at all, so increment the jump count and set
`curr_end = farthest` (moving to the next level/range). This mirrors
`04_linked_list`'s level-by-level BFS shape, just over an implicit
range-based graph instead of explicit nodes and edges.
"""


def jump(nums: list[int]) -> int:
    jumps = 0
    curr_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest

    return jumps


if __name__ == "__main__":
    tests = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([0], 0),
        ([1, 1, 1, 1], 3),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        got = jump(nums)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
