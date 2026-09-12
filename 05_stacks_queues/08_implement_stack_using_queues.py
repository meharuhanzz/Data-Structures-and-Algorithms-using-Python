"""
Problem: Implement a LIFO stack using only a queue (or queues).
Support push, pop, top, and empty.
Source : LeetCode 225 - Implement Stack using Queues

Example:
    s = MyStack()
    s.push(1); s.push(2)
    s.top()   -> 2
    s.pop()   -> 2

Idea: the mirror image of 07's problem. A single deque is enough:
after pushing a new element, rotate the queue by (size - 1) steps so
the just-pushed element moves to the *front*. That makes the queue's
front always equal to the most-recently-pushed element - i.e. LIFO
order - so pop/top just operate on the front like a normal queue
operation, no second data structure needed.
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q: deque = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q


if __name__ == "__main__":
    s = MyStack()
    ops = [
        (s.push, (1,), None),
        (s.push, (2,), None),
        (s.top, (), 2),
        (s.pop, (), 2),
        (s.empty, (), False),
        (s.push, (3,), None),
        (s.push, (4,), None),
        (s.pop, (), 4),
        (s.pop, (), 3),
        (s.pop, (), 1),
        (s.empty, (), True),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} ({fn.__name__}{args} -> got {got}, expected {expected})")
