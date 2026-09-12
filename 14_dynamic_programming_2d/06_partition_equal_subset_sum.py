"""
Problem: Given an array of positive integers, determine if it can be
partitioned into two subsets with equal sum.
Source : LeetCode 416 - Partition Equal Subset Sum

Example:
    Input:  [1, 5, 11, 5]
    Output: True   ([1, 5, 5] and [11] both sum to 11)

Idea: not obviously a knapsack problem from the statement, but it is
one: if the total sum is odd, an equal split is impossible
immediately (no need to search at all). Otherwise, the question
becomes "does some subset sum to exactly total/2?" - which is 05's
knapsack with every item's *value equal to its weight* and capacity
set to target: "can capacity be filled exactly" instead of "what's
the best value that fits." Each number is an item, taken (included in
the subset) or skipped, same as 05 - just reframed as a boolean
reachability table (`dp[s]` = "is sum s achievable?") instead of a
value-maximization table. The space is rolled down to 1D here (unlike
05's explicit 2D table) by iterating the capacity dimension
*backward* for each item - the same "don't let one item update a
value that the same item might read again later in the same pass"
concern as `13_dynamic_programming_1d/06_coin_change_ii`'s loop-order
requirement, adapted to the 0/1 (no-reuse) setting.
"""


def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for n in nums:
        for s in range(target, n - 1, -1):
            if dp[s - n]:
                dp[s] = True

    return dp[target]


if __name__ == "__main__":
    tests = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([1, 1], True),
        ([1], False),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        got = can_partition(nums)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
