"""
Problem: You're climbing a staircase of n steps; each move you can
climb 1 or 2 steps. Return the number of distinct ways to reach the
top.
Source : LeetCode 70 - Climbing Stairs

Example:
    Input:  n = 5
    Output: 8

Idea: the simplest possible 1D DP, and the template for every problem
in this folder: the number of ways to reach step n is the number of
ways to reach step n-1 (then take one more step) plus the number of
ways to reach step n-2 (then take a two-step jump) - literally the
Fibonacci recurrence, arrived at independently from the problem's own
structure rather than memorized. Rather than an explicit dp array,
only the last two values are ever needed at once, so two rolling
variables (`prev2`, `prev1`) suffice - O(1) space instead of O(n).
This "only the last k states matter" observation is what turns a
naive O(2^n) recursive branch-on-every-choice solution into a linear
one-pass computation.
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev2, prev1 = 1, 2  # ways to reach step 1, ways to reach step 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2

    return prev1


if __name__ == "__main__":
    tests = [
        (1, 1),
        (2, 2),
        (3, 3),
        (5, 8),
    ]

    for i, (n, expected) in enumerate(tests, 1):
        got = climb_stairs(n)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
