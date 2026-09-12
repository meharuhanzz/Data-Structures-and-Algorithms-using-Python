"""
Problem: Given a string of digits 2-9, return all possible letter
combinations the digits could represent on an old phone keypad
(2 -> "abc", 3 -> "def", etc).
Source : LeetCode 17 - Letter Combinations of a Phone Number

Example:
    Input:  "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Idea: the simplest possible backtracking shape - no pruning, no
constraint to check, just a direct Cartesian product of "letters for
digit 0" x "letters for digit 1" x ... generated via recursion
instead of nested loops (useful because the number of digits, and
therefore the nesting depth, isn't known ahead of time). At each
recursion level, try every letter available for the current digit,
recurse to the next digit, and un-choose before trying the next
letter - same choose/explore/un-choose shape as every problem in
this folder, just without any pruning condition.
"""


def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    result = []
    path: list[str] = []

    def backtrack(index: int) -> None:
        if index == len(digits):
            result.append("".join(path))
            return
        for ch in mapping[digits[index]]:
            path.append(ch)
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return result


if __name__ == "__main__":
    tests = [
        ("23", {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}),
        ("", set()),
        ("2", {"a", "b", "c"}),
    ]

    for i, (digits, expected) in enumerate(tests, 1):
        got = set(letter_combinations(digits))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
