"""
Problem: Koko has piles of bananas and h hours before the guards
return. Each hour she picks one pile and eats up to `speed` bananas
from it (if the pile has fewer than `speed`, she finishes that pile
and doesn't eat more that hour). Find the minimum integer eating
speed such that she finishes all piles within h hours.
Source : LeetCode 875 - Koko Eating Bananas

Example:
    Input:  piles = [3, 6, 7, 11], h = 8
    Output: 4

Idea: "binary search on the answer" - a different flavor from every
problem so far in this folder, all of which binary-searched over an
*array index*. Here there's no array to search; instead, the answer
itself (the eating speed) lives in a range [1, max(piles)], and
"hours needed at speed X" is *monotonic* - a faster speed never needs
more hours. That monotonicity is exactly what makes binary search
valid here: binary search only requires being able to evaluate "is
this candidate answer good enough?" and having that answer be
monotonic in the candidate - it doesn't require an actual sorted
array at all.
"""


def min_eating_speed(piles: list[int], h: int) -> int:
    def hours_needed(speed: int) -> int:
        return sum((p + speed - 1) // speed for p in piles)

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= h:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    tests = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([312884470], 968709470, 1),
    ]

    for i, (piles, h, expected) in enumerate(tests, 1):
        got = min_eating_speed(piles, h)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
