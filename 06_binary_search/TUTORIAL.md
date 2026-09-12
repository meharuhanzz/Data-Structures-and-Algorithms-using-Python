# Binary Search — Tutorial

Covers the 10 problems solved in this folder. The core idea never
changes across all 10: at every step, eliminate half the remaining
search space using one comparison. What changes is *what* is being
searched over — an array's index, a range of possible answers, or a
partition point — and that's the real skill this topic builds:
recognizing when a problem has binary search's one true requirement
(monotonicity - a clean "too small / too big" split) even when there's
no visible sorted array to search.

## The patterns

### 1. Exact-match search (`01`)
The baseline. `left <= right`, checking `nums[mid] == target`
directly, closing in with `mid ± 1`. Every other pattern in this
folder is a variation on this loop shape.

### 2. Left-boundary search (`02`, `03`)
Instead of "does this exact value exist," the question is "what's
the first index satisfying some condition." The loop shape changes
subtly: `right` starts at `len(nums)` (a valid *position*, not just a
valid *index*), the loop condition is `left < right`, and on a match
you set `right = mid` (not `mid - 1`) because `mid` itself might be
the answer and must stay eligible.
- `search_insert_position`: first index where `nums[i] >= target`.
- `first_and_last_position`: runs this shape *twice* — once biased
  to keep shrinking left after a match (find first), once biased to
  keep shrinking right (find last). Two O(log n) searches, still
  O(log n) total, versus an O(n) scan out from one found index.

### 3. Search on structurally-broken sortedness (`04`, `05`)
The array as a whole isn't sorted, but a rotation only breaks
sortedness at exactly one point — so at every `mid`, at least one of
the two halves is still a clean sorted run. The technique in both
problems is the same: figure out *which* half is sorted by comparing
boundary values, then decide which half to keep based on that.
- `search_rotated_sorted_array`: once the sorted half is known, check
  if target's value range falls inside it.
- `find_minimum_rotated_sorted_array`: the minimum *is* the rotation's
  break point, found by comparing `nums[mid]` to `nums[right]` instead
  of searching for a target value at all.

### 4. Search on slope, not on order (`06`)
`find_peak_element` doesn't require the array to be sorted or
rotated-sorted at all — just a guarantee that a peak provably exists
in whichever half is kept. Comparing `nums[mid]` to its neighbor
gives a local slope; the direction of that slope tells you which
half must contain a peak. This is the most abstract pattern here:
binary search doesn't require *any* global order, only a local
comparison that provably keeps a valid answer in the remaining half.

### 5. Flattened 2D search (`07`)
`search_2d_matrix` is pattern 1, unchanged — the only new idea is
using `divmod(mid, cols)` to treat a row-major-sorted 2D grid as a
single virtual 1D array, avoiding a separate row-then-column search.

### 6. Binary search on the answer space (`08`, `09`)
The biggest conceptual jump in the folder: there is no array being
searched at all. The *candidate answers themselves* form the search
space (e.g. possible eating speeds, possible ship capacities), and
what's being tested at each `mid` is a predicate — "is this candidate
good enough?" — that must be monotonic (true for all values above/
below some threshold, never toggling back and forth). Any time a
problem says "find the minimum/maximum X such that condition holds,"
and increasing X only ever makes the condition easier or only ever
harder (never both), that's this pattern, regardless of whether a
sorted array is anywhere in sight.
- `koko_eating_bananas`: predicate = "can she finish in <= h hours at
  this speed?" — monotonic because faster speed never needs more time.
- `capacity_to_ship_packages`: predicate = "can it ship in <= days
  days at this capacity?" — monotonic the same way.

### 7. Binary search on a partition point (`10`)
`median_of_two_sorted_arrays` is a third distinct shape: binary
search over *where to cut* two arrays simultaneously so that
everything left of both cuts is <= everything right of both cuts.
The partition in the smaller array is searched directly; the
partition in the other array is derived (`j = half - i`), not
searched independently — that's what keeps the whole thing at
O(log(min(m,n))) instead of O(log(m) + log(n)) or worse. Four border
values determine, in O(1), whether the current partition is valid or
needs to shift left/right.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | binary_search | O(log n) | O(1) |
| 02 | search_insert_position | O(log n) | O(1) |
| 03 | first_and_last_position | O(log n) | O(1) |
| 04 | search_rotated_sorted_array | O(log n) | O(1) |
| 05 | find_minimum_rotated_sorted_array | O(log n) | O(1) |
| 06 | find_peak_element | O(log n) | O(1) |
| 07 | search_2d_matrix | O(log(m·n)) | O(1) |
| 08 | koko_eating_bananas | O(n · log(max(piles))) | O(1) |
| 09 | capacity_to_ship_packages | O(n · log(sum(weights))) | O(1) |
| 10 | median_of_two_sorted_arrays | O(log(min(m,n))) | O(1) |

Note `08` and `09` aren't purely O(log(answer_range)) — each binary
search step also runs an O(n) predicate check (`hours_needed`,
`days_needed`), so the total is the product, not just the log term.
Interviewers will expect this distinction stated explicitly.

## Common interview follow-ups to be ready for

- `binary_search`: "what if the array has duplicates?" — exact-match
  search still works, but "which occurrence" becomes ambiguous;
  that's exactly what `03` solves properly.
- `first_and_last_position`: "can you avoid writing the search logic
  twice?" — yes, with a single helper parameterized by a boolean
  (as done here) or by which comparison operator to bias toward.
- `search_rotated_sorted_array`: "what if duplicates are allowed?" —
  `nums[left] <= nums[mid]` can no longer reliably identify the
  sorted half (LC81); worst case degrades to O(n).
- `find_peak_element`: "what if the array could be flat (equal
  neighbors) instead of strictly increasing/decreasing?" — problem
  guarantees strict inequality between neighbors here; discuss what
  breaks in the slope argument without that guarantee.
- `koko_eating_bananas` / `capacity_to_ship_packages`: "how do you
  even recognize this is a binary search problem?" — be ready to
  articulate the tell: a min/max-such-that-condition-holds question
  with a monotonic condition, independent of any sorted array.
- `median_of_two_sorted_arrays`: "why binary search the smaller
  array?" — searching the larger one is still correct but wastes
  time; know why the swap at the top of the function matters for the
  stated O(log(min(m,n))) bound, not just for correctness.

## Self-check before moving on

You should be able to, without looking at the code:
- State the difference in loop shape between exact-match search (`01`)
  and left-boundary search (`02`), and why each is correct for its
  purpose.
- Explain how a rotated array guarantees at least one sorted half at
  every step.
- Recognize a "binary search on the answer" problem from its
  description alone, without seeing the code, and state what the
  monotonic predicate is.
- Explain in one sentence why `median_of_two_sorted_arrays` searches
  a partition point instead of a value.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `07_trees`.
