"""
Problem: Given a string s, return the total number of palindromic
substrings it contains (different positions count separately, even
if the substrings have the same characters).
Source : LeetCode 647 - Palindromic Substrings

Example:
    Input:  "aaa"
    Output: 6   ("a","a","a","aa","aa","aaa")

Idea: the exact same dp[i][j] palindrome table as 08 - the only
difference is what's done with it. Instead of tracking the single
best (longest) palindrome found, every cell that's True is itself a
valid palindromic substring, so simply counting how many cells end up
True gives the answer directly. This pairing (08 and 09) is worth
noticing as a general lesson: once a DP table answers "is X true for
this state," many different final questions (longest, count, does any
exist, list them all) can be read off the *same* table - the table
itself is usually the hard part; the final readout is often trivial.
"""


def count_substrings(s: str) -> int:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                count += 1

    return count


if __name__ == "__main__":
    tests = [
        ("abc", 3),
        ("aaa", 6),
        ("", 0),
        ("aba", 4),
    ]

    for i, (s, expected) in enumerate(tests, 1):
        got = count_substrings(s)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
