r"""
Problem: Given the root of a binary tree, invert it (mirror every
subtree - swap left and right children, recursively) and return the
root.
Source : LeetCode 226 - Invert Binary Tree

Example:
    Input:      4                  Output:      4
               / \                             / \
              2   7                           7   2
             / \ / \                         / \ / \
            1  3 6  9                       9  6 3  1

Idea: same recursive shape as 02, but instead of *computing* a value
from the subtrees, it *rebuilds* the tree from inverted subtrees.
Swap root.left and root.right using the recursively-inverted versions
of each - Python evaluates both `invert_tree(...)` calls before doing
the assignment, so there's no need for a temporary variable to avoid
overwriting one child before the other is inverted.
"""

from tree_node import build_tree, to_level_order


def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == "__main__":
    tests = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = to_level_order(invert_tree(build_tree(inp)))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
