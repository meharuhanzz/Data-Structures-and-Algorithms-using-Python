"""
Problem: Given strings s1 and s2, return True if s2 contains a
permutation of s1 as a contiguous substring (i.e. some substring of
s2 is an anagram of s1).
Source : LeetCode 567 - Permutation in String

Example:
    Input:  s1 = "ab", s2 = "eidbaooo"
    Output: True   ("ba" at index 3..4 is a permutation of "ab")

Idea: fixed-size window, size = len(s1). Maintain a running character
count of the current window in s2 and compare it to s1's character
count. Slide the window one step at a time (add the entering
character, remove the one leaving); whenever the two count dicts are
exactly equal, a permutation has been found. Dict equality (`==`)
compares keys and values, so this is a single O(1)-ish check per
step rather than resorting/recomparing strings.
"""


def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    need: dict[str, int] = {}
    for ch in s1:
        need[ch] = need.get(ch, 0) + 1

    window: dict[str, int] = {}
    k = len(s1)

    for i, ch in enumerate(s2):
        window[ch] = window.get(ch, 0) + 1

        if i >= k:
            left_ch = s2[i - k]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]

        if window == need:
            return True

    return False


if __name__ == "__main__":
    tests = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
        ("hello", "ooolleoooleh", False),
    ]

    for i, (s1, s2, expected) in enumerate(tests, 1):
        got = check_inclusion(s1, s2)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
