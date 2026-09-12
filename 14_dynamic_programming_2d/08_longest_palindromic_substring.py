"""
Problem: Given a string s, return its longest palindromic substring
(contiguous, unlike a subsequence).
Source : LeetCode 5 - Longest Palindromic Substring

Example:
    Input:  "babad"
    Output: "bab"   ("aba" is also a valid answer)

Idea: dp[i][j] = "is s[i..j] a palindrome?" A substring is a
palindrome exactly when its outer characters match
(`s[i] == s[j]`) *and* everything strictly inside is also a
palindrome (`dp[i+1][j-1]`) - or the inside is trivially empty/a
single character (length 2 or less), which needs no further check.
Filling the table by increasing *length* (not by row or column
directly) is what makes this correct: computing dp[i][j] for a
substring of length L requires dp[i+1][j-1], a strictly shorter
substring, which must already be finalized - iterating outer-to-inner
lengths guarantees that dependency is always ready before it's
needed. Track the best (start, length) seen as the table fills.
"""


def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    start, max_len = 0, 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if length > max_len:
                    start, max_len = i, length

    return s[start:start + max_len]


if __name__ == "__main__":
    tests = [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("a", {"a"}),
        ("", {""}),
    ]

    for i, (s, expected_set) in enumerate(tests, 1):
        got = longest_palindromic_substring(s)
        status = "PASS" if got in expected_set else "FAIL"
        print(f"Test {i}: {status} (got {got!r}, expected one of {expected_set})")
