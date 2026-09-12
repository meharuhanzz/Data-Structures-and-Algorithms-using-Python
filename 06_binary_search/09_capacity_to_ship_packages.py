"""
Problem: Packages (given as weights, in order) must be shipped within
`days` days. Each day the ship loads consecutive packages (in the
given order) up to its weight capacity. Find the minimum capacity
that allows shipping everything within `days` days.
Source : LeetCode 1011 - Capacity To Ship Packages Within D Days

Example:
    Input:  weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15

Idea: same "binary search on the answer" shape as 08. The candidate
answer is the ship's capacity, ranging from max(weights) (must fit
the single heaviest package) to sum(weights) (ship everything in one
day). "Days needed at capacity X" is monotonic - a bigger capacity
never needs more days - so binary search for the smallest capacity
whose days-needed is still <= the limit.
"""


def ship_within_days(weights: list[int], days: int) -> int:
    def days_needed(capacity: int) -> int:
        trips = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                trips += 1
                current_load = 0
            current_load += w
        return trips

    left, right = max(weights), sum(weights)

    while left < right:
        mid = (left + right) // 2
        if days_needed(mid) <= days:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
    ]

    for i, (weights, days, expected) in enumerate(tests, 1):
        got = ship_within_days(weights, days)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
