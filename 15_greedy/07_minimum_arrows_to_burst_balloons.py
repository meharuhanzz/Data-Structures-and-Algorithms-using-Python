"""
Problem: Balloons are represented as intervals [x_start, x_end] along
a line. An arrow shot at position x bursts every balloon whose
interval contains x. Return the minimum number of arrows needed to
burst all balloons.
Source : LeetCode 452 - Minimum Number of Arrows to Burst Balloons

Example:
    Input:  [[10,16], [2,8], [1,6], [7,12]]
    Output: 2   (one arrow at x=6 bursts [2,8] and [1,6]; one arrow
                  at x=12 bursts [10,16] and [7,12])

Idea: the same end-time-sorted greedy shape as 06, applied to a
question about *covering* points instead of *keeping* non-overlapping
intervals - but they're really the same problem viewed from opposite
sides. Sort by end coordinate; shoot the first arrow at the first
balloon's end - the latest possible x that still bursts it, which
therefore has the best chance of also bursting other balloons whose
ranges extend that far. Any later balloon whose start is beyond the
current arrow's position can't be hit by it, so it needs a new arrow,
placed at *that* balloon's end going forward. Every balloon that
starts before or at the current arrow's x is already covered - no
separate tracking needed, since sorting by end time guarantees
covered balloons are consumed in order.
"""


def find_min_arrow_shots(points: list[list[int]]) -> int:
    if not points:
        return 0

    points = sorted(points, key=lambda p: p[1])
    arrows = 1
    arrow_pos = points[0][1]

    for start, end in points[1:]:
        if start > arrow_pos:
            arrows += 1
            arrow_pos = end

    return arrows


if __name__ == "__main__":
    tests = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        ([], 0),
    ]

    for i, (points, expected) in enumerate(tests, 1):
        got = find_min_arrow_shots(points)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
