"""
Problem: Given an array of strings, group the anagrams together.
Return the groups in any order (order within a group also doesn't
matter for grading here).
Source : LeetCode 49 - Group Anagrams

Example:
    Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Idea: anagrams share the same character multiset, so sorting a
string's characters gives a canonical key that's identical for every
anagram of it. Use that sorted string as a dict key and bucket
originals under it.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}

    for s in strs:
        key = "".join(sorted(s))
        groups.setdefault(key, []).append(s)

    return list(groups.values())


def _normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    tests = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = group_anagrams(inp)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
