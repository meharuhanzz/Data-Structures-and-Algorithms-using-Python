"""
Problem: Given the root of a binary tree, return the length (number
of edges) of the longest path between any two nodes. The path does
not need to pass through the root.
Source : LeetCode 543 - Diameter of Binary Tree

Example:
    Input:      1
               / \
              2   3
             / \
            4   5
    Output: 3   (path 4 -> 2 -> 1 -> 3, or 5 -> 2 -> 1 -> 3)

Idea: the diameter *through* any given node equals the sum of its
left and right subtree heights - and the overall answer is the best
such sum seen at *any* node, not necessarily the root (that's why
the path "does not need to pass through the root"). Rather than
computing heights and diameter as two separate traversals, compute
them together in one pass: the height function (identical to 02's
max_depth) updates a `diameter` variable as a side effect every time
it's called, capturing "the best diameter seen so far through the
current node" while still returning the height needed by the
caller's own diameter calculation one level up.
"""

from tree_node import build_tree


def diameter_of_binary_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        diameter = max(diameter, left_h + right_h)
        return 1 + max(left_h, right_h)

    height(root)
    return diameter


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([], 0),
        ([1], 0),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = diameter_of_binary_tree(build_tree(inp))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
