"""
Problem: Given a string s, find the length of the longest substring
without repeating characters.
Source : LeetCode 3 - Longest Substring Without Repeating Characters

Example:
    Input:  "abcabcbb"
    Output: 3   ("abc")

Idea: variable-size sliding window. `right` extends the window one
character at a time. A dict tracks the last index each character was
seen at. If the character at `right` was seen before *and* that
occurrence is still inside the current window, jump `left` to just
past it - no need to shrink one step at a time, the dict gives the
jump target directly.
"""


def length_of_longest_substring(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    longest = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = length_of_longest_substring(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
