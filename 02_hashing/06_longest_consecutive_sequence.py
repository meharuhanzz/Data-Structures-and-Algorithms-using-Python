"""
Problem: Given an unsorted array of integers, return the length of
the longest run of consecutive integers (order in the array doesn't
matter). Must run in O(n) time.
Source : LeetCode 128 - Longest Consecutive Sequence

Example:
    Input:  [100, 4, 200, 1, 3, 2]
    Output: 4   (the sequence 1, 2, 3, 4)

Idea: put everything in a set for O(1) membership checks. Only start
counting a sequence from a number that is the *start* of one, i.e.
n - 1 is not in the set. That guarantees each sequence is only ever
walked once in full, from its start, giving O(n) total work instead
of O(n) per starting point.
"""


def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    tests = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1, 2, 0, 1], 3),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = longest_consecutive(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
