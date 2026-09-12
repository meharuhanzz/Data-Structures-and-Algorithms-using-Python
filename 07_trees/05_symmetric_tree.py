r"""
Problem: Given the root of a binary tree, check whether it is a
mirror of itself (symmetric around its center).
Source : LeetCode 101 - Symmetric Tree

Example:
    Input:      1
               / \
              2   2
             / \ / \
            3  4 4  3
    Output: True

Idea: symmetry means the left subtree is a *mirror image* of the
right subtree, not just an equal copy. Compare two subtrees at once,
checking outer-with-outer and inner-with-inner: `a.left` against
`b.right`, and `a.right` against `b.left`. This is structurally
different from a plain "are these two trees identical" check (which
would compare `a.left` to `b.left`) - the swap is the entire point.
"""

from tree_node import build_tree


def is_symmetric(root):
    def is_mirror(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return (
            a.val == b.val
            and is_mirror(a.left, b.right)
            and is_mirror(a.right, b.left)
        )

    return is_mirror(root.left, root.right) if root else True


if __name__ == "__main__":
    tests = [
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([], True),
        ([1], True),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = is_symmetric(build_tree(inp))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
