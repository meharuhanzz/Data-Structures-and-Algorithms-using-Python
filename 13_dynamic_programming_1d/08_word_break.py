"""
Problem: Given a string s and a dictionary of words, return True if
s can be segmented into a sequence of one or more dictionary words
(words may be reused any number of times).
Source : LeetCode 139 - Word Break

Example:
    Input:  s = "leetcode", word_dict = ["leet", "code"]
    Output: True   ("leet" + "code")

Idea: dp[i] = "can the prefix s[:i] be fully segmented into
dictionary words?" dp[0] = True (the empty prefix trivially can, with
zero words) is the base case that everything else builds from. For
each position i, check every earlier split point j: if s[:j] is
already known segmentable (dp[j] is True) and the remaining piece
s[j:i] is itself a dictionary word, then s[:i] is segmentable too.
This is structurally the same "try every split point" shape as
`10_recursion_backtracking/08_palindrome_partitioning`, except here
only a yes/no reachability is needed (not every possible partition
enumerated), which is exactly what turns an exponential backtracking
search into a polynomial DP - each dp[i] is computed once and reused,
instead of being re-explored from scratch down every branch.
"""


def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]


if __name__ == "__main__":
    tests = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("", ["a"], True),
    ]

    for i, (s, word_dict, expected) in enumerate(tests, 1):
        got = word_break(s, word_dict)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
