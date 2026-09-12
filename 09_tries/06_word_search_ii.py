"""
Problem: Given an m x n grid of letters and a list of words, return
all words from the list that can be formed by a path of adjacent
cells (up/down/left/right, no cell reused within one word).
Source : LeetCode 212 - Word Search II

Example:
    board = [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]]
    words = ["oath", "pea", "eat", "rain"]
    Output: ["eat", "oath"]

Idea: searching for each word separately with its own DFS would
re-walk shared prefixes of the grid over and over (e.g. every word
starting with the same letters retraces the same early cells). Instead,
build one trie from *all* words first, then do a single DFS per
starting cell that walks the trie and the grid *in lockstep together*
- at each cell, only step to a neighbor if that neighbor's letter
exists as a child in the current trie node, pruning any path that no
word could possibly complete. Storing the full word at its terminal
trie node (instead of just an `is_end` flag) means a match is found
directly with no need to reconstruct it from the path. Temporarily
marking a visited cell (`'#'`) prevents reuse within one path, undone
on backtrack so other paths can still use that cell.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.word: str | None = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.word = w

    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r: int, c: int, node: TrieNode) -> None:
        ch = board[r][c]
        if ch not in node.children:
            return
        next_node = node.children[ch]
        if next_node.word:
            found.add(next_node.word)

        board[r][c] = "#"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, next_node)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return list(found)


if __name__ == "__main__":
    tests = [
        ([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
         ["oath", "pea", "eat", "rain"], {"eat", "oath"}),
        ([["a", "b"], ["c", "d"]], ["abcb"], set()),
    ]

    for i, (board, words, expected) in enumerate(tests, 1):
        got = set(find_words(board, words))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
