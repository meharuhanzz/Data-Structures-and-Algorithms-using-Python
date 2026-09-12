# Stacks & Queues — Tutorial

Covers the 10 problems solved in this folder. Stacks and queues are
the two simplest possible restrictions on where you can add/remove
elements (LIFO vs FIFO) — most of this topic is about recognizing
*which* restriction a problem secretly needs, since neither structure
is built into Python as a distinct type (a `list` serves as a stack;
`collections.deque` serves as a queue or a double-ended structure).

## The patterns

### 1. Plain LIFO matching (`01`)
The most direct use of a stack: nested structure where the most
recently opened thing must be the next one closed. Push on open,
pop-and-compare on close, and a non-empty stack at the end means
something was left unclosed. This exact "push open, resolve on
close" shape reappears in `10_decode_string` for a harder version of
the same idea.

### 2. Auxiliary stack for O(1) extra queries (`02`)
When a stack needs to answer a question that isn't naturally O(1)
(like "what's the minimum right now?"), keep a second stack in
lockstep that caches the answer to that question *as of each push*.
`min_stack` computes `min(new_val, previous_min)` on every push and
pops in lockstep with the main stack, so `get_min()` never has to
re-scan.

### 3. Postfix expression evaluation (`03`)
Postfix (RPN) notation is designed around a stack: by the time an
operator token is read, both its operands are already sitting on top
of the stack in the right order, so evaluation is just repeated
pop-pop-compute-push. No precedence or parenthesis handling needed —
that's the entire reason RPN exists as a notation.

### 4. Monotonic stack (`04`, `05`, `06`)
The single most important pattern in this folder. Keep a stack whose
values are always increasing or always decreasing (top to bottom).
When a new value would break that ordering, pop everything that it
resolves — each popped element has just found its "next greater" (or
next smaller, or right boundary) relative to the current position.
Every element is pushed once and popped at most once, so despite the
inner `while` loop this is O(n) total, not O(n^2) — same amortized
argument as topic 03's shrinking sliding window.
- `daily_temperatures`: decreasing stack of indices; a warmer day
  resolves every colder day still stacked, recording the day-gap.
- `next_greater_element`: identical mechanism, but the pass builds a
  reusable `value -> next_greater` dict over all of nums2 once,
  since only a subset of values (nums1) actually needs answering.
- `largest_rectangle_in_histogram`: increasing stack of indices. A
  shorter bar resolves every taller bar still stacked — each
  resolved bar's rectangle spans from the (now-exposed) new stack
  top to the current position. This is the hardest problem in the
  folder; the monotonic-stack idea is identical to the other two,
  just computing an area instead of a gap or a value.

### 5. Simulating one structure with the other (`07`, `08`)
Mirror-image design problems: build a FIFO queue out of LIFO stacks,
or a LIFO stack out of a FIFO queue.
- `implement_queue_using_stacks`: two stacks, `in_stack` for pushes
  and `out_stack` for pops. Only reverse `in_stack` into `out_stack`
  when `out_stack` is empty ("lazy transfer") — each element crosses
  from one stack to the other at most once in its lifetime, keeping
  amortized cost O(1) despite an occasional O(n) reversal.
- `implement_stack_using_queues`: a single deque, rotated by
  `size - 1` after every push so the newest element ends up at the
  front — trading push's cost (O(n) rotation) for making pop/top
  trivial (O(1) front access), the opposite trade-off from the
  stacks-based queue above.

### 6. Monotonic deque for a sliding window (`09`)
`sliding_window_maximum` combines the monotonic-stack idea from
pattern 4 with topic 03's sliding window: it needs removal from
*both* ends — the back (discard values that can never be the max
again, same rule as pattern 4) and the front (discard indices that
fell outside the window). That two-ended removal requirement is
exactly why a `deque` is needed here instead of a plain stack.

### 7. Stack-based nested parsing (`10`)
`decode_string` generalizes pattern 1: instead of just matching
open/close, each stack frame carries *state* (the partial string
built so far, plus the repeat count) that gets paused on `[` and
resumed/combined on `]`. This push-state-before-descending,
pop-and-combine-on-return shape is the general template for parsing
any nested grammar (JSON, arithmetic expressions with parens, HTML/
XML) with a stack instead of recursion.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | valid_parentheses | O(n) | O(n) |
| 02 | min_stack | O(1) per op | O(n) |
| 03 | evaluate_reverse_polish_notation | O(n) | O(n) |
| 04 | daily_temperatures | O(n) | O(n) |
| 05 | next_greater_element | O(n+m) | O(n) |
| 06 | largest_rectangle_in_histogram | O(n) | O(n) |
| 07 | implement_queue_using_stacks | O(1) amortized per op | O(n) |
| 08 | implement_stack_using_queues | O(n) push, O(1) pop/top | O(n) |
| 09 | sliding_window_maximum | O(n) | O(k) |
| 10 | decode_string | O(n · max repeat depth) | O(n) |

Every monotonic-stack problem here (`04`, `05`, `06`, `09`) looks
like it should be O(n^2) from the nested loop, but isn't — always be
ready to give the amortized argument (each element pushed once,
popped at most once) rather than just asserting "it's O(n)."

## Common interview follow-ups to be ready for

- `valid_parentheses`: "what about other paired delimiters, like
  custom tags?" — the `pairs` dict generalizes to any closing->opening
  mapping without changing the algorithm shape.
- `min_stack`: "can you do it with O(1) *extra* space instead of a
  second full stack?" — yes, by storing the *difference* from the
  running min instead of the min itself, but it's a harder trick;
  know the auxiliary-stack version cold first.
- `next_greater_element`: "what if nums2 could have duplicates?" —
  problem guarantees distinct values here; discuss what breaks (the
  dict key collision) if that guarantee were dropped.
- `largest_rectangle_in_histogram`: "how does this extend to
  'maximal rectangle in a binary matrix'?" (LC85) — run this exact
  algorithm once per row, treating each row as a histogram built from
  consecutive 1s above it.
- `implement_queue_using_stacks`: "is push or pop the expensive
  operation?" — neither, in the amortized sense; be ready to explain
  why a single push can still trigger an O(n) transfer without
  breaking the O(1) amortized claim.
- `sliding_window_maximum`: "what about sliding window *minimum*?"
  — flip the monotonic direction of the deque; same mechanism.
- `decode_string`: "what if the encoding also supported letters
  mixed with the repeat count directly, like real-world compressed
  formats?" — the state-pushing template still applies, just with a
  richer per-frame state.

## Self-check before moving on

You should be able to, without looking at the code:
- Explain the amortized O(n) argument for any of the monotonic-stack
  problems (why the inner while loop doesn't make it O(n^2)).
- Write the "lazy transfer" queue-from-two-stacks from memory and
  explain why it's O(1) amortized, not O(n) per operation.
- Explain why `sliding_window_maximum` needs a deque (both-end
  removal) instead of a plain stack.
- Trace `decode_string` by hand on `"3[a2[c]]"`, writing out the
  stack's contents after each `[` and `]`.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `06_binary_search`.
