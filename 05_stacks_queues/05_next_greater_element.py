"""
Problem: nums1 is a subset of nums2 (all elements distinct). For each
element in nums1, find its next greater element to the right in
nums2, or -1 if none exists.
Source : LeetCode 496 - Next Greater Element I

Example:
    Input:  nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
    Output: [-1, 3, -1]

Idea: same monotonic-stack shape as 04_daily_temperatures, but here
the "gap" being recorded is the *value* at the resolving index rather
than the distance to it, and the answer only needs to be looked up
for the nums1 subset afterward - so the stack pass builds a
value -> next_greater dict over all of nums2 once, then nums1 just
does O(1) dict lookups.
"""


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    next_greater: dict[int, int] = {}
    stack: list[int] = []  # values, decreasing bottom to top

    for n in nums2:
        while stack and stack[-1] < n:
            next_greater[stack.pop()] = n
        stack.append(n)

    return [next_greater.get(n, -1) for n in nums1]


if __name__ == "__main__":
    tests = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
    ]

    for i, (nums1, nums2, expected) in enumerate(tests, 1):
        got = next_greater_element(nums1, nums2)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
