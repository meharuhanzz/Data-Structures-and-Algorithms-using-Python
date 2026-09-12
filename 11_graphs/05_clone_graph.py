"""
Problem: Given a reference to a node in a connected undirected graph
(each node has a value and a list of neighbor references), return a
deep copy of the entire graph.
Source : LeetCode 133 - Clone Graph

Example:
    Input:  a graph 1 -- 2
                     |    |
                     4 -- 3
    Output: a structurally identical graph, entirely new node objects

Idea: the first problem in this folder on an explicit graph (nodes
with neighbor lists) instead of an implicit grid. Cloning requires
visiting every node exactly once despite cycles being possible (an
undirected graph's neighbor relationships go both ways, so a plain
DFS without tracking visited nodes would recurse forever). A dict
mapping original node -> its clone serves two purposes at once: it's
the visited-set (if a node is already a key, its clone already
exists and traversal shouldn't continue past it) and it's how a
node's neighbors get wired to the *already-created* clones of
whichever neighbors were visited first, rather than creating
duplicate clones for the same original node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    if not node:
        return None

    clones: dict[Node, Node] = {}

    def dfs(n: Node) -> Node:
        if n in clones:
            return clones[n]
        copy = Node(n.val)
        clones[n] = copy
        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)


def build_graph(adj_list: list[list[int]]) -> Node | None:
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbor_vals in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[v] for v in neighbor_vals]
    return nodes[1]


def to_adj_list(node: Node | None) -> list[list[int]]:
    if not node:
        return []
    visited: dict[int, Node] = {}

    def dfs(n: Node) -> None:
        if n.val in visited:
            return
        visited[n.val] = n
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)
    ordered = [visited[v] for v in sorted(visited)]
    return [[nb.val for nb in n.neighbors] for n in ordered]


if __name__ == "__main__":
    tests = [
        [[2, 4], [1, 3], [2, 4], [1, 3]],
        [[]],
        [],
    ]

    for i, adj_list in enumerate(tests, 1):
        original = build_graph(adj_list)
        clone = clone_graph(original)
        got = to_adj_list(clone)
        status = "PASS" if got == adj_list else "FAIL"
        identity_ok = clone is not original if original else True
        status = status if identity_ok else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {adj_list})")
