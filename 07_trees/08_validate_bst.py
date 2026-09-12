"""
Problem: Given the root of a binary tree, determine if it is a valid
binary search tree (every node's value strictly greater than all
values in its left subtree and strictly less than all values in its
right subtree - not just compared to its immediate children).
Source : LeetCode 98 - Validate Binary Search Tree

Example:
    Input:      5
               / \
              1   4
                 / \
                3   6
    Output: False  (4's left child 3 is fine locally, but 3 also sits
                     in 5's right subtree and must be > 5, which it
                     isn't - a check against immediate parents only
                     would miss this)

Idea: checking each node against only its direct parent is the
classic wrong approach - it misses violations further up the tree,
as in the example above. Instead, carry a valid (low, high) range
down through the recursion: the root can be anything, but each left
child tightens the range's upper bound to the parent's value, and
each right child tightens the lower bound. A node is valid only if
its value falls strictly inside the range accumulated from *every*
ancestor, not just its immediate parent.
"""

from tree_node import build_tree


def is_valid_bst(root):
    def validate(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    tests = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([], True),
        ([1], True),
        ([5, 4, 6, None, None, 3, 7], False),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = is_valid_bst(build_tree(inp))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
