"""
Shared ListNode definition and helpers for the linked list problems in
this folder. Not a problem itself - just plumbing so each problem file
can focus on the algorithm instead of list-building boilerplate.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def to_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_python_list(head, limit=10000):
    result = []
    while head and len(result) < limit:
        result.append(head.val)
        head = head.next
    return result
