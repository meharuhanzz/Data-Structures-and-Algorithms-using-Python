"""
Shared TreeNode definition and helpers for the tree problems in this
folder. Not a problem itself - just plumbing so each problem file can
focus on the algorithm instead of tree-building boilerplate.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree(values):
    """Build a binary tree from a LeetCode-style level-order list
    (None marks a missing child) and return the root."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)

    return root


def to_level_order(root):
    """Inverse of build_tree, for comparing results in tests. Trims
    trailing Nones so [1,2,None] and [1,2] compare equal."""
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


def find_node(root, val):
    """Look up a node by value, so tests can pass real TreeNode
    references (matching LeetCode's p/q signature) instead of values."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)
