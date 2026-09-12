"""
Problem: Given an integer array `nums` and integer k, return the k
most frequent elements.
Source : LeetCode 347 - Top K Frequent Elements

Example:
    Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

Idea: sorting all (value, freq) pairs by frequency is O(n log n).
Bucket sort does it in O(n): frequency can never exceed len(nums), so
make a list of buckets indexed by frequency, drop each value into
bucket[its frequency], then read buckets from highest frequency down
until k values are collected.
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts: dict[int, int] = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result


if __name__ == "__main__":
    tests = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 4, 4, 6, 6, 6, 1], 2, [4, 6]),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        got = top_k_frequent(nums, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
