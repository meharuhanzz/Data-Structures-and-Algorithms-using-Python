# Heaps & Priority Queues — Tutorial

Covers the 10 problems solved in this folder. A heap answers exactly
one question efficiently, repeatedly: "what's the smallest (or
largest) item in this collection right now?" — in O(log n) per
insert/remove instead of the O(n) a plain list scan would need, and
without the overhead of keeping the whole collection fully sorted.
Python's `heapq` only implements a *min*-heap, so most of this
folder's problems begin with the same trick: negate values on the
way in and out to simulate a max-heap.

## The patterns

### 1. Direct simulation (`01`)
`last_stone_weight` is the most literal use of a heap: the problem
statement itself says "repeatedly take the two largest," so a
max-heap (via negation) *is* the algorithm, not just an optimization
of one. Worth doing first specifically because the heap maps onto
the problem with zero translation needed.

### 2. Size-k heap for top-k extraction (`02`, `03`, `04`)
The single most common heap pattern in interviews. Maintain a heap of
exactly size k holding the "best k so far"; its root is the *worst*
of those k, making it the one to evict the instant something better
appears. This turns an O(n log n) full sort into O(n log k) — a real
win whenever k is much smaller than n.
- `kth_largest_element_in_array`: min-heap of size k; root is
  directly the kth largest (the smallest among the top k).
- `kth_largest_element_in_a_stream`: identical invariant, but the
  heap persists across calls instead of being rebuilt each time —
  the "streaming" version of the same idea.
- `k_closest_points_to_origin`: same invariant, but a *max*-heap
  (negated) of size k, and the comparison key is a derived value
  (squared distance) rather than the raw element.

### 3. Heap over a derived ordering (`05`, `06`)
Sometimes what's tracked in the heap isn't "the elements" directly,
but a fact *about* them that changes as the algorithm runs.
- `meeting_rooms_ii`: the heap holds end times of rooms currently in
  use. A new meeting either reuses the room whose end time has
  already passed (root of the heap), or needs a brand new room —
  the heap's final size is the peak concurrent room count.
- `task_scheduler`: the heap holds remaining counts per task type,
  always running the most-frequent-remaining task next (greedy). A
  side FIFO queue holds tasks temporarily "on cooldown" and returns
  them to the heap once their wait time has elapsed — this is the
  first problem in the folder combining a heap with a second data
  structure to enforce a constraint the heap alone can't express.

### 4. K-way merge (`07`)
`merge_k_sorted_lists` generalizes `04_linked_list/02_merge_two_
sorted_lists` from 2 lists to k. Comparing all k current heads by
hand at every step would cost O(k) per node; keeping them in a heap
instead drops that to O(log k) per node, since the heap always
surfaces the smallest of the k candidates directly. The `(val, index,
node)` tuple trick — including a tiebreaker index — matters here
specifically because `ListNode` objects aren't comparable, and ties
on `val` would otherwise crash the comparison.

### 5. Heap-driven generation, not extraction (`08`)
`ugly_number_ii` uses a heap to *generate* a sequence in sorted order
rather than to extract top/bottom elements from an existing
collection. Each popped value spawns new candidates (`×2`, `×3`,
`×5`); a `seen` set prevents the same candidate being queued twice
from different paths (e.g. reaching 6 via both `2×3` and `3×2`).

### 6. Greedy placement with a one-step delay (`09`)
`reorganize_string` greedily places the most frequent remaining
character, using the same max-heap-by-count shape as `06`. The new
idea is the one-step delay: a just-placed character can't be pushed
back into contention immediately, or it could get placed twice in a
row. Holding it in a single `prev` variable and pushing it back only
after the *next* character is chosen is a minimal way to enforce a
"not immediately again" constraint without extra bookkeeping.

### 7. Two heaps for an always-current statistic (`10`)
`find_median_from_data_stream` is the hardest problem here: split the
stream into a max-heap of the lower half and a min-heap of the upper
half, size-balanced to within one element. The median then sits at
the boundary between the two heaps — an O(1) read at any point in the
stream, no sorting or scanning needed, with each insert costing
O(log n) to maintain the split.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | last_stone_weight | O(n log n) | O(n) |
| 02 | kth_largest_element_in_array | O(n log k) | O(k) |
| 03 | kth_largest_element_in_a_stream | O(log k) per add | O(k) |
| 04 | k_closest_points_to_origin | O(n log k) | O(k) |
| 05 | meeting_rooms_ii | O(n log n) | O(n) |
| 06 | task_scheduler | O(n log 26) ≈ O(n) | O(1) (26 task types) |
| 07 | merge_k_sorted_lists | O(n log k) | O(k) |
| 08 | ugly_number_ii | O(n log n) | O(n) |
| 09 | reorganize_string | O(n log 26) ≈ O(n) | O(n) |
| 10 | find_median_from_data_stream | O(log n) per add, O(1) per query | O(n) |

## Common interview follow-ups to be ready for

- `kth_largest_element_in_array`: "can you do better than O(n log k)?"
  — yes, Quickselect averages O(n), though worst-case O(n^2); know
  the heap version cold first, then mention Quickselect as the
  follow-up optimization.
- `k_closest_points_to_origin`: "why squared distance instead of
  actual distance?" — sqrt is monotonic, so it never changes relative
  ordering; skipping it avoids float precision and cost for free.
- `meeting_rooms_ii`: "what if you also needed to know *which* room
  each meeting used?" — store room identifiers alongside end times in
  the heap instead of bare integers.
- `task_scheduler`: "is there a closed-form formula instead of
  simulation?" — yes (based on the max count and how many tasks tie
  for it), but the simulation shown here is easier to derive live and
  to explain the reasoning behind, which interviewers often prefer.
- `merge_k_sorted_lists`: "what if k is very large, larger than the
  total number of nodes?" — the heap never holds more than k elements
  at once regardless of total node count, so this doesn't change the
  complexity; be ready to state that explicitly.
- `find_median_from_data_stream`: "what if numbers can also be
  *removed* from the stream?" — plain heaps don't support efficient
  arbitrary removal; this needs lazy deletion (mark-and-skip) or a
  balanced BST/order-statistics structure instead — good to mention
  as the natural harder follow-up.

## Self-check before moving on

You should be able to, without looking at the code:
- Explain the negate-for-max-heap trick and why Python's heapq only
  offers a min-heap.
- State the size-k heap invariant from memory and explain why the
  root is always the "worst of the best k."
- Explain why `merge_k_sorted_lists` needs a tiebreaker in its heap
  tuples.
- Walk through the two-heap balancing steps in
  `find_median_from_data_stream` on a small example (5-6 numbers) by
  hand, tracking both heaps after each insert.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `09_tries`.
