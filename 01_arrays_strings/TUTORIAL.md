# Arrays & Strings — Tutorial

Covers the 10 problems solved in this folder. Arrays/strings aren't a
single technique — this topic is really a grab-bag of five reusable
patterns that show up constantly in later topics too.

## The patterns

### 1. Mirror two-pointer (`01`, `09`)
One pointer at index 0, one at index `len-1`, walking inward until
they meet or cross. Used to process a sequence from both ends at
once — reversal, palindrome checks.
```python
left, right = 0, len(s) - 1
while left < right:
    # look at / swap s[left], s[right]
    left += 1
    right -= 1
```
`09_valid_palindrome` extends this with inner skip-loops (ignore
non-alphanumeric chars) and case-insensitive comparison — same
skeleton, extra filtering per step.

### 2. Read/write pointer — in-place partition/compaction (`02`, `03`)
One pointer (`i`/`read`) scans every element; a second pointer
(`insert_pos`/`write`) only advances when the current element needs
to be kept. This is how you filter or dedupe an array without
allocating a new one.
- `move_zeroes`: write pointer advances on non-zero elements, swap.
- `remove_duplicates_sorted_array`: write pointer advances when the
  current element differs from the *last written* element (relies on
  the array being sorted so duplicates are adjacent).

### 3. Single-pass running state (`04`, `07`)
Track one or two running values while scanning once, left to right.
No lookahead, no extra storage proportional to input size.
- `max_subarray` (Kadane's): running sum, reset to the current
  element whenever the running sum goes negative (dead weight).
- `best_time_to_buy_sell_stock`: running minimum price + running
  best profit, checked in that order each step.

This is the simplest form of dynamic programming: "the answer at
position i depends only on the answer at position i-1," computed
without an explicit DP array since only the last state is needed.

### 4. Prefix / suffix precomputation (`06`)
When you need "everything before i" and "everything after i"
combined, and can't do it in one pass, do it in two: build a
prefix result left-to-right, then fold in a suffix result
right-to-left over the same output array.
`product_except_self` is the canonical example — also the standard
answer to "compute X without using operation Y" (here: product
without division).

### 5. Two-pointer merge from the correct end (`05`, `08`)
- `rotate_array`: the "three reversals" trick — reverse the whole
  array, then reverse each of the two resulting segments — turns an
  array rotation into three O(n) passes with zero extra space.
- `merge_sorted_array`: when one array has trailing free space,
  merge **from the back** (largest elements first) instead of the
  front, avoiding the O(n) per-insert shifting a forward merge would
  need.

### 6. Vertical / structural scan (`10`)
`longest_common_prefix` scans by *character position* across all
strings simultaneously, rather than comparing strings pairwise.
Generalizes to any "find the common structure across N sequences"
problem.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | reverse_string | O(n) | O(1) |
| 02 | move_zeroes | O(n) | O(1) |
| 03 | remove_duplicates_sorted_array | O(n) | O(1) |
| 04 | max_subarray | O(n) | O(1) |
| 05 | rotate_array | O(n) | O(1) |
| 06 | product_except_self | O(n) | O(1) (excl. output) |
| 07 | best_time_to_buy_sell_stock | O(n) | O(1) |
| 08 | merge_sorted_array | O(m+n) | O(1) |
| 09 | valid_palindrome | O(n) | O(1) |
| 10 | longest_common_prefix | O(n·m) | O(1) (excl. output) |

Every problem in this set is linear time, constant extra space — that
combination (in-place, single or double pass) is the recurring
interview expectation for "easy" array/string problems. If an
approach needs a new array/dict proportional to input size, that's
usually a sign there's a more in-place way to do it (as in `02`, `03`,
`05`, `08` above), *unless* the problem genuinely needs a hash map —
which is exactly what topic `02_hashing` covers next.

## Common interview follow-ups to be ready for

- "Can you do it in O(1) space?" — already true for all 10 here;
  know *why* for each (which pointer trick makes it possible).
- `max_subarray`: "return the actual subarray, not just the sum" —
  track start/end indices alongside the running sum.
- `rotate_array`: "what if k is negative (rotate left)?" —
  normalize with `k %= n` first, then a negative k still works with
  Python's modulo, but be ready to explain rotating left vs right.
- `merge_sorted_array`: "what if nums1 doesn't have extra space?" —
  becomes a different problem (merge into new array, or in-place
  merge using O(1) space with a harder swap-based algorithm).
- `product_except_self`: "what if the array is streamed / can't fit
  in memory?" — no longer solvable in O(1) space; discuss O(n) as
  the floor once random access is gone.
- `longest_common_prefix`: "what about a trie instead?" — vertical
  scan is O(n·m) worst case; a trie built once amortizes better if
  you'll query prefixes repeatedly (preview of topic `09_tries`).

## Self-check before moving on

You should be able to, without looking at the code:
- Write the mirror two-pointer skeleton from memory.
- Explain why `remove_duplicates_sorted_array`'s approach breaks if
  the array isn't sorted.
- Explain why Kadane's algorithm resets instead of just tracking the
  global max naively.
- Derive the three-reversal rotation trick on paper with a 5-element
  example.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `02_hashing`.
