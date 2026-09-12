"""
Problem: Given an array of meeting time intervals [start, end],
return the minimum number of conference rooms required to hold all
of them (overlapping meetings need separate rooms).
Source : LeetCode 253 - Meeting Rooms II

Example:
    Input:  [[0, 30], [5, 10], [15, 20]]
    Output: 2

Idea: sort meetings by start time, then process them in that order
while tracking the *end times of all currently-ongoing meetings* in
a min-heap. For each new meeting, check the heap's smallest end time
(the room that frees up soonest): if that room is already free by
the time this meeting starts, reuse it (pop the old end time, push
the new one - same room, new occupant). Otherwise, no existing room
is free yet, so a new one is needed (just push, growing the heap).
The heap's final size is exactly the peak number of simultaneously
occupied rooms - the answer.
"""

import heapq


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    intervals = sorted(intervals)
    heap: list[int] = []  # end times of ongoing meetings

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)

    return len(heap)


if __name__ == "__main__":
    tests = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [8, 9], [8, 9]], 2),
        ([], 0),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = min_meeting_rooms(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
