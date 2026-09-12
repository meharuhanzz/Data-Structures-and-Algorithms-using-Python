"""
Problem: Given k sorted linked lists, merge them into one sorted
linked list.
Source : LeetCode 23 - Merge k Sorted Lists

Example:
    Input:  [[1,4,5], [1,3,4], [2,6]]
    Output: [1,1,2,3,4,4,5,6]

Idea: 04_linked_list/02_merge_two_sorted_lists merges *two* lists by
always taking whichever head is smaller. Merging k lists the same
way pairwise would cost O(kn) per level. Instead, keep the current
head of every list in a min-heap at once - the heap root is always
the smallest value across *all* k lists, so popping it and pushing
its successor keeps the invariant with O(log k) work per node
instead of O(k) work per node (comparing all k heads by hand).
A tuple (val, index, node) is pushed rather than the bare node,
because ListNode isn't comparable and two nodes could tie on value -
the unique `index` (which list it came from) breaks ties before
Python would ever try to compare two ListNode objects directly.
"""

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_python_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def merge_k_lists(lists: list) -> ListNode:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    tail = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


if __name__ == "__main__":
    tests = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1]], [1]),
    ]

    for i, (lists_vals, expected) in enumerate(tests, 1):
        lists = [to_linked_list(v) for v in lists_vals]
        got = to_python_list(merge_k_lists(lists))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
