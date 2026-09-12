"""
Problem: Given n pairs of parentheses, generate all combinations of
well-formed parenthesis strings.
Source : LeetCode 22 - Generate Parentheses

Example:
    Input:  n = 3
    Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

Idea: rather than generating all 2^(2n) strings of parens and
filtering for validity, prune invalid paths *during* construction -
a much smaller search tree. Two counters, `open_count` and
`close_count`, track how many of each have been placed. An open
paren can be added any time `open_count < n` (haven't used them all
yet). A close paren can only be added if `close_count < open_count`
(there must be a still-unmatched open paren to close - this is
exactly what keeps every prefix of the string valid, not just the
final result). No explicit "un-choose" of the counters is needed
since they're passed by value into each recursive call.
"""


def generate_parenthesis(n: int) -> list[str]:
    result = []
    path: list[str] = []

    def backtrack(open_count: int, close_count: int) -> None:
        if len(path) == 2 * n:
            result.append("".join(path))
            return
        if open_count < n:
            path.append("(")
            backtrack(open_count + 1, close_count)
            path.pop()
        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count + 1)
            path.pop()

    backtrack(0, 0)
    return result


if __name__ == "__main__":
    tests = [
        (3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),
        (1, {"()"}),
    ]

    for i, (n, expected) in enumerate(tests, 1):
        got = set(generate_parenthesis(n))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
