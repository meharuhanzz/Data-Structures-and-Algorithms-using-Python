r"""
Problem: Given the root of a BST and two nodes p and q known to
exist in it, find their lowest common ancestor (the deepest node
that has both p and q as descendants; a node can be its own
descendant).
Source : LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree

Example:
    BST:        6
              /   \
             2     8
            / \   / \
           0   4 7   9
              / \
             3   5
    LCA(2, 8) = 6
    LCA(2, 4) = 2

Idea: unlike the general-tree version (10_lowest_common_ancestor_
binary_tree), this can exploit the BST ordering property directly,
without exploring both subtrees. Starting at the root: if both p and
q are smaller than the current node, the LCA must be in the left
subtree (both are there); if both are larger, it must be in the
right subtree. The moment they're *not* both on the same side, the
current node is exactly the split point - and therefore the LCA -
since that's the deepest node from which p and q diverge. No
recursion into both branches needed, just a single walk down.
"""

from tree_node import build_tree, find_node


def lowest_common_ancestor(root, p, q):
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
    return None


if __name__ == "__main__":
    tree = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    tests = [
        (2, 8, 6),
        (2, 4, 2),
        (0, 5, 2),
        (7, 9, 8),
    ]

    for i, (p_val, q_val, expected_val) in enumerate(tests, 1):
        p, q = find_node(tree, p_val), find_node(tree, q_val)
        got = lowest_common_ancestor(tree, p, q)
        got_val = got.val if got else None
        status = "PASS" if got_val == expected_val else "FAIL"
        print(f"Test {i}: {status} (LCA({p_val}, {q_val}) -> got {got_val}, expected {expected_val})")
