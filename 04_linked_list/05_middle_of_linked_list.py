"""
Problem: Given the head of a singly linked list, return the middle
node. If there are two middle nodes (even length), return the
second one.
Source : LeetCode 876 - Middle of the Linked List

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: node with value 3

    Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6
    Output: node with value 4   (second of the two middles)

Idea: fast-slow pointers again, but this time the *destination*
itself (where slow ends up when fast runs out) is the answer, not a
meeting point. `fast` moves twice as fast as `slow`, so by the time
`fast` reaches the end, `slow` has covered exactly half the
distance - landing on the middle in a single pass, no need to count
the length first.
"""

from list_node import to_linked_list


def middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6], 4),
        ([1], 1),
        ([1, 2], 2),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got_node = middle_node(to_linked_list(inp))
        got = got_node.val if got_node else None
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
