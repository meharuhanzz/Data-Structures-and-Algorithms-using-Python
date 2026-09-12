"""
Problem: Given a dictionary of root words and a sentence, replace
every word in the sentence with its shortest matching root from the
dictionary, if one exists (a word is replaceable if some dictionary
root is a prefix of it). Words with no matching root are left as-is.
Source : LeetCode 648 - Replace Words

Example:
    Input:  dictionary = ["cat", "bat", "rat"],
            sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"

Idea: build a trie from the dictionary roots, then for each word in
the sentence, walk it character by character down the trie - the
*first* `is_end` node hit along that walk is necessarily the
shortest matching root (any root found earlier in the walk is, by
definition, shorter than one found later). Stop as soon as either a
root is found or the trie runs out of matching children (no root
applies, keep the original word).
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


def replace_words(dictionary: list[str], sentence: str) -> str:
    root = TrieNode()
    for word in dictionary:
        node = root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def find_root(word: str) -> str:
        node = root
        prefix_chars = []
        for ch in word:
            if ch not in node.children:
                break
            node = node.children[ch]
            prefix_chars.append(ch)
            if node.is_end:
                return "".join(prefix_chars)
        return word

    return " ".join(find_root(w) for w in sentence.split())


if __name__ == "__main__":
    tests = [
        (["cat", "bat", "rat"], "the cattle was rattled by the battery",
         "the cat was rat by the bat"),
        (["a", "b", "c"], "aadsfasf absbs bbab cadsfafs", "a a b c"),
        (["catt", "cat", "bat", "rat"], "the cattle was rattled by the battery",
         "the cat was rat by the bat"),
    ]

    for i, (dictionary, sentence, expected) in enumerate(tests, 1):
        got = replace_words(dictionary, sentence)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got!r}, expected {expected!r})")
