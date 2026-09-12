"""
Problem: Given a list of tasks (letters) and a cooldown n (the same
task must wait at least n intervals before running again), return the
minimum total number of intervals (including idle slots) needed to
finish all tasks. Each interval runs one task or sits idle.
Source : LeetCode 621 - Task Scheduler

Example:
    Input:  tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8   (A B _ A B _ A B - the two idle slots are unavoidable)

Idea: greedily run whichever remaining task has the *highest* count
first - a max-heap of task counts, same negate trick as 01. After
running a task, it can't run again for n intervals, so it goes into a
side "cooldown queue" holding (time_it_becomes_available_again,
remaining_count) instead of straight back into the heap. Only once
the clock reaches that available time does it get pushed back onto
the heap to compete again. The simulation naturally produces idle
intervals: if the heap is empty but the cooldown queue isn't, time
still has to advance with nothing to run.
"""

import heapq
from collections import Counter, deque


def least_interval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_heap = [-c for c in counts.values()]
    heapq.heapify(max_heap)

    time = 0
    cooldown: deque[tuple[int, int]] = deque()  # (time_available_again, remaining_count)

    while max_heap or cooldown:
        time += 1
        if max_heap:
            remaining = 1 + heapq.heappop(max_heap)  # remaining is <= 0 (negated)
            if remaining:
                cooldown.append((time + n, remaining))
        if cooldown and cooldown[0][0] == time:
            heapq.heappush(max_heap, cooldown.popleft()[1])

    return time


if __name__ == "__main__":
    tests = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    ]

    for i, (tasks, n, expected) in enumerate(tests, 1):
        got = least_interval(tasks, n)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
