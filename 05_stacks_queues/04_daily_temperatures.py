"""
Problem: Given a list of daily temperatures, return a list where
answer[i] is the number of days until a warmer temperature. If there
is none, answer[i] = 0.
Source : LeetCode 739 - Daily Temperatures

Example:
    Input:  [73, 74, 75, 71, 69, 72, 76, 73]
    Output: [1, 1, 4, 2, 1, 1, 0, 0]

Idea: monotonic (decreasing) stack of *indices*. Walk left to right;
whenever the current temperature is warmer than the temperature at
the index on top of the stack, that's the answer for that stacked
index (found its "next warmer day"), so pop it and record the gap.
Keep popping while the new temperature beats the stack top - a
single element only ever gets pushed once and popped once, so the
whole pass is O(n) even though it looks like nested loops.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    stack: list[int] = []  # indices, temperatures decreasing bottom to top

    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)

    return result


if __name__ == "__main__":
    tests = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = daily_temperatures(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
