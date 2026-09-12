"""
Problem: Design a structure that supports add_num(val), adding an
integer to a running stream, and find_median(), returning the median
of all numbers added so far, at any point in the stream.
Source : LeetCode 295 - Find Median from Data Stream

Example:
    mf = MedianFinder()
    mf.add_num(1); mf.add_num(2)
    mf.find_median()  -> 1.5
    mf.add_num(3)
    mf.find_median()  -> 2.0

Idea: the hardest problem in this folder, and the canonical
"two heaps" pattern. Split all numbers seen so far into two halves:
`small`, a *max*-heap (negated) holding the smaller half, and
`large`, a *min*-heap holding the bigger half - kept balanced so
their sizes differ by at most one. The median is then always sitting
at the top of one or both heaps, an O(1) lookup, with no need to ever
sort or scan the full stream. Every add_num does three heap ops to
maintain two invariants:
  1. every value in `small` <= every value in `large` (enforced by
     always pushing into `small` first, then immediately moving its
     largest into `large` - guarantees correct ordering even if the
     new value belonged in `large`).
  2. `len(large) <= len(small) <= len(large) + 1` (enforced by moving
     one value back from `large` to `small` if `large` grew too big).
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.small: list[int] = []  # max-heap (negated), holds the lower half
        self.large: list[int] = []  # min-heap, holds the upper half

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    ops = [
        (mf.add_num, (1,), None),
        (mf.add_num, (2,), None),
        (mf.find_median, (), 1.5),
        (mf.add_num, (3,), None),
        (mf.find_median, (), 2.0),
        (mf.add_num, (10,), None),
        (mf.find_median, (), 2.5),
        (mf.add_num, (-5,), None),
        (mf.find_median, (), 2.0),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        if expected is None:
            status = "PASS"
        else:
            status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} ({fn.__name__}{args} -> got {got}, expected {expected})")
