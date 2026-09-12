"""
Problem: Given an array `height` where height[i] is the height of a
vertical line at position i, find two lines that, together with the
x-axis, form a container holding the most water. Return the max area.
Source : LeetCode 11 - Container With Most Water

Example:
    Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49   (lines at index 1 (height 8) and index 8 (height 7):
                  area = min(8,7) * (8-1) = 7 * 7 = 49)

Idea: start with the widest possible container (both ends). Area is
limited by the shorter of the two lines, so moving the pointer at the
*taller* line inward can only keep the height the same or make it
worse (still capped by the other, shorter side) while width shrinks -
guaranteed loss. Moving the *shorter* line's pointer inward is the
only move that could possibly find a taller line and improve the
area. That greedy justification is what makes this O(n) safe (no
need to check every pair).
"""


def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        h = min(height[left], height[right])
        best = max(best, h * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best


if __name__ == "__main__":
    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = max_area(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
