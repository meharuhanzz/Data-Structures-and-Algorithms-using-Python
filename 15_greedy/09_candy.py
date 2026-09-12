"""
Problem: Children stand in a line, each with a rating. Every child
gets at least one candy, and any child with a higher rating than an
immediate neighbor must get more candy than that neighbor. Return the
minimum total candies needed.
Source : LeetCode 135 - Candy

Example:
    Input:  [1, 0, 2]
    Output: 5   (candies [2, 1, 2])

Idea: the constraint is *bidirectional* (compare to both the left
neighbor and the right neighbor), but each single greedy left-to-
right or right-to-left pass can only correctly enforce the comparison
in *one* direction at a time. The fix: two passes. A left-to-right
pass enforces "higher than the left neighbor gets more candy than the
left neighbor" by only ever increasing from the previous position. A
right-to-left pass then enforces the mirror constraint against the
right neighbor - using `max(candies[i], candies[i+1] + 1)`, not a
plain overwrite, since the left-to-right pass may have already
assigned this position a value satisfying its *left* constraint that's
bigger than what the right constraint alone would require, and that
already-satisfied value must not be reduced.
"""


def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


if __name__ == "__main__":
    tests = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 3, 2, 2, 1], 7),
        ([1], 1),
    ]

    for i, (ratings, expected) in enumerate(tests, 1):
        got = candy(ratings)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
