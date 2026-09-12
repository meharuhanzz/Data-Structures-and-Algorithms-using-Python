"""
Problem: Design WordFilter(words), supporting f(prefix, suffix):
return the largest index i such that words[i] has the given prefix
AND the given suffix (both simultaneously). Return -1 if none match.
Source : LeetCode 745 - Prefix and Suffix Search

Example:
    wf = WordFilter(["apple", "app"])
    wf.f("a", "e")  -> 0   ("apple" starts with 'a', ends with 'e')
    wf.f("a", "p")  -> 1   ("app" starts with 'a', ends with 'p')

Idea: 01-09 all trie on a *single* dimension per word (its prefix
structure alone). This problem needs "starts with X AND ends with Y"
simultaneously, which a plain prefix trie can't answer directly.
The trick: for each word, insert every one of its (suffix, word)
combinations as a *single combined key*: `suffix + "#" + word`, for
every possible suffix length. A query for (prefix, suffix) then
becomes a single ordinary trie lookup of `suffix + "#" + prefix` -
if that combined path exists in the trie, every word that passes
through it necessarily has both the required suffix (it's literally
the start of the key) and the required prefix (since the word
itself, appearing right after the '#', starts with it). Storing the
word's index at every node along each inserted path, overwritten in
increasing index order, means the last (largest) index naturally
survives at each node - exactly the tie-breaking rule the problem
asks for.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.index = -1


class WordFilter:
    def __init__(self, words: list[str]):
        self.root = TrieNode()
        for idx, word in enumerate(words):
            for j in range(len(word) + 1):
                key = word[j:] + "#" + word
                node = self.root
                node.index = idx
                for ch in key:
                    node = node.children.setdefault(ch, TrieNode())
                    node.index = idx

    def f(self, prefix: str, suffix: str) -> int:
        key = suffix + "#" + prefix
        node = self.root
        for ch in key:
            if ch not in node.children:
                return -1
            node = node.children[ch]
        return node.index


if __name__ == "__main__":
    wf = WordFilter(["apple", "app"])
    tests = [
        (("a", "e"), 0),
        (("a", "p"), 1),
        (("b", "e"), -1),
        (("app", "p"), 1),
    ]

    for i, ((prefix, suffix), expected) in enumerate(tests, 1):
        got = wf.f(prefix, suffix)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (f({prefix!r}, {suffix!r}) -> got {got}, expected {expected})")
