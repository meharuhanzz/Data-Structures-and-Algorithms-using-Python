"""
Problem: Implement a Union-Find (Disjoint Set Union) structure
supporting find(x) (which set does x belong to), union(x, y) (merge
the sets containing x and y, returning False if they were already in
the same set - i.e. the edge (x, y) would create a cycle), and
tracking the current number of disjoint sets.
Source : foundational structure, used throughout this folder (not a
         single numbered LeetCode problem)

Example:
    uf = UnionFind(5)
    uf.union(0, 1)      -> True   (merged into one set)
    uf.union(1, 2)      -> True
    uf.connected(0, 2)  -> True   (both in the same set now)
    uf.union(0, 2)      -> False  (already connected - redundant edge)
    uf.count            -> 3      ({0,1,2}, {3}, {4})

Idea: every node starts as its own parent (its own set). find(x)
walks up parent pointers until it hits a node that's its own parent
(the set's "root" / representative), with *path compression* -
every node visited along the way gets repointed directly to the root
- so future find() calls on those nodes are O(1). union(x, y) finds
both roots; if they're already equal, x and y are already connected
(this is exactly how 02's redundant-connection detection works - the
first edge whose endpoints are already connected is the one creating
a cycle). Otherwise, attach the smaller-rank tree under the
larger-rank one ("union by rank") to keep trees shallow. Together,
path compression and union by rank give near-O(1) amortized find/
union - the reason Union-Find beats a plain DFS-based connectivity
check when there are many union/find queries interleaved.
"""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    uf = UnionFind(5)
    ops = [
        (uf.union, (0, 1), True),
        (uf.union, (1, 2), True),
        (uf.connected, (0, 2), True),
        (uf.union, (0, 2), False),
        (lambda: uf.count, (), 3),
        (uf.union, (3, 4), True),
        (lambda: uf.count, (), 2),
        (uf.connected, (0, 4), False),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
