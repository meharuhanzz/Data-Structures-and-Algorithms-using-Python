"""
Problem: Given the head of a singly linked list, return True if it
reads the same forwards and backwards. O(1) extra space (no copying
into an array).
Source : LeetCode 234 - Palindrome Linked List

Example:
    Input:  1 -> 2 -> 2 -> 1
    Output: True

Idea: combines three techniques from this folder in sequence:
  1. Find the middle (05's fast-slow trick).
  2. Reverse the second half in place (01's reversal trick).
  3. Walk the first half and the reversed second half together,
     comparing values - a palindrome check is just an equality check
     between a list and its own reverse.
This avoids O(n) extra space (no array copy) at the cost of
temporarily mutating the list's second half - acceptable here since
nothing else needs the original structure afterward.
"""

from list_node import to_linked_list


def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


if __name__ == "__main__":
    tests = [
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([1, 2, 3, 2, 1], True),
        ([], True),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = is_palindrome(to_linked_list(inp))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
