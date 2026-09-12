"""
Problem: Given the head of a linked list, return the node where the
cycle begins, or None if there is no cycle. O(1) extra space.
Source : LeetCode 142 - Linked List Cycle II

Example:
    Input:  3 -> 2 -> 0 -> -4 -> (back to node with value 2)
    Output: the node with value 2

Idea: two-phase Floyd's algorithm. Phase 1 (same as 03) finds a
meeting point somewhere inside the cycle - not necessarily its start.
Phase 2 uses the algorithm's key property: resetting one pointer to
`head` and advancing both pointers one step at a time from there,
they meet again exactly at the cycle's entrance. (Proof sketch: if
the entrance is `k` steps from head, the meeting point in phase 1 is
also `k` steps before the entrance when measured going around the
cycle - the math works out so both walks of length `k` land in the
same place.)
"""

from list_node import ListNode


def detect_cycle(head):
    slow = fast = head
    met = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            met = True
            break

    if not met:
        return None

    ptr = head
    while ptr is not slow:
        ptr = ptr.next
        slow = slow.next

    return ptr


def _build_cyclic(values, pos):
    if not values:
        return None, None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    entry = None
    if pos != -1:
        nodes[-1].next = nodes[pos]
        entry = nodes[pos]
    return nodes[0], entry


if __name__ == "__main__":
    tests = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1),
        ([], -1),
        ([1, 2, 3], -1),
    ]

    for i, (values, pos) in enumerate(tests, 1):
        head, expected_entry = _build_cyclic(values, pos)
        got = detect_cycle(head)
        status = "PASS" if got is expected_entry else "FAIL"
        got_val = got.val if got else None
        expected_val = expected_entry.val if expected_entry else None
        print(f"Test {i}: {status} (got {got_val}, expected {expected_val})")
