"""
Problem: Given a list of strings, find the longest common prefix
shared by all of them. Return "" if there is no common prefix.
Source : LeetCode 14 - Longest Common Prefix

Example:
    Input:  ["flower", "flow", "flight"]
    Output: "fl"

Idea: vertical scan. Walk character-index by character-index using
the first string as the reference; at each index, check that every
other string has the same character there. Stop at the first
mismatch (or the first string that's too short) and the prefix so
far is the answer.
"""


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]


if __name__ == "__main__":
    tests = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["a"], "a"),
        ([], ""),
        (["", "b"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = longest_common_prefix(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got!r}, expected {expected!r})")
