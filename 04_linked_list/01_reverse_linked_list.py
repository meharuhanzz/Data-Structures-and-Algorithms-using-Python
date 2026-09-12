"""
Problem: Given the head of a singly linked list, reverse it and
return the new head.
Source : LeetCode 206 - Reverse Linked List

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

Idea: walk the list once, and at each node flip its `.next` pointer
to point backward instead of forward. `prev` tracks the already-
reversed portion; `next_node` must be saved *before* overwriting
`curr.next`, or the rest of the list becomes unreachable.
"""

from list_node import to_linked_list, to_python_list


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        head = to_linked_list(inp)
        got = to_python_list(reverse_list(head))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
