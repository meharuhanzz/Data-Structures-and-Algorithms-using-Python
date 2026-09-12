"""
Problem: Given the root of a binary tree, return its level-order
traversal - a list of lists, one per depth level, left to right.
Source : LeetCode 102 - Binary Tree Level Order Traversal

Example:
    Input:      3
               / \
              9   20
                  / \
                 15  7
    Output: [[3], [9, 20], [15, 7]]

Idea: every other traversal in this folder so far is depth-first
(recursion or an explicit stack). Level order is breadth-first,
which needs a queue instead - process one full level of the queue at
a time by snapshotting `len(queue)` *before* the inner loop starts
(since pushing that level's children during the loop would otherwise
grow the count being iterated over and blur level boundaries).
"""

from collections import deque

from tree_node import build_tree


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


if __name__ == "__main__":
    tests = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = level_order(build_tree(inp))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
