"""
Problem: Given an encoded string like "3[a2[c]]", decode it. The
encoding rule is k[encoded_string], meaning encoded_string is
repeated k times. Nesting is allowed.
Source : LeetCode 394 - Decode String

Example:
    Input:  "3[a2[c]]"
    Output: "accaccacc"

Idea: a stack of (string-so-far, repeat-count) pairs, one entry per
level of nesting. On '[', the current partial string and the number
built up before it are pushed - "paused" - and a fresh partial string
starts for the nested level. On ']', the nested level is complete:
pop the paused (outer_string, count), and the finished nested string
is repeated `count` times and appended onto outer_string, which
becomes the new "current" string. This is the general pattern for
any nested-structure parsing problem: push state before descending
into a nested level, pop and combine when that level closes.
"""


def decode_string(s: str) -> str:
    stack: list[tuple[str, int]] = []
    current_str = ""
    current_num = 0

    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == "[":
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif ch == "]":
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += ch

    return current_str


if __name__ == "__main__":
    tests = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = decode_string(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got!r}, expected {expected!r})")
