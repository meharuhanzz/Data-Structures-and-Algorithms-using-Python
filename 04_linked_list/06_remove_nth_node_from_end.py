"""
Problem: Given the head of a linked list, remove the nth node from
the end of the list and return the head. One pass.
Source : LeetCode 19 - Remove Nth Node From End of List

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5

Idea: two pointers held `n` nodes apart. Advance `fast` n steps first
to create the gap, then advance both together until `fast` falls off
the end - at that point `slow` sits exactly at the node *before* the
one that needs removing. A dummy node before `head` handles the edge
case of removing the head itself uniformly, so no separate "is this
the first node" branch is needed.
"""

from list_node import ListNode, to_linked_list, to_python_list


def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
    ]

    for i, (inp, n, expected) in enumerate(tests, 1):
        got = to_python_list(remove_nth_from_end(to_linked_list(inp), n))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
