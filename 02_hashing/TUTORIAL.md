# Hashing — Tutorial

Covers the 10 problems solved in this folder. Every problem here uses
a dict or set to turn an O(n) or O(n^2) lookup into O(1) amortized —
that trade of memory for speed is the entire point of this topic.

## The patterns

### 1. Complement lookup (`01`)
Walking once, and for each element asking "have I already seen the
value that would pair with this one to hit my target?" Store
value -> index as you go; check before you insert so you never match
an element with itself.
```python
seen = {}
for i, n in enumerate(nums):
    if (target - n) in seen:
        return [seen[target - n], i]
    seen[n] = i
```
Turns the brute-force O(n^2) pair check into a single O(n) pass.

### 2. Plain membership (`02`, `08`)
When the question is just "have I seen this before" or "what's
common between two collections," a `set` alone is enough — no need
for a dict with values attached.
- `contains_duplicate`: add-then-check as you scan.
- `intersection_of_two_arrays`: two sets, `&` operator. Sometimes the
  "hashing technique" *is* just knowing the right built-in operator
  exists and is already optimal.

### 3. Frequency counting (`03`, `05`, `10`)
Build a dict of value -> count, then use those counts to answer a
question. Three different questions, same counting step:
- `valid_anagram`: build counts from s, *decrement* while consuming
  t — a clean way to check two multisets are equal without building
  two separate dicts and comparing them.
- `top_k_frequent_elements`: counts feed into a bucket-sort indexed
  by frequency (bucket index = frequency value, since frequency is
  bounded by `len(nums)`), giving O(n) instead of the O(n log n) a
  sort-by-frequency approach would cost.
- `first_unique_character`: counts first, then a *second* pass in
  original order to find the first count-1 entry — needed because
  "first" refers to original string order, not count order.

### 4. Canonical-key grouping (`04`)
When items need to be bucketed by "sameness" under some
transformation, compute a canonical form and use it as a dict key.
`group_anagrams` sorts each string's characters — every anagram of a
word produces the identical sorted string, so that sorted string is
a perfect grouping key. This generalizes: any "group things that are
equivalent under transformation X" problem reduces to "compute X,
use it as a dict key."

### 5. Prefix-sum + hash (`07`)
The hardest pattern here. When you need to count subarrays matching
a sum condition, and the array has negative numbers (so sliding
window's "shrink when too big" logic breaks), track running prefix
sums in a dict of sum -> how many times seen. A subarray from j+1 to
i sums to k exactly when `prefix[i] - prefix[j] == k`, so at each
step you look up `prefix[i] - k` in the dict of prior prefix sums.
Seeding with `{0: 1}` is required to count subarrays that start at
index 0 (their "j" is the empty prefix before the array starts).

### 6. Bijective (two-way) mapping (`09`)
Some problems need *both directions* of a mapping to stay consistent,
not just one. `isomorphic_strings` keeps two dicts (s->t and t->s)
because a single dict would silently allow two different source
characters to map to the same target character, which breaks the
one-to-one requirement. Whenever "mapping" and "no two things collide
into the same target" both appear in a problem statement, that's the
signal to keep both directions.

### 7. Set-based sequence detection (`06`)
`longest_consecutive_sequence` looks like a sorting problem but
sorting costs O(n log n) and the problem asks for O(n). The trick:
put everything in a set, then only *start* counting a run from a
number whose predecessor (`n-1`) is not in the set. That guarantees
every run is walked exactly once, from its true start — total work
across all runs is O(n), not O(n) per element.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | two_sum | O(n) | O(n) |
| 02 | contains_duplicate | O(n) | O(n) |
| 03 | valid_anagram | O(n) | O(1) (bounded alphabet) |
| 04 | group_anagrams | O(n·k log k) | O(n·k) |
| 05 | top_k_frequent_elements | O(n) | O(n) |
| 06 | longest_consecutive_sequence | O(n) | O(n) |
| 07 | subarray_sum_equals_k | O(n) | O(n) |
| 08 | intersection_of_two_arrays | O(n+m) | O(n+m) |
| 09 | isomorphic_strings | O(n) | O(1) (bounded alphabet) |
| 10 | first_unique_character | O(n) | O(1) (bounded alphabet) |

(`k` in `04` is average string length, from the per-string sort.)
Unlike topic 01, this whole topic trades O(n) *extra space* for
dropping time complexity from O(n^2)/O(n log n) down to O(n) — that
trade is the defining feature of hashing problems, versus topic 01's
in-place O(1)-space focus.

## Common interview follow-ups to be ready for

- `two_sum`: "what if there's no valid pair?" — returning `[]` here;
  confirm with the interviewer whether that's acceptable or an
  exception/sentinel is expected instead.
- `two_sum`: "what if the array is sorted?" — then two-pointer from
  both ends beats hashing on space (O(1) instead of O(n)); know when
  hashing is *not* the best tool.
- `group_anagrams`: "what if strings can have unicode / very long
  length?" — sorting-as-key costs O(k log k) per string; a character
  *count tuple* as the key avoids the sort, dropping to O(k) per
  string at the cost of a bulkier key.
- `top_k_frequent_elements`: "what if k is close to n?" — bucket sort
  here is still O(n) regardless of k, unlike a heap-based O(n log k)
  approach; know why bucket sort wins whenever frequency is bounded.
- `subarray_sum_equals_k`: "what if you need the actual subarrays,
  not just the count?" — the dict would need to store lists of
  indices per prefix sum instead of just counts.
- `longest_consecutive_sequence`: "why not just sort?" — be ready to
  state the O(n log n) vs O(n) distinction explicitly; sorting is the
  "obvious" answer interviewers expect you to beat.
- `isomorphic_strings`: "what about three or more strings needing the
  same isomorphism?" — the two-dict trick generalizes to checking
  pairwise consistency across all of them.

## Self-check before moving on

You should be able to, without looking at the code:
- Explain why `two_sum`'s dict check happens *before* inserting the
  current element.
- Derive the prefix-sum equation for `subarray_sum_equals_k` on paper
  (why `prefix[i] - prefix[j] == k`, and why `{0: 1}` is seeded).
- Explain why `longest_consecutive_sequence` doesn't just sort first.
- State from memory when a plain dict is enough vs when you need two
  dicts (bijective mapping) vs when you need a set instead of a dict.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `03_two_pointers_sliding_window`.
