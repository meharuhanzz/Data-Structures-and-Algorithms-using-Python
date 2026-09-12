"""
Problem: Given two words, return the minimum number of single-
character operations (insert, delete, or replace) needed to turn
word1 into word2.
Source : LeetCode 72 - Edit Distance (Levenshtein Distance)

Example:
    Input:  word1 = "horse", word2 = "ros"
    Output: 3   (horse -> rorse -> rose -> ros)

Idea: same dp[i][j]-over-two-strings shape as 03, but instead of
"longest match," this counts "fewest edits." If the current
characters match, no edit is needed here - carry forward dp[i-1][j-1]
unchanged (mirrors 03's diagonal-match case exactly). If they don't
match, one of three single edits must happen, and each maps to a
specific neighbor in the table: replace word1[i-1] with word2[j-1]
(dp[i-1][j-1] + 1 - both strings advance together after the edit),
delete word1[i-1] (dp[i-1][j] + 1 - word1 advances alone), or insert
word2[j-1] into word1 (dp[i][j-1] + 1 - word2 advances alone). Taking
the minimum of those three options is what makes this "edit distance"
where 03 took a `max` for "longest match" - same table shape, inverted
optimization goal. The first row/column are seeded with i and j
(turning an i-length prefix into empty, or empty into a j-length
prefix, costs exactly that many inserts/deletes).
"""


def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j - 1],  # replace
                    dp[i - 1][j],      # delete from word1
                    dp[i][j - 1],      # insert into word1
                )

    return dp[m][n]


if __name__ == "__main__":
    tests = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "abc", 3),
        ("abc", "abc", 0),
    ]

    for i, (word1, word2, expected) in enumerate(tests, 1):
        got = min_distance(word1, word2)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
