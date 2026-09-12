"""
Problem: Design a structure supporting insert(key, val) (overwriting
val if key already exists) and sum(prefix) - the sum of vals for
every inserted key that starts with prefix.
Source : LeetCode 677 - Map Sum Pairs

Example:
    ms = MapSum()
    ms.insert("apple", 3)
    ms.sum("ap")          -> 3
    ms.insert("app", 2)
    ms.sum("ap")          -> 5

Idea: rather than storing values only at word-end nodes and summing
via a DFS over the subtree at query time (correct, but O(subtree
size) per query), store a running total *at every node along each
inserted key's path*, so sum(prefix) becomes a single O(len(prefix))
walk to the prefix's node and a direct read. The one subtlety:
overwriting an existing key must adjust every node on its path by
the *difference* between the new and old value (not just add the new
value again), so a separate `key_values` dict tracks each key's
current value for computing that delta.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.value = 0


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key_values: dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_values.get(key, 0)
        self.key_values[key] = val

        node = self.root
        node.value += delta
        for ch in key:
            node = node.children.setdefault(ch, TrieNode())
            node.value += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.value


if __name__ == "__main__":
    ms = MapSum()
    ops = [
        (ms.insert, ("apple", 3), None),
        (ms.sum, ("ap",), 3),
        (ms.insert, ("app", 2), None),
        (ms.sum, ("ap",), 5),
        (ms.insert, ("apple", 5), None),  # overwrite: 3 -> 5
        (ms.sum, ("ap",), 7),
        (ms.sum, ("b",), 0),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} ({fn.__name__}{args} -> got {got}, expected {expected})")
