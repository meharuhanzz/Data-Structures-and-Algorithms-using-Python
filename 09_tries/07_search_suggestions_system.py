"""
Problem: Given a list of products and a search word, for every
prefix of search_word (built one character at a time as if the user
were typing), return up to 3 lexicographically smallest products
that have that prefix.
Source : LeetCode 1268 - Search Suggestions System

Example:
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = "mouse"
    Output: [
        ["mobile", "moneypot", "monitor"],   # prefix "m"
        ["mobile", "moneypot", "monitor"],   # prefix "mo"
        ["mouse", "mousepad"],               # prefix "mou"
        ["mouse", "mousepad"],               # prefix "mous"
        ["mouse", "mousepad"],               # prefix "mouse"
    ]

Idea: the "autocomplete" trie pattern - sort all products first, then
insert them into a trie in that sorted order, capping each node's
stored suggestion list at 3 entries. Because insertion happens in
sorted order and each node only *accepts* new entries while its list
has fewer than 3, every node's list ends up holding exactly the
(up to) 3 lexicographically smallest products passing through it -
no separate sort needed at query time. Answering the query is then
just walking the trie one character at a time along search_word and
reading off each node's precomputed list directly.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.suggestions: list[str] = []


def suggested_products(products: list[str], search_word: str) -> list[list[str]]:
    root = TrieNode()
    for p in sorted(products):
        node = root
        for ch in p:
            node = node.children.setdefault(ch, TrieNode())
            if len(node.suggestions) < 3:
                node.suggestions.append(p)

    result = []
    node = root
    for ch in search_word:
        if node is not None and ch in node.children:
            node = node.children[ch]
            result.append(node.suggestions)
        else:
            node = None
            result.append([])

    return result


if __name__ == "__main__":
    tests = [
        (["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse", [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ]),
        (["havana"], "havana", [["havana"]] * 6),
        (["bags", "baggage", "banner", "box", "cloths"], "bags", [
            ["baggage", "bags", "banner"],
            ["baggage", "bags", "banner"],
            ["baggage", "bags"],
            ["bags"],
        ]),
    ]

    for i, (products, word, expected) in enumerate(tests, 1):
        got = suggested_products(products, word)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
