# Linked List — Tutorial

Covers the 10 problems solved in this folder, plus the shared
`list_node.py` (a `ListNode` class and `to_linked_list`/
`to_python_list` conversion helpers used by every test harness here).

Linked lists have no random access (`nums[i]` doesn't exist - you can
only follow `.next`), so every technique in this folder exists to
work around that one constraint using a small number of pointers
moving through the list at different speeds or in different phases.

## The patterns

### 1. In-place reversal (`01`)
Walk once, flip each node's `.next` to point backward. The one
non-obvious detail: save `next_node = curr.next` *before* overwriting
`curr.next = prev`, otherwise the rest of the list is lost the moment
you rewrite the pointer. This exact three-line reversal core
reappears inside `07` and `08`.

### 2. Dummy head for merge/splice (`02`, `06`)
Whenever a problem might need to change *which node is first*
(merging, deleting the head), give yourself a throwaway `dummy` node
pointing at the real head, operate relative to `dummy`, and return
`dummy.next` at the end. This removes the need for an `if this is the
first node` special case anywhere in the main logic.

### 3. Fast-slow pointers (`03`, `04`, `05`)
The core linked-list technique, first previewed in
`03_two_pointers_sliding_window/10_find_the_duplicate_number` on a
plain array. `fast` moves 2 steps per iteration, `slow` moves 1:
- **Cycle detection** (`03`): if a cycle exists, `fast` eventually
  laps `slow` inside it and they land on the same node. If acyclic,
  `fast` simply reaches `None` first.
- **Finding the cycle's start** (`04`): two-phase version of the
  same idea - phase 1 finds *a* meeting point, phase 2 (reset one
  pointer to `head`, advance both by 1 step) finds the meeting point
  is always exactly the cycle's entrance. Worth being able to state
  the informal proof (see the file's docstring), not just the code.
- **Finding the middle** (`05`): no meeting point needed here - by
  the time `fast` runs off the end, `slow` has covered exactly half
  the distance, landing on the middle directly.

### 4. Two pointers with a fixed gap (`06`)
`remove_nth_node_from_end` advances one pointer `n` steps first to
create a gap, then moves both together until the leading pointer
falls off the end. The trailing pointer ends up exactly `n` nodes
from the end without ever computing the list's length - a one-pass
alternative to the two-pass "count length, then walk to position"
approach.

### 5. Composite problems — combining earlier patterns (`07`, `08`)
Once reversal and middle-finding both exist as primitives, harder
problems become "apply pattern A, then pattern B, then a simple
walk":
- `palindrome_linked_list`: find middle (05) -> reverse second half
  (01) -> walk both halves comparing values.
- `reorder_list`: find middle (05) -> reverse second half (01) ->
  merge by strict alternation (structurally like 02's merge, but
  alternating instead of comparison-driven, since the two halves
  aren't sorted relative to each other).

This is the main payoff of solving problems in a deliberate order:
by the time you reach a "hard"-rated problem, it's often just 2-3
"easy" problems chained together.

### 6. Two-pointer list-switching for alignment (`09`)
`intersection_of_two_linked_lists` uses a pointer-switching trick
instead of computing list lengths up front: each pointer walks its
own list, then switches to the *other* list's head the instant it
hits the end. Both pointers then cover exactly `len(A) + len(B)`
total nodes by the time they'd meet, which automatically cancels out
any length difference between the two lists - no separate "compute
the offset" step needed.

### 7. Doubly linked list + hashmap for O(1) design (`10`)
`lru_cache` is the one problem here needing a doubly (not singly)
linked list. The dict gives O(1) key -> node lookup; the doubly
linked list keeps nodes ordered by recency and supports O(1) removal
of an arbitrary node (not just the head/tail), because removal only
needs to patch two neighbor pointers - no need to walk from the head
to find a predecessor, which is exactly the operation a singly
linked list can't do in O(1). Sentinel `head`/`tail` nodes (not real
entries) avoid null-checking to know when a queue of one is
"empty".

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | reverse_linked_list | O(n) | O(1) |
| 02 | merge_two_sorted_lists | O(n+m) | O(1) |
| 03 | linked_list_cycle | O(n) | O(1) |
| 04 | linked_list_cycle_ii | O(n) | O(1) |
| 05 | middle_of_linked_list | O(n) | O(1) |
| 06 | remove_nth_node_from_end | O(n) | O(1) |
| 07 | palindrome_linked_list | O(n) | O(1) |
| 08 | reorder_list | O(n) | O(1) |
| 09 | intersection_of_two_linked_lists | O(n+m) | O(1) |
| 10 | lru_cache | O(1) per op | O(capacity) |

Every problem here is O(1) extra space except the LRU cache, whose
O(capacity) space *is* the point (it's a cache) - not a missed
optimization.

## Common interview follow-ups to be ready for

- `reverse_linked_list`: "can you do it recursively?" — yes, but
  recursive reversal uses O(n) call-stack space, so the iterative
  version here is the space-optimal answer; know both.
- `linked_list_cycle_ii`: "prove why the second phase's meeting point
  is the cycle entrance" — interviewers frequently push on the math
  here specifically, not just whether the code works.
- `palindrome_linked_list` / `reorder_list`: "what if you can't
  mutate the input?" — both currently mutate the second half via
  reversal; the workaround is copying values into an array first
  (trades the O(1) space guarantee for O(n)).
- `remove_nth_node_from_end`: "what if n is invalid (larger than the
  list length)?" — current code doesn't guard this; be ready to
  discuss what should happen (raise, no-op, or the problem guarantees
  valid n, as LeetCode does here).
- `intersection_of_two_linked_lists`: "what if the lists don't
  intersect?" — both pointers hit `None` at the same step and the
  loop condition `a is not b` becomes `None is not None` -> False,
  so it correctly returns `None` without a special case.
- `lru_cache`: "how would you make this thread-safe?" — a lock around
  `get`/`put` is the standard answer; also be ready for "what would
  an LFU (least *frequently* used) cache need instead?" (a second
  layer of buckets keyed by frequency).

## Self-check before moving on

You should be able to, without looking at the code:
- Write the 3-line reversal core from memory.
- Explain why a dummy head removes the need for a "first node"
  special case.
- Walk through both phases of Floyd's cycle-start algorithm on a
  small hand-drawn example.
- Explain why `lru_cache` needs a *doubly* (not singly) linked list.
- Derive `reorder_list` on paper by naming the three sub-steps it's
  built from.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `05_stacks_queues`.
