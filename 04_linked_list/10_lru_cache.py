"""
Problem: Design a Least Recently Used (LRU) cache with fixed
capacity, supporting get(key) and put(key, value) in O(1) time each.
get returns -1 if the key isn't present. put evicts the least
recently used entry when inserting would exceed capacity. Both get
and put count as "using" a key (move it to most-recently-used).
Source : LeetCode 146 - LRU Cache

Example:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)      -> 1   (1 is now most recently used)
    cache.put(3, 3)          (evicts 2, the least recently used)
    cache.get(2)      -> -1  (evicted)

Idea: this is the one problem in the folder needing a *doubly* linked
list, not singly. A dict alone gives O(1) key lookup but no notion of
recency order; a linked list alone gives O(1) reordering but no O(1)
key lookup. Combine them: the dict maps key -> node, and a doubly
linked list keeps nodes ordered by recency (most-recent right after a
sentinel head, least-recent right before a sentinel tail). Doubly
linked is required specifically because removing a node needs to
patch up both its neighbor's pointers in O(1) - a singly linked list
would need to walk from the head to find a node's predecessor first,
which breaks the O(1) guarantee.
"""


class _DListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> _DListNode
        self.head = _DListNode()  # sentinel, head.next = most recently used
        self.tail = _DListNode()  # sentinel, tail.prev = least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = _DListNode(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    cache = LRUCache(2)
    ops = [
        (cache.put, (1, 1), None),
        (cache.put, (2, 2), None),
        (cache.get, (1,), 1),
        (cache.put, (3, 3), None),   # evicts key 2
        (cache.get, (2,), -1),
        (cache.put, (4, 4), None),   # evicts key 1
        (cache.get, (1,), -1),
        (cache.get, (3,), 3),
        (cache.get, (4,), 4),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} ({fn.__name__}{args} -> got {got}, expected {expected})")
