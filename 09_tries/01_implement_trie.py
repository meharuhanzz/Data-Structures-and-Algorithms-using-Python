"""
Problem: Implement a trie (prefix tree) with insert(word),
search(word) (exact match), and starts_with(prefix) (prefix match).
Source : LeetCode 208 - Implement Trie (Prefix Tree)

Example:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")     -> True
    trie.search("app")       -> False   (only a prefix, not inserted)
    trie.starts_with("app")  -> True
    trie.insert("app")
    trie.search("app")       -> True

Idea: the foundational data structure for this whole folder. Each
node holds a dict mapping character -> child node, plus a flag
marking "a complete word ends here." Shared prefixes across inserted
words share the same chain of nodes automatically - "apple" and "app"
share the nodes for a-p-p, and only "apple" continues past that. This
is what makes a trie efficient for anything involving many strings
that share prefixes: shared work is done once, not once per string.
search() and starts_with() differ by exactly one thing: search()
additionally requires the final node's `is_end` flag to be set (the
string must be a complete inserted word, not just a path that
happens to exist because it's a prefix of something longer).
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def _find(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    ops = [
        (trie.insert, ("apple",), None),
        (trie.search, ("apple",), True),
        (trie.search, ("app",), False),
        (trie.starts_with, ("app",), True),
        (trie.insert, ("app",), None),
        (trie.search, ("app",), True),
        (trie.search, ("appl",), False),
        (trie.starts_with, ("b",), False),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} ({fn.__name__}{args} -> got {got}, expected {expected})")
