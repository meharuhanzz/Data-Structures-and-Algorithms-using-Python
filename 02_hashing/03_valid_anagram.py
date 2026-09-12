"""
Problem: Given two strings s and t, return True if t is an anagram
of s (same characters, same counts, any order).
Source : LeetCode 242 - Valid Anagram

Example:
    Input:  s = "anagram", t = "nagaram"
    Output: True

Idea: build a frequency count of s, then walk t decrementing counts.
If t ever needs a character that's not available (missing or count
already 0), it's not an anagram. If the count dict is empty at the
end, every character balanced out exactly.
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] == 0:
            del counts[ch]

    return len(counts) == 0


if __name__ == "__main__":
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("", "", True),
        ("aacc", "ccac", False),
    ]

    for i, (s, t, expected) in enumerate(tests, 1):
        got = is_anagram(s, t)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
