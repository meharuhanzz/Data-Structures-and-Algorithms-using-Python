# Two Pointers & Sliding Window — Tutorial

Covers the 10 problems solved in this folder. Where topic 01 used
two pointers mostly to *mirror* (swap ends inward) and topic 02 used
hashing to trade space for O(1) lookups, this topic is about two
pointers (or a pointer pair defining a window) moving *independently*
based on a running condition — sum, character count, or comparison
result.

## The patterns

### 1. Fixed-size window (`01`, `05`)
Window length is given up front and never changes. Compute the
window's state once, then slide by exactly one step at a time: add
what enters on the right, remove what leaves on the left.
- `max_average_subarray`: state = running sum.
- `permutation_in_string`: state = a character-count dict; slide the
  same way, comparing the whole dict to a target dict each step.

Avoids recomputing from scratch at every position — the difference
between O(n) and O(n·k).

### 2. Variable-size window, grow-then-shrink (`02`, `03`, `04`)
Window length isn't fixed; `right` always advances, `left` advances
conditionally based on whether the current window is still valid.
Two flavors depending on what "valid" means:
- **Shrink while invalid** (`longest_substring_without_repeating`,
  `longest_repeating_character_replacement`): keep growing; the
  moment the window breaks its constraint, shrink from the left
  until it's valid again, then keep growing. Answer = best window
  length seen at any point.
- **Shrink while (still) valid, to find the minimum** (
  `minimum_size_subarray_sum`): grow until the window satisfies the
  condition, then shrink as far as possible *while it still does*,
  recording the shortest length at each shrink step, before growing
  again.

The tell for "this is a variable window problem": the question asks
for the longest/shortest substring or subarray satisfying some
running condition (sum, distinct-character count, replacement
budget) — as opposed to "does one exist" (that's often plain hashing,
topic 02) or "count all of them" (often prefix-sum + hash, also
topic 02).

### 3. Converging two-pointer on sorted data (`06`, `07`)
Only works because the data is sorted: comparing the current pair's
sum/value to a target tells you *unambiguously* which side to move.
- `two_sum_sorted`: sum too small -> move `left` right (only way to
  increase). Sum too big -> move `right` left.
- `three_sum`: fix one element via a loop, then run the exact same
  two-pointer routine on the rest for "sum to -nums[i]". Sorting also
  makes duplicate-skipping nearly free, since equal values become
  adjacent.

This is strictly better than hashing's `two_sum` (topic 02, `01`)
*when the array is already sorted* — O(1) space instead of O(n),
since the greedy pointer movement replaces the need to remember what
was seen.

### 4. Converging two-pointer via greedy elimination (`08`)
`container_with_most_water` isn't sorted, so it's not the same
justification as pattern 3 — instead, the area is capped by the
*shorter* of the two current lines, so moving the taller side's
pointer inward can never help (still capped by the same shorter
side, less width). Moving the shorter side is the only move that
could possibly improve things. That greedy argument — one specific
move is provably never better — is what justifies collapsing an
O(n^2) all-pairs check into O(n).

### 5. Three-pointer partition (`09`)
`sort_colors` generalizes the read/write pointer from topic 01 to
three regions instead of two: `low`/`mid` boundary for one value,
`mid`/`high` boundary for another, with `mid` itself doing the
classifying. The asymmetry — advancing `mid` after a 0-swap but not
after a 2-swap — comes from *what's known* about the swapped-in
value at each boundary (see the comment in `09_sort_colors.py` for
the full argument). This pattern generalizes to "partition into k
labeled groups in one pass."

### 6. Fast-slow pointers / cycle detection preview (`10`)
`find_the_duplicate_number` treats an array as an implicit linked
list (`i -> nums[i]`) and applies Floyd's cycle detection: a fast
pointer moving 2 steps and a slow pointer moving 1 step will meet
inside a cycle if one exists; resetting one pointer to the start and
advancing both by 1 step finds the cycle's entrance. This is included
here specifically as a preview — the exact same two-phase algorithm
returns in `04_linked_list` for real cycle-detection problems, just
with `.next` instead of `nums[i]`.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | max_average_subarray | O(n) | O(1) |
| 02 | longest_substring_without_repeating | O(n) | O(min(n, alphabet)) |
| 03 | minimum_size_subarray_sum | O(n) | O(1) |
| 04 | longest_repeating_character_replacement | O(n) | O(alphabet) |
| 05 | permutation_in_string | O(n) | O(alphabet) |
| 06 | two_sum_sorted | O(n) | O(1) |
| 07 | three_sum | O(n^2) | O(1) (excl. sort/output) |
| 08 | container_with_most_water | O(n) | O(1) |
| 09 | sort_colors | O(n) | O(1) |
| 10 | find_the_duplicate_number | O(n) | O(1) |

Note `03` and `04`'s inner `while`/shrink loop looks like it could be
O(n^2) nested, but `left` only ever moves forward and never resets —
across the whole run it advances at most n times total, so the true
cost is O(n) amortized, not O(n) per outer step. Worth being able to
explain this amortized-analysis argument out loud in an interview.

## Common interview follow-ups to be ready for

- `longest_substring_without_repeating`: "what if the alphabet is
  huge (unicode)?" — dict-based `last_seen` already handles this;
  a fixed-size array trick (common for ASCII-only variants) would not.
- `minimum_size_subarray_sum`: "what if nums can contain negative
  numbers?" — the shrink logic breaks (sum isn't monotonic as the
  window grows), which is exactly why `07_subarray_sum_equals_k` in
  topic 02 needed prefix-sum + hash instead of a sliding window.
- `three_sum`: "what about 4Sum / kSum?" — generalizes by fixing k-2
  elements with nested loops and running the same two-pointer on the
  remainder; same duplicate-skipping logic applies at each fixed level.
- `container_with_most_water`: be ready to justify out loud *why*
  moving the taller pointer can never be optimal — interviewers often
  push specifically on this proof step, not just the code.
- `sort_colors`: "what if there were k colors instead of 3?" — the
  three-pointer trick doesn't generalize cleanly past 3; a counting
  sort (frequency count + overwrite) becomes the right answer instead.
- `find_the_duplicate_number`: "what if you could modify the array or
  use O(n) space?" — then it degenerates to `02_hashing/02_
  contains_duplicate`'s set-based approach; know why the *O(1)-space,
  can't-modify* constraints specifically force Floyd's algorithm here.

## Self-check before moving on

You should be able to, without looking at the code:
- State the difference between "shrink while invalid" and "shrink
  while valid" sliding windows, and give one example of each.
- Explain the amortized O(n) argument for why `left` never causing
  nested-loop blowup in `03`/`04`.
- Justify on paper why `container_with_most_water`'s greedy pointer
  move is safe.
- Walk through Floyd's cycle detection on a small example by hand
  (both phases) for `find_the_duplicate_number`.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `04_linked_list`.
