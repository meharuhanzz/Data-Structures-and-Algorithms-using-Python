"""
Problem: A digit string can be decoded to letters via 'A'->1 ...
'Z'->26. Given a digit string s, return the number of ways it can be
decoded. (A leading zero in any 1- or 2-digit group makes that
grouping invalid - '0' alone decodes to nothing.)
Source : LeetCode 91 - Decode Ways

Example:
    Input:  "226"
    Output: 3   ("2,2,6" -> "BBF", "22,6" -> "VF", "2,26" -> "BZ")

Idea: same rolling-pair shape as 01's climbing stairs - the number of
ways to decode the prefix ending at position i is built from the
number of ways ending at i-1 (if the single digit at i is valid,
i.e. not '0') plus the number of ways ending at i-2 (if the *two*
digits ending at i form a valid 10-26 group). This is genuinely
climbing stairs with an extra validity condition gating each of the
two "step sizes" - worth noticing the structural similarity rather
than treating this as an unrelated new problem. The two edge
conditions (a lone '0' is always invalid; a two-digit group must be
10-26, not any two digits) are what most solutions get wrong first
try - they're the entire difficulty of this problem, not the DP shape.
"""


def num_decodings(s: str) -> int:
    if not s or s[0] == "0":
        return 0

    n = len(s)
    prev2, prev1 = 1, 1  # ways to decode "" (empty), ways to decode s[:1]

    for i in range(2, n + 1):
        curr = 0
        one_digit = int(s[i - 1])
        two_digit = int(s[i - 2:i])

        if one_digit >= 1:
            curr += prev1
        if 10 <= two_digit <= 26:
            curr += prev2

        prev2, prev1 = prev1, curr

    return prev1


if __name__ == "__main__":
    tests = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
        ("0", 0),
        ("10", 1),
        ("27", 1),
        ("100", 0),
    ]

    for i, (s, expected) in enumerate(tests, 1):
        got = num_decodings(s)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
