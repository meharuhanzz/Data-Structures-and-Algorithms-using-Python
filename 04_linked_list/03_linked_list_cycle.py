"""
Problem: Given the head of a linked list, determine if it has a
cycle (some node's `.next` eventually points back to an earlier
node), using O(1) extra space.
Source : LeetCode 141 - Linked List Cycle

Example:
    Input:  3 -> 2 -> 0 -> -4 -> (back to node with value 2)
    Output: True

Idea: Floyd's cycle detection (fast-slow pointers), first previewed
in 03_two_pointers_sliding_window/10_find_the_duplicate_number on a
plain array. Same idea here on real nodes: if a cycle exists, the
fast pointer (2 steps/iteration) will eventually lap the slow pointer
(1 step/iteration) inside the loop and they'll land on the same node.
If the list is acyclic, `fast` simply reaches the end (None) first.
"""

from list_node import ListNode


def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def _build_cyclic(values, pos):
    """pos = index the tail connects back to, or -1 for no cycle."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    tests = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1, 2, 3], -1, False),
    ]

    for i, (values, pos, expected) in enumerate(tests, 1):
        head = _build_cyclic(values, pos)
        got = has_cycle(head)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
