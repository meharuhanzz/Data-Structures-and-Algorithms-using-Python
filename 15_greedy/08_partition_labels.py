"""
Problem: Given a string s, partition it into as many contiguous
pieces as possible such that each letter appears in at most one
piece. Return the list of piece lengths.
Source : LeetCode 763 - Partition Labels

Example:
    Input:  "ababcbacadefegdehijhklij"
    Output: [9, 7, 8]

Idea: precompute, for every character, the *last* index it occurs at
in the whole string - that's the earliest a partition boundary could
possibly be placed if this character has been seen in the current
piece. Then scan left to right, extending the current piece's `end`
to cover the last occurrence of every character encountered so far
(same "extend to cover everything currently active" idea as
`11_graphs/10_pacific_atlantic_water_flow`'s multi-source reasoning,
just in 1D). The moment the scan position `i` reaches `end`, every
character seen in this piece has had its last occurrence accounted
for - none of them can appear again later, so it's safe to close the
partition here and start a new one.
"""


def partition_labels(s: str) -> list[int]:
    last_occurrence = {ch: i for i, ch in enumerate(s)}
    result = []
    start = end = 0

    for i, ch in enumerate(s):
        end = max(end, last_occurrence[ch])
        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


if __name__ == "__main__":
    tests = [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
        ("abc", [1, 1, 1]),
    ]

    for i, (s, expected) in enumerate(tests, 1):
        got = partition_labels(s)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
