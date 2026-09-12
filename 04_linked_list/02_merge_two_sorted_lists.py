"""
Problem: Given the heads of two sorted linked lists, merge them into
one sorted list by splicing together the existing nodes (no new
nodes), and return the head.
Source : LeetCode 21 - Merge Two Sorted Lists

Example:
    Input:  l1 = 1 -> 2 -> 4,  l2 = 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Idea: a dummy head sidesteps the "what's the first node" special case
- start `tail` at the dummy, always attach the smaller of the two
current nodes to `tail.next`, advance both `tail` and whichever list
contributed. Once one list runs out, the other is already sorted and
can just be attached wholesale.
"""

from list_node import ListNode, to_linked_list, to_python_list


def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


if __name__ == "__main__":
    tests = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([2], [1], [1, 2]),
    ]

    for i, (a, b, expected) in enumerate(tests, 1):
        got = to_python_list(merge_two_lists(to_linked_list(a), to_linked_list(b)))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
