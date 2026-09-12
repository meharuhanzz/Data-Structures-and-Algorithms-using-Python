"""
Problem: Given a string s of uppercase letters and integer k, you may
replace up to k characters in the string with any other uppercase
letter. Return the length of the longest substring achievable where
every character is the same after doing so.
Source : LeetCode 424 - Longest Repeating Character Replacement

Example:
    Input:  s = "AABABBA", k = 1
    Output: 4   (replace one 'A' at index 3 -> "AABBBBA" contains "ABBB"? actually "BABB"->
                 replace to get "AABBBBA", longest run of one letter after 1 replacement is 4)

Idea: variable window tracked with a frequency count of the window's
characters. A window of length L needs at most k replacements to
become uniform if (L - count of its most frequent character) <= k -
i.e. everything that ISN'T the majority character must be replaceable
within budget k. Grow `right` always; shrink `left` only when the
window violates that budget. `max_count` is allowed to go stale
(never decremented on shrink) because the answer only cares about the
best window ever seen, not the exact max_count for the current
window - a well-known simplification for this specific problem.
"""


def character_replacement(s: str, k: int) -> int:
    counts: dict[str, int] = {}
    left = 0
    max_count = 0
    longest = 0

    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        max_count = max(max_count, counts[ch])

        window_len = right - left + 1
        if window_len - max_count > k:
            counts[s[left]] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    tests = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 0, 4),
        ("ABBB", 0, 3),
    ]

    for i, (s, k, expected) in enumerate(tests, 1):
        got = character_replacement(s, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
