"""
Problem: Customers pay for a $5 lemonade with a $5, $10, or $20 bill,
in the order given by `bills`. You start with no change. Return True
if every customer can be given correct change.
Source : LeetCode 860 - Lemonade Change

Example:
    Input:  [5, 5, 5, 10, 20]
    Output: True

Idea: the simplest possible greedy - at each step there's often only
one *possible* choice, and where there's a real choice (making change
for a $20: either one $10 + one $5, or three $5s), always prefer
spending the *less flexible* bill first. A $10 bill is only ever
useful for making change for a $20 - it can't help a future $10
customer. A $5 bill can make change for *either* a $10 or a $20. So
when both options are available, spend the $10 (keep the more
versatile $5s in reserve) - a greedy choice that's provably never
worse than the alternative, since nothing is lost by keeping the more
flexible resource around longer.
"""


def lemonade_change(bills: list[int]) -> bool:
    five = ten = 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True


if __name__ == "__main__":
    tests = [
        ([5, 5, 5, 10, 20], True),
        ([5, 5, 10, 10, 20], False),
        ([5, 5, 10], True),
        ([10, 10], False),
    ]

    for i, (bills, expected) in enumerate(tests, 1):
        got = lemonade_change(bills)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
