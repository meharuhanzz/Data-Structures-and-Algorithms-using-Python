"""
Problem: Given a string s, determine if it is a palindrome after
considering only alphanumeric characters and ignoring case.
Source : LeetCode 125 - Valid Palindrome

Example:
    Input:  "A man, a plan, a canal: Panama"
    Output: True   (reads "amanaplanacanalpanama" both ways)

    Input:  "race a car"
    Output: False

Idea: same mirror two-pointer shape as reverse_string, but each
pointer independently skips non-alphanumeric characters before the
comparison, and comparison is case-insensitive.
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
        (".,", True),
        ("0P", False),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = is_palindrome(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
