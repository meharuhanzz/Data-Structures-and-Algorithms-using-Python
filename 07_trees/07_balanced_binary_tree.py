"""
Problem: Given the root of a binary tree, determine if it is
height-balanced: for every node, the heights of its left and right
subtrees differ by at most 1.
Source : LeetCode 110 - Balanced Binary Tree

Example:
    Input:      3
               / \
              9   20
                  / \
                 15  7
    Output: True

Idea: the naive approach recomputes height from scratch at every
node while also checking balance, giving O(n^2) in the worst case
(a skewed tree). Better: reuse 02's height computation, but make it
return -1 as a sentinel the instant any subtree below is found
unbalanced, and propagate that -1 upward immediately without doing
any more work. Every node's height is then computed exactly once
(O(n) total), and an early -1 short-circuits the rest of the tree
once imbalance is already known - no need to check nodes above it.
"""

from tree_node import build_tree


def is_balanced(root):
    def height(node):
        if not node:
            return 0

        left_h = height(node.left)
        if left_h == -1:
            return -1

        right_h = height(node.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1

        return 1 + max(left_h, right_h)

    return height(root) != -1


if __name__ == "__main__":
    tests = [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),
        ([1], True),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = is_balanced(build_tree(inp))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
