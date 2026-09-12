"""
Problem: Given a string s, rearrange its characters so that no two
adjacent characters are the same. Return any valid rearrangement, or
"" if impossible.
Source : LeetCode 767 - Reorganize String

Example:
    Input:  "aab"
    Output: "aba"   (any valid rearrangement is accepted)

Idea: greedily place the *most frequent remaining* character at each
position - a max-heap of (count, char), same negate trick as 01/06.
The subtlety is avoiding placing the same character twice in a row:
after popping and placing a character, don't push it straight back
(it might get popped again immediately if it's still the most
frequent) - instead hold it in `prev` for exactly one step, and push
it back only after the *next* character has been placed. This
guarantees at least one different character separates two uses of
the same letter. Impossible cases are detected up front: if the most
frequent character's count exceeds `(len(s) + 1) // 2`, it can't be
spread out enough no matter the arrangement.
"""

import heapq
from collections import Counter


def reorganize_string(s: str) -> str:
    counts = Counter(s)
    max_heap = [(-c, ch) for ch, c in counts.items()]
    heapq.heapify(max_heap)

    if max_heap and -max_heap[0][0] > (len(s) + 1) // 2:
        return ""

    result = []
    prev = None  # (count, char) of the previously placed character

    while max_heap:
        count, ch = heapq.heappop(max_heap)
        result.append(ch)
        if prev and prev[0] < 0:
            heapq.heappush(max_heap, prev)
        count += 1  # count is negative; +1 means "used one instance"
        prev = (count, ch)

    return "".join(result)


def _is_valid_reorganization(original: str, result: str) -> bool:
    if sorted(original) != sorted(result):
        return False
    return all(result[i] != result[i + 1] for i in range(len(result) - 1))


if __name__ == "__main__":
    tests = ["aab", "aaab", "vvvlo", "a", ""]
    expected_possible = [True, False, True, True, True]

    for i, (s, possible) in enumerate(zip(tests, expected_possible), 1):
        got = reorganize_string(s)
        if not possible:
            status = "PASS" if got == "" else "FAIL"
        else:
            status = "PASS" if _is_valid_reorganization(s, got) else "FAIL"
        print(f"Test {i}: {status} (input={s!r}, got {got!r})")
