"""
Problem: Given a list of words, find the longest word that can be
built one character at a time by other words in the list (i.e. every
prefix of it, at every length, is also present in the list). If
there's a tie in length, return the lexicographically smallest.
Source : LeetCode 720 - Longest Word in Dictionary

Example:
    Input:  ["w", "wo", "wor", "worl", "world"]
    Output: "world"   (every prefix - w, wo, wor, worl - is present)

Idea: build a trie from all words, marking `is_end` on the node for
each complete word. Then DFS from the root, but with a constraint
not seen in 01-03: only descend into a child if that child's node is
itself `is_end` - meaning a word ending exactly there is also in the
list. This directly encodes "buildable one character at a time" as a
traversal rule, rather than checking all prefixes separately for
each candidate word. Visiting children in sorted character order
means the first-found longest word is automatically the
lexicographically smallest tie-breaker too.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


def longest_word(words: list[str]) -> str:
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    best = ""

    def dfs(node: TrieNode, path: list[str]) -> None:
        nonlocal best
        word = "".join(path)
        if len(word) > len(best) or (len(word) == len(best) and word < best):
            best = word
        for ch in sorted(node.children):
            child = node.children[ch]
            if child.is_end:
                path.append(ch)
                dfs(child, path)
                path.pop()

    dfs(root, [])
    return best


if __name__ == "__main__":
    tests = [
        (["w", "wo", "wor", "worl", "world"], "world"),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
        (["a"], "a"),
    ]

    for i, (words, expected) in enumerate(tests, 1):
        got = longest_word(words)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got!r}, expected {expected!r})")
