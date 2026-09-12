"""
Problem: Given an array of bar heights forming a histogram (each bar
width 1), find the area of the largest rectangle that fits entirely
within the histogram's outline.
Source : LeetCode 84 - Largest Rectangle in Histogram

Example:
    Input:  [2, 1, 5, 6, 2, 3]
    Output: 10   (rectangle of height 5 spanning bars at indices 2-3
                  gives 5*2=10; height 2 spanning indices 2-5 also
                  gives 2*4=8; the height-5/6 pair wins at 10)

Idea: monotonic (increasing) stack of indices. For any bar, the
widest rectangle *of that bar's height* extends left and right until
hitting a shorter bar - so the moment a shorter bar is encountered
while scanning left to right, every taller bar still on the stack has
just found its right boundary. Pop it, compute its area using the
now-shorter stack top as its left boundary (or index 0 if the stack
is empty, meaning nothing shorter exists to its left). A sentinel
height of 0 appended at the end forces every remaining bar on the
stack to be resolved by the time the scan finishes.
"""


def largest_rectangle_area(heights: list[int]) -> int:
    heights = heights + [0]
    stack: list[int] = []  # indices, heights increasing bottom to top
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


if __name__ == "__main__":
    tests = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([], 0),
        ([5, 5, 5], 15),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = largest_rectangle_area(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
