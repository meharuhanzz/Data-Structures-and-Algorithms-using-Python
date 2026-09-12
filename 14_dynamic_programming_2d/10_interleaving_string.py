"""
Problem: Given strings s1, s2, and s3, determine if s3 is formed by
interleaving s1 and s2 (s3 uses every character of both, preserving
each string's internal relative order, but the two can be mixed
together in any order).
Source : LeetCode 97 - Interleaving String

Example:
    Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: True

Idea: back to a two-string dp[i][j] table like 03/04, but here both
i and j jointly determine a *fixed* position in s3
(`s3[i+j-1]`) rather than being compared to each other directly -
the length constraint `len(s1) + len(s2) == len(s3)` must hold first,
or interleaving is impossible regardless of content. dp[i][j] = "can
the first i characters of s1 and first j characters of s2 interleave
to form the first i+j characters of s3?" True exactly when *either*
s1's next character extends a valid interleaving from dp[i-1][j], or
s2's next character extends one from dp[i][j-1] - matching the
appropriate side against s3[i+j-1] in each case. The first row and
column are seeded by checking whether s1 alone (or s2 alone) matches
the corresponding prefix of s3 exactly, since only one string is
contributing along those edges.
"""


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (
                (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
            )

    return dp[m][n]


if __name__ == "__main__":
    tests = [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
        ("a", "", "a", True),
        ("a", "b", "ab", True),
    ]

    for i, (s1, s2, s3, expected) in enumerate(tests, 1):
        got = is_interleave(s1, s2, s3)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
