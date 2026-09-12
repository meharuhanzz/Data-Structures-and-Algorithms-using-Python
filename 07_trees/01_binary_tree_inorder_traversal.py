"""
Problem: Given the root of a binary tree, return its inorder
traversal (left, node, right) as a list of values. Do it iteratively
(no recursion), to practice the technique explicitly rather than
relying on the call stack to do it implicitly.
Source : LeetCode 94 - Binary Tree Inorder Traversal

Example:
    Input:      1
                 \
                  2
                 /
                3
    Output: [1, 3, 2]

Idea: recursive inorder is trivial (`inorder(left); visit(node);
inorder(right)`), but that's really using the *call stack* as an
implicit stack. Making it explicit: push every left-child down a
chain onto a stack first (mirrors "go as far left as possible"),
then pop one, visit it, and repeat the same "push everything on the
left chain" process starting from its right child. This same
explicit-stack-instead-of-recursion swap generalizes to preorder and
postorder too.
"""

from tree_node import build_tree


def inorder_traversal(root):
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


if __name__ == "__main__":
    tests = [
        ([1, None, 2, 3], [1, 3, 2]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [4, 2, 5, 1, 3]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = inorder_traversal(build_tree(inp))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
