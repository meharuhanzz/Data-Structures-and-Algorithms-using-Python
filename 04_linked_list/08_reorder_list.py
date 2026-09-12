"""
Problem: Given the head of a singly linked list L0 -> L1 -> ... ->
Ln-1 -> Ln, reorder it in place to:
    L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
Source : LeetCode 143 - Reorder List

Example:
    Input:  1 -> 2 -> 3 -> 4
    Output: 1 -> 4 -> 2 -> 3

Idea: three steps, each one reused from earlier in this folder:
  1. Find the middle (05) and split the list into two halves.
  2. Reverse the second half (01).
  3. Merge the two halves by alternating nodes from each - similar
     shape to 02's merge, but here it's a strict alternation instead
     of a comparison-driven merge, since the two halves aren't sorted
     relative to each other.
Modifies the list in place; returns nothing (matches LeetCode's
"do not return anything" signature convention for in-place problems).
"""

from list_node import to_linked_list, to_python_list


def reorder_list(head):
    if not head or not head.next:
        return

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    prev = None
    curr = second
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev

    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        head = to_linked_list(inp)
        reorder_list(head)
        got = to_python_list(head)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
