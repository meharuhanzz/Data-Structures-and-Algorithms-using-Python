"""
Problem: Given the root of a binary tree, return its maximum depth
(the number of nodes along the longest path from root to a leaf).
Source : LeetCode 104 - Maximum Depth of Binary Tree

Example:
    Input:      3
               / \
              9   20
                  / \
                 15  7
    Output: 3

Idea: the simplest possible tree recursion, and the template every
later "compute something about a subtree" problem in this folder
builds on. A tree's depth is 1 (for the current node) plus whichever
child subtree is deeper - recursion handles "how deep is this
subtree" identically at every level, bottoming out at an empty
subtree having depth 0.
"""

from tree_node import build_tree


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    tests = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = max_depth(build_tree(inp))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
