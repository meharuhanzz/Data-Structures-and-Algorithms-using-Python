"""
Problem: Given a string s, partition it so that every substring in
the partition is a palindrome. Return all possible partitions.
Source : LeetCode 131 - Palindrome Partitioning

Example:
    Input:  "aab"
    Output: [["a", "a", "b"], ["aa", "b"]]

Idea: backtracking over *where to cut*, not over which elements to
pick. At each position `start`, try every possible end point for the
next piece (`end` from start+1 to len(s)); only recurse into that
choice if `s[start:end]` is itself a palindrome (pruning branches
that could never lead to a valid full partition). A complete
partition is found once `start` reaches the end of the string - every
character has been assigned to some palindromic piece.
"""


def partition(s: str) -> list[list[str]]:
    result = []
    path: list[str] = []

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(start: int) -> None:
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end)
                path.pop()

    backtrack(0)
    return result


def _normalize(partitions):
    return sorted(tuple(p) for p in partitions)


if __name__ == "__main__":
    tests = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("", [[]]),
    ]

    for i, (s, expected) in enumerate(tests, 1):
        got = partition(s)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
