"""
Problem: Given a string s, return the index of the first character
that does not repeat elsewhere in s. Return -1 if none exists.
Source : LeetCode 387 - First Unique Character in a String

Example:
    Input:  "leetcode"
    Output: 0   ('l' never repeats)

    Input:  "loveleetcode"
    Output: 2   ('v' is the first char with count 1)

Idea: two passes. First build a full frequency count (need to see
the whole string before knowing which chars repeat). Second pass
walks in original order and returns the first index whose character
has count 1 - the dict lookup makes this O(1) per character.
"""


def first_uniq_char(s: str) -> int:
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i

    return -1


if __name__ == "__main__":
    tests = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("", -1),
        ("z", 0),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = first_uniq_char(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
