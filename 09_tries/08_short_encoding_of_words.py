"""
Problem: A valid encoding of a list of words is a reference string
built by concatenating each word followed by '#', where every word
in the list appears as a *suffix* of some entry in the reference
(so a word doesn't need its own entry if it's already a suffix of a
longer word already included). Return the length of the shortest
possible valid encoding.
Source : LeetCode 820 - Short Encoding of Words

Example:
    Input:  ["time", "me", "bell"]
    Output: 10   ("time#bell#" - "me" is a suffix of "time", so it
                   doesn't need its own entry)

Idea: "is a suffix of" on normal words becomes "is a *prefix* of" if
every word is reversed first - and prefix relationships are exactly
what a trie represents naturally (shared prefixes share nodes). Build
a trie from all *reversed* words. A word only needs its own encoding
entry if no other word extends past it in the trie - i.e. its
reversed-word node has no children (a leaf). Any word whose node
*does* have children is a suffix of some longer word already covered
by that longer word's own entry, so it contributes nothing extra.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}


def minimum_length_encoding(words: list[str]) -> int:
    words = list(set(words))  # exact duplicates never need re-encoding
    root = TrieNode()
    node_for_word = {}

    for w in words:
        node = root
        for ch in reversed(w):
            node = node.children.setdefault(ch, TrieNode())
        node_for_word[w] = node

    total = 0
    for w in words:
        if not node_for_word[w].children:  # leaf: not a suffix of any other word
            total += len(w) + 1

    return total


if __name__ == "__main__":
    tests = [
        (["time", "me", "bell"], 10),
        (["t"], 2),
        (["time", "me"], 5),
        (["a", "aa", "aaa"], 4),
    ]

    for i, (words, expected) in enumerate(tests, 1):
        got = minimum_length_encoding(words)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
