"""
Problem: Given the heads of two singly linked lists, return the node
at which they intersect (share the exact same node onward), or None
if they don't intersect. O(1) extra space.
Source : LeetCode 160 - Intersection of Two Linked Lists

Example:
    listA-only: 4 -> 1 -\
                         6 -> 8 -> 4 -> 5   (shared tail)
    listB-only: 5 -> 6 -/
    Output: the node with value 6 (start of the shared tail)

Idea: if listA has length a and listB has length b, and they share a
tail of length c, then walking A-then-B covers (a + b) total nodes,
and so does walking B-then-A. Both walks end up traversing the exact
same total distance, so if you switch a pointer to the *other* list's
head the instant it hits the end of its own list, both pointers
arrive at the intersection point (or both hit None simultaneously,
if there is none) at the same step - no need to compute lengths or
alignment offsets up front.
"""

from list_node import ListNode


def get_intersection_node(head_a, head_b):
    if not head_a or not head_b:
        return None

    a, b = head_a, head_b
    while a is not b:
        a = a.next if a else head_b
        b = b.next if b else head_a

    return a


def _build_intersection(list_a_only, list_b_only, common):
    common_head = None
    common_tail = None
    for v in common:
        node = ListNode(v)
        if common_head is None:
            common_head = node
        else:
            common_tail.next = node
        common_tail = node

    def _prepend(values, tail):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        curr.next = tail
        return dummy.next

    return _prepend(list_a_only, common_head), _prepend(list_b_only, common_head), common_head


if __name__ == "__main__":
    tests = [
        ([4, 1], [5, 6, 1], [8, 4, 5]),
        ([2, 6, 4], [1, 5], []),
        ([1], [], []),
    ]

    for i, (a_only, b_only, common) in enumerate(tests, 1):
        head_a, head_b, expected_node = _build_intersection(a_only, b_only, common)
        got = get_intersection_node(head_a, head_b)
        status = "PASS" if got is expected_node else "FAIL"
        got_val = got.val if got else None
        expected_val = expected_node.val if expected_node else None
        print(f"Test {i}: {status} (got {got_val}, expected {expected_val})")
