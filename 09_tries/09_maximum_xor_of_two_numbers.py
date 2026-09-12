"""
Problem: Given an integer array nums, return the maximum possible
XOR of any two numbers in it.
Source : LeetCode 421 - Maximum XOR of Two Numbers in an Array

Example:
    Input:  [3, 10, 5, 25, 2, 8]
    Output: 28   (5 XOR 25 = 28)

Idea: a trie doesn't have to store characters - it can store the
*bits* of a number, one level per bit, from most significant to
least. Every number becomes a fixed-length root-to-leaf path of 0s
and 1s. Insert every number's bit-path into the trie first. Then for
each number, greedily walk the trie trying, at every bit, to go
toward the *opposite* bit of the current number - XOR-ing opposite
bits produces a 1 in that position, maximizing the result from the
most significant bit downward (the greedy choice is safe because a 1
in a higher bit position always beats any combination of lower
bits). If the opposite branch doesn't exist, fall back to the same
bit (contributing a 0 there) and keep going. This finds, for every
number, its best XOR partner in O(bit_length) instead of comparing
all O(n^2) pairs.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[int, "TrieNode"] = {}


def find_maximum_xor(nums: list[int]) -> int:
    if not nums:
        return 0

    max_bits = max(nums).bit_length()
    root = TrieNode()

    for n in nums:
        node = root
        for i in range(max_bits - 1, -1, -1):
            bit = (n >> i) & 1
            node = node.children.setdefault(bit, TrieNode())

    best = 0
    for n in nums:
        node = root
        curr_xor = 0
        for i in range(max_bits - 1, -1, -1):
            bit = (n >> i) & 1
            toggled = 1 - bit
            if toggled in node.children:
                curr_xor = (curr_xor << 1) | 1
                node = node.children[toggled]
            else:
                curr_xor = curr_xor << 1
                node = node.children[bit]
        best = max(best, curr_xor)

    return best


if __name__ == "__main__":
    tests = [
        ([3, 10, 5, 25, 2, 8], 28),
        ([0], 0),
        ([2, 4], 6),
        ([8, 10, 2], 10),
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        got = find_maximum_xor(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
