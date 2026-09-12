"""
Problem: Implement a FIFO queue using only two stacks (LIFO).
Support push, pop, peek, and empty.
Source : LeetCode 232 - Implement Queue using Stacks

Example:
    q = MyQueue()
    q.push(1); q.push(2)
    q.peek()  -> 1
    q.pop()   -> 1
    q.empty() -> False

Idea: two stacks, `in_stack` for incoming pushes and `out_stack` for
outgoing pops. Pushing is always cheap (just append to in_stack).
Popping/peeking needs the *oldest* element, which is at the *bottom*
of in_stack - reversing in_stack once into out_stack (via repeated
pop/push) puts it on top of out_stack. Only refill out_stack when
it's empty; otherwise its existing order is still correct. This
"lazy transfer" is what keeps amortized cost O(1) per operation - each
element is moved from in_stack to out_stack at most once in its
lifetime.
"""


class MyQueue:
    def __init__(self):
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _transfer_if_needed(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    ops = [
        (q.push, (1,), None),
        (q.push, (2,), None),
        (q.peek, (), 1),
        (q.pop, (), 1),
        (q.empty, (), False),
        (q.push, (3,), None),
        (q.push, (4,), None),
        (q.pop, (), 2),
        (q.pop, (), 3),
        (q.pop, (), 4),
        (q.empty, (), True),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} ({fn.__name__}{args} -> got {got}, expected {expected})")
