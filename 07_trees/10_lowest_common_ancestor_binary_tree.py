r"""
Problem: Given the root of a general binary tree (no BST property)
and two nodes p and q known to exist in it, find their lowest common
ancestor.
Source : LeetCode 236 - Lowest Common Ancestor of a Binary Tree

Example:
    Tree:        3
               /   \
              5     1
             / \   / \
            6   2 0   8
               / \
              7   4
    LCA(5, 1) = 3
    LCA(5, 4) = 5

Idea: without BST ordering, there's no shortcut for which side to
search - both subtrees must be explored. Recurse into left and
right; a call returns the node itself the moment it *is* p or q (no
need to look further down that branch - a node can be its own
ancestor). If both the left and right recursive calls come back
non-None, that means p was found on one side and q on the other, so
the *current* node is exactly where their paths converge - the LCA.
If only one side returns non-None, both p and q must be in that same
subtree, so pass that result upward unchanged.
"""

from tree_node import build_tree, find_node


def lowest_common_ancestor(root, p, q):
    if not root or root is p or root is q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left or right


if __name__ == "__main__":
    tree = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    tests = [
        (5, 1, 3),
        (5, 4, 5),
        (6, 4, 5),
        (0, 8, 1),
    ]

    for i, (p_val, q_val, expected_val) in enumerate(tests, 1):
        p, q = find_node(tree, p_val), find_node(tree, q_val)
        got = lowest_common_ancestor(tree, p, q)
        got_val = got.val if got else None
        status = "PASS" if got_val == expected_val else "FAIL"
        print(f"Test {i}: {status} (LCA({p_val}, {q_val}) -> got {got_val}, expected {expected_val})")
