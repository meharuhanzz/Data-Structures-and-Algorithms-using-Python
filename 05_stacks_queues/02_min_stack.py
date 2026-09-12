"""
Problem: Design a stack that supports push, pop, top, and retrieving
the minimum element, all in O(1) time.
Source : LeetCode 155 - Min Stack

Example:
    stack = MinStack()
    stack.push(-2); stack.push(0); stack.push(-3)
    stack.get_min()  -> -3
    stack.pop()
    stack.top()       -> 0
    stack.get_min()   -> -2

Idea: a single stack can't answer get_min() in O(1) after pops, since
the minimum could change with every pop and re-scanning is O(n).
Fix: keep a second, parallel stack where min_stack[i] always holds
"the minimum of the main stack's bottom i+1 elements." Every push
computes and stores that running minimum; every pop discards from
both stacks together, so min_stack[-1] is always instantly correct.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    stack = MinStack()
    ops = [
        (stack.push, (-2,), None),
        (stack.push, (0,), None),
        (stack.push, (-3,), None),
        (stack.get_min, (), -3),
        (stack.pop, (), None),
        (stack.top, (), 0),
        (stack.get_min, (), -2),
    ]

    for i, (fn, args, expected) in enumerate(ops, 1):
        got = fn(*args)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} ({fn.__name__}{args} -> got {got}, expected {expected})")
