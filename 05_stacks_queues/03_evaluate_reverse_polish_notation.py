"""
Problem: Evaluate an arithmetic expression given in Reverse Polish
(postfix) Notation. Tokens are integers or one of + - * /.
Source : LeetCode 150 - Evaluate Reverse Polish Notation

Example:
    Input:  ["2", "1", "+", "3", "*"]
    Output: 9   ((2 + 1) * 3)

Idea: postfix notation is exactly what a stack-based evaluator is
for - by the time an operator is read, its two operands are already
on top of the stack (in the order they were pushed), so applying the
operator is just: pop twice, compute, push the result back. No
parentheses or precedence rules are ever needed, which is the whole
appeal of postfix.
"""


def eval_rpn(tokens: list[str]) -> int:
    stack: list[int] = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # truncate toward zero, not floor
        else:
            stack.append(int(token))

    return stack[0]


if __name__ == "__main__":
    tests = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]

    for i, (tokens, expected) in enumerate(tests, 1):
        got = eval_rpn(tokens)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
