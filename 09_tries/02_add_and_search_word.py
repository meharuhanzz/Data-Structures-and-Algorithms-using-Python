"""
Problem: Design a data structure supporting add_word(word) and
search(word), where search's word may contain '.' as a wildcard
matching any single character.
Source : LeetCode 211 - Design Add and Search Words Data Structure

Example:
    wd = WordDictionary()
    wd.add_word("bad"); wd.add_word("dad"); wd.add_word("mad")
    wd.search("pad")  -> False
    wd.search("bad")  -> True
    wd.search(".ad")  -> True
    wd.search("b..")  -> True

Idea: same trie as 01 for storage, but search can no longer be a
simple single-path walk, because '.' means "try every branch here."
That turns search into a DFS: at a normal character, follow the one
matching child (or fail if it doesn't exist, same as before); at a
'.', recursively try *every* child and succeed if any of them lead to
a full match. This is exhaustive backtracking bounded by the trie's
branching factor, not a full re-scan of all stored words.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    wd = WordDictionary()
    ops = [
        (wd.add_word, ("bad",), None),
        (wd.add_word, ("dad",), None),
        (wd.add_word, ("mad",), None),
        (wd.search, ("pad",), False),
        (wd.search, ("bad",), True),
        (wd.search, (".ad",), True),
        (wd.search, ("b..",), True),
        (wd.search, ("....",), False),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} ({fn.__name__}{args} -> got {got}, expected {expected})")
