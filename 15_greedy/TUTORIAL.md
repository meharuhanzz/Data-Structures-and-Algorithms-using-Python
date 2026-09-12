# Greedy — Tutorial

Covers the 10 problems solved in this folder. A greedy algorithm
makes the locally-best choice at every step and never looks back or
reconsiders — which only produces a correct *global* answer when the
problem has a specific structural property (an "exchange argument":
any optimal solution can be transformed into the greedy choice
without making things worse). The hard part of a greedy problem is
rarely writing the loop — it's proving to yourself *why* the local
choice is safe, which is what most of the docstrings in this folder
focus on.

## The patterns

### 1. Prefer the more flexible resource (`01`)
`lemonade_change`'s only real decision point is making change for a
$20: spend a $10 (if available) before spending three $5s, because a
$5 bill can make change for *either* a future $10 or $20, while a
$10 bill only ever helps with a future $20. Keeping the more
versatile resource in reserve is never worse — a small but general
greedy instinct.

### 2. Decompose a global optimum into local gains (`02`)
`best_time_to_buy_and_sell_stock_ii` capturing every single positive
day-to-day price increase is provably equivalent to the true optimum,
because any longer profitable buy-low-sell-high stretch is exactly
the sum of its individual daily gains — there's nothing to be gained
by trying to detect longer runs explicitly.

### 3. Track one running "farthest reach" value (`03`, `04`)
Both jump-game problems avoid trying every possible jump length from
every position by tracking only the single most useful fact: how far
could be reached, at best, from everything considered so far.
`can_jump` (03) just checks that value never falls behind the current
position. `jump` (04) turns the same tracked value into an implicit
BFS: `curr_end` marks the current "level's" boundary, and hitting it
forces a jump-count increment before the level (window) advances —
the same "process a whole distance-level before moving to the next"
shape as a real level-order BFS, expressed without an actual queue.

### 4. Reset the search boundary instead of retrying every candidate (`05`)
`gas_station`'s key insight is that once the running tank goes
negative between `start` and some index `i`, *no* station in that
whole stretch could have worked as a starting point — so the next
candidate start can jump straight past all of them to `i + 1`,
instead of retrying each one individually. This is what keeps the
whole algorithm O(n) instead of O(n^2).

### 5. Sort by end time for interval scheduling (`06`, `07`)
Both interval problems use the same greedy backbone: sort by end
coordinate, then greedily keep/act on whichever interval ends
soonest, since that leaves the most room for everything that comes
after. `non_overlapping_intervals` counts what has to be *rejected*
when a new interval starts before the last kept one ends;
`minimum_arrows_to_burst_balloons` is the same idea from the opposite
angle — placing a "covering" arrow at the earliest interval's end,
since anything that extends that far is covered for free, and only
starting a new arrow once something falls outside the current one's
reach.

### 6. Extend a boundary to cover everything currently active (`08`)
`partition_labels` scans once, extending the current partition's
`end` to the last occurrence of every character seen so far — closing
the partition only once the scan position catches up to that boundary,
guaranteeing every character inside has no future occurrence left
unaccounted for. Structurally the same "extend to cover what's
currently reachable/active" idea as the multi-source traversals in
`11_graphs`, just applied in one dimension over a string instead of a
grid.

### 7. Two passes to satisfy a bidirectional constraint (`09`)
`candy`'s constraint compares each child to *both* neighbors, but a
single greedy pass can only correctly enforce a comparison in one
direction. The fix — a left-to-right pass, then a right-to-left pass
using `max` (not overwrite) to avoid undoing what the first pass
already guaranteed — is the general template whenever a greedy
constraint needs to look both ways: split it into two one-directional
passes and combine with whichever operation preserves both.

### 8. Find a processing order where one constraint can't undo another (`10`)
`queue_reconstruction_by_height` has two coordinates pulling in
different directions. The trick is finding the *order* to process
people in where satisfying one person's constraint never retroactively
breaks an already-placed person's constraint: tallest-first (with
ties broken by ascending k) means every already-placed person is at
least as tall, so inserting a new (necessarily shorter-or-equal)
person anywhere never changes any earlier person's count of
taller-or-equal people in front of them. This is the most abstract
lesson in the folder — sometimes the greedy insight isn't a formula,
it's *which order to process things in* so the choices stop
interfering with each other.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | lemonade_change | O(n) | O(1) |
| 02 | best_time_to_buy_and_sell_stock_ii | O(n) | O(1) |
| 03 | jump_game | O(n) | O(1) |
| 04 | jump_game_ii | O(n) | O(1) |
| 05 | gas_station | O(n) | O(1) |
| 06 | non_overlapping_intervals | O(n log n) | O(1) (excl. sort) |
| 07 | minimum_arrows_to_burst_balloons | O(n log n) | O(1) (excl. sort) |
| 08 | partition_labels | O(n) | O(1) (bounded alphabet) |
| 09 | candy | O(n) | O(n) |
| 10 | queue_reconstruction_by_height | O(n^2) (list insert is O(n)) | O(n) |

`10`'s O(n^2) comes specifically from `list.insert` shifting elements
— a linked-list-backed structure could bring it down to
O(n log n) overall (still O(n) sort dominates), worth mentioning as
an optimization if asked.

## Common interview follow-ups to be ready for

- `jump_game` / `jump_game_ii`: "can you return the actual jump
  sequence, not just whether it's possible / how many jumps?" — track
  which index each `curr_end` update came from, then reconstruct the
  path backward.
- `gas_station`: "how do you know the answer is unique if the total
  is non-negative?" — be ready to sketch the exchange-argument proof
  informally, not just assert it.
- `non_overlapping_intervals`: "why sort by end time instead of start
  time?" — sorting by start time doesn't work; be ready with a small
  counterexample showing why (a long interval starting first can
  block several short ones that would otherwise all fit).
- `minimum_arrows_to_burst_balloons`: "how is this different from
  `non_overlapping_intervals`?" — same sort, opposite framing: one
  counts rejections to *eliminate* overlap, the other counts
  selections to *cover* every interval; useful to state the
  relationship explicitly.
- `candy`: "can you do it in one pass instead of two?" — a trickier
  single-pass version exists (tracking ascending/descending run
  lengths), but the two-pass version here is the one to have solid
  first — mention the harder variant only if asked.
- `queue_reconstruction_by_height`: "why does tallest-first work but
  shortest-first doesn't?" — be ready to explain concretely why
  processing shorter people first breaks already-placed people's
  counts (a shorter person inserted before a taller one changes how
  many taller-or-equal people are in front of someone already placed).

## Self-check before moving on

You should be able to, without looking at the code:
- State the exchange-argument shape in one sentence: "any optimal
  solution can be transformed into the greedy choice without making
  it worse."
- Explain why jump_game_ii's "level" boundary (`curr_end`) update
  mirrors a BFS level, without prompting.
- Explain gas_station's "skip the whole failed stretch" argument on
  a small hand-drawn example.
- State why interval-scheduling greedy problems sort by *end* time,
  with a concrete counterexample for why start-time sorting fails.
- Explain why `candy` needs two passes and why the second pass uses
  `max` instead of overwriting.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `16_intervals`.
