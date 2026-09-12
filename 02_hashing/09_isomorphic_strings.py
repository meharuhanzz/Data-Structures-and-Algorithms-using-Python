"""
Problem: Given two strings s and t, return True if s can be
transformed into t by replacing every occurrence of each character
in s with another character. Mapping must be one-to-one in both
directions (no two source chars map to the same target char).
Source : LeetCode 205 - Isomorphic Strings

Example:
    Input:  s = "egg", t = "add"
    Output: True   (e->a, g->d)

    Input:  s = "foo", t = "bar"
    Output: False  (o would need to map to both a and r)

Idea: a single s->t dict isn't enough - it misses the case where two
different source characters both map to the same target character
(mapping must be a bijection, not just a function). Keep two dicts,
one per direction, and check both stay consistent at every step.
"""


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_st: dict[str, str] = {}
    map_ts: dict[str, str] = {}

    for cs, ct in zip(s, t):
        if cs in map_st and map_st[cs] != ct:
            return False
        if ct in map_ts and map_ts[ct] != cs:
            return False
        map_st[cs] = ct
        map_ts[ct] = cs

    return True


if __name__ == "__main__":
    tests = [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
    ]

    for i, (s, t, expected) in enumerate(tests, 1):
        got = is_isomorphic(s, t)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
