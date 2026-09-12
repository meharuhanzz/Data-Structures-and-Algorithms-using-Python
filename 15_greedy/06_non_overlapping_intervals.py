"""
Problem: Given a collection of intervals, return the minimum number
of intervals that must be removed so the rest don't overlap.
Source : LeetCode 435 - Non-overlapping Intervals

Example:
    Input:  [[1,2], [2,3], [3,4], [1,3]]
    Output: 1   (remove [1,3])

Idea: the classic "activity selection" greedy - sort intervals by
*end* time (not start time), then greedily keep an interval only if
it starts at or after the previously kept interval's end. Sorting by
end time is the crucial choice: keeping whichever interval ends
*soonest* at every step leaves the most room for future intervals to
also fit without overlapping - provably at least as good as any
other selection strategy (an exchange argument: any valid selection
can be modified to instead pick the earliest-ending option at each
step without making things worse). Every interval that doesn't fit
(starts before the previous kept interval ends) has to be one of the
removed ones, so counting those rejections directly gives the answer
- no need to explicitly construct the kept set.
"""


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda interval: interval[1])
    removed = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < prev_end:
            removed += 1
        else:
            prev_end = end

    return removed


if __name__ == "__main__":
    tests = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
        ([], 0),
    ]

    for i, (intervals, expected) in enumerate(tests, 1):
        got = erase_overlap_intervals(intervals)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
