"""
Problem: Given two strings text1 and text2, return the length of
their longest common subsequence (characters in the same relative
order in both, not necessarily contiguous). Return 0 if none.
Source : LeetCode 1143 - Longest Common Subsequence

Example:
    Input:  text1 = "abcde", text2 = "ace"
    Output: 3   ("ace" is a subsequence of both)

Idea: the canonical *two-string* 2D DP - dp[i][j] = the LCS length
using the first i characters of text1 and the first j characters of
text2. Two cases at each cell: if the current characters match
(`text1[i-1] == text2[j-1]`), they can both be included in the
subsequence, so extend the LCS found *without* either of them
(dp[i-1][j-1] + 1). If they don't match, the best is whichever is
better - dropping the current character of text1 or dropping the
current character of text2 (`max(dp[i-1][j], dp[i][j-1])`). This
"match -> extend diagonally; mismatch -> take the best of dropping
one side" shape is the foundation `04`'s edit distance builds on
directly.
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    tests = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
    ]

    for i, (text1, text2, expected) in enumerate(tests, 1):
        got = longest_common_subsequence(text1, text2)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
