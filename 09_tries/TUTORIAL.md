# Tries — Tutorial

Covers the 10 problems solved in this folder. A trie's core idea is
always the same: turn each item (a word, a number's bits, a combined
key) into a *path* through a tree, one symbol per edge, so that items
sharing a common prefix automatically share the same nodes for that
prefix. Every problem here is really "what do I store at/along that
path, and what do I do with the path once it's built" — the tree
structure itself barely changes.

## The patterns

### 1. The foundational structure (`01`)
A `TrieNode` is a dict of `character -> child node` plus a flag for
"a word ends here." `insert` walks/creates the path for a word;
`search` walks it and checks the end flag; `starts_with` walks it and
checks only that the path exists. Every other problem in this folder
is this same skeleton with something added: a different thing stored
at each node, a different traversal rule, or both.

### 2. Wildcard search via DFS instead of a single path walk (`02`)
Once a query can contain a wildcard, "walk the one matching path"
stops being enough — a `.` means "branch into every child here."
`add_and_search_word`'s `search` becomes a DFS: normal characters
narrow to one child as before, but `.` recursively tries every child
and succeeds if *any* branch leads to a match.

### 3. Stopping at the first match instead of the full path (`03`)
`replace_words` walks a word down the dictionary trie and returns as
soon as it hits an `is_end` node — not because the word ran out, but
because a *shorter* match was found and nothing shorter could exist
(anything found earlier in the walk is, by construction, shorter than
anything found later).

### 4. Constrained traversal — descend only where a rule allows (`04`)
`longest_word_in_dictionary` DFS's the trie, but only continues into
a child if that child is *itself* a complete word (`is_end`). This
encodes "every prefix must also be in the list" directly as a
traversal rule instead of checking all prefixes of each candidate
word separately.

### 5. Storing an aggregate at every node, not just at the end (`05`)
`map_sum_pairs` stores a running sum at *every* node along each
inserted key's path (not just the terminal node), so `sum(prefix)` is
a single O(len(prefix)) walk to the prefix's node and a direct read —
no subtree scan needed at query time. The delta-based update handles
overwriting an existing key's value correctly.

### 6. Trie-guided backtracking over a grid (`06`)
`word_search_ii` combines a trie with the grid-DFS backtracking style
from other topics: walk the grid and the trie *together*, only
stepping to a grid neighbor if that letter exists as a child of the
current trie node. This prunes paths no word could ever complete,
avoiding a separate independent search per word (which would re-walk
shared prefixes of the grid repeatedly).

### 7. Precomputing bounded results at every node (`07`)
`search_suggestions_system` is the "autocomplete" trie: insert
products in sorted order, capping each node's stored suggestion list
at 3 entries so only the lexicographically smallest ones accumulate
there. This precomputes every possible query's answer *during
insertion*, making each query just a walk-and-read, no sorting or
filtering at query time.

### 8. Reversing the string to flip suffix into prefix (`08`)
Trie structure only exposes prefix relationships naturally.
`short_encoding_of_words` needs *suffix* relationships ("is this word
a suffix of another"), so it inserts every word *reversed* — suffix
of the original becomes prefix of the reversed string, which the trie
handles for free. A word only needs its own encoding entry if its
reversed-path node is a leaf (nothing extends past it, so it isn't a
suffix of anything longer already covered).

### 9. Trie over bits instead of characters (`09`)
`maximum_xor_of_two_numbers` is the biggest conceptual jump in the
folder: the trie's alphabet is just `{0, 1}`, one level per bit of a
fixed-width number. This makes tries applicable well beyond strings —
anything with a fixed-length symbol sequence (bits, digits, tokens)
can be trie-indexed the same way. Greedily walking toward the
*opposite* bit at each level (to maximize XOR) is a bit-level version
of pattern 4's "traversal rule enforces a constraint" idea.

### 10. Combined keys to answer a two-part query (`10`)
A plain trie answers one-dimensional questions ("starts with X").
`prefix_and_suffix_search` needs "starts with X *and* ends with Y"
simultaneously — solved by inserting a synthetic combined key
(`suffix + "#" + word`) for every possible suffix length of every
word, turning a query into an ordinary single-path trie lookup of
`suffix + "#" + prefix`. This "encode two constraints into one key"
trick is worth remembering as a general escape hatch whenever a trie
needs to answer more than a single prefix condition at once.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | implement_trie | O(len) per op | O(total chars inserted) |
| 02 | add_and_search_word | O(len) exact, O(26^len) worst case with wildcards | O(total chars) |
| 03 | replace_words | O(total sentence length) | O(total dictionary chars) |
| 04 | longest_word_in_dictionary | O(total chars) | O(total chars) |
| 05 | map_sum_pairs | O(len(key)) per op | O(total chars) |
| 06 | word_search_ii | O(rows·cols·4^L) worst case (L = max word length) | O(total dictionary chars) |
| 07 | search_suggestions_system | O(total chars · log(total) for sort) | O(total chars) |
| 08 | short_encoding_of_words | O(total chars) | O(total chars) |
| 09 | maximum_xor_of_two_numbers | O(n · bit_length) | O(n · bit_length) |
| 10 | prefix_and_suffix_search | O(len(word)^2) per insert (all suffixes), O(len) per query | O(total chars^2) |

`10`'s space cost is the notable outlier — inserting every suffix of
every word is quadratic in word length, the price paid for answering
a two-constraint query in a single lookup. Worth being able to state
that trade-off explicitly if asked.

## Common interview follow-ups to be ready for

- `implement_trie`: "how would you support delete?" — need to walk to
  the word's end node, clear `is_end`, then walk back up removing any
  now-childless nodes that aren't the end of some other word.
- `add_and_search_word`: "what's the worst-case time for a query full
  of dots?" — O(26^len) in the worst case (branching at every level);
  be ready to state this isn't actually O(len) like a plain search.
- `word_search_ii`: "why build one trie for all words instead of
  searching for each word separately?" — shared prefixes across
  words would otherwise be re-walked on the grid once per word;
  the shared trie prunes all of them together in one pass.
- `map_sum_pairs`: "what if sum() needed to support a range of
  prefixes, not just one?" — would need a different structure
  (e.g. a sorted list of keys with binary search), since a trie
  only naturally answers single-prefix queries efficiently.
- `short_encoding_of_words`: "can you do this without a trie?" — yes,
  by checking (for each word) whether it's a suffix of any other word
  in the list directly, but that's O(n^2 · avg_len) versus the trie's
  O(total chars); know both and the complexity gap between them.
- `maximum_xor_of_two_numbers`: "what if numbers could be negative?"
  — the fixed-width two's-complement bit representation still works,
  but the sign bit needs special handling; be ready to discuss it
  even if not implementing it live.
- `prefix_and_suffix_search`: "what's the space cost, and is it worth
  it?" — O(len^2) per word from inserting every suffix; worth
  contrasting with a simpler (but slower per query) approach of two
  separate tries intersected with a set, to show you understand the
  trade-off being made.

## Self-check before moving on

You should be able to, without looking at the code:
- Write the basic `TrieNode`/`insert`/`search` skeleton from memory.
- Explain why `add_and_search_word`'s wildcard search needs DFS
  instead of a single-path walk.
- Explain the "reverse the string" trick in
  `short_encoding_of_words` and why it turns suffix into prefix.
- Explain how a trie generalizes to bits in
  `maximum_xor_of_two_numbers`, and why the greedy "opposite bit"
  choice at each level is safe.
- State the combined-key trick from `prefix_and_suffix_search` and
  what it costs in extra space.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to
`10_recursion_backtracking`.
