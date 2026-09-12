# Dynamic Programming (1D) — Tutorial

Covers the 10 problems solved in this folder. Every DP problem
answers the same underlying question: "if I already knew the answer
to every smaller version of this problem, how would I combine those
answers to get the answer for the current size?" 1D DP means that
state is indexed by a single number (a position, a length, an
amount) rather than a pair — the topic after this one,
`14_dynamic_programming_2d`, is exactly this same idea with two
indices instead of one.

## The patterns

### 1. Rolling-pair state — only the last two answers matter (`01`, `02`, `04`, `09`)
The single most common 1D DP shape here. `dp[i]` depends on only
`dp[i-1]` and `dp[i-2]`, so there's no need for a full array — two
rolling variables (`prev2`, `prev1`), updated each step, are enough
and drop space from O(n) to O(1). What changes between these four
problems is only *how* the two prior states combine:
- `climbing_stairs`: `prev1 + prev2` (Fibonacci — sum the ways).
- `house_robber`: `max(prev1, prev2 + n)` (choice under a
  can't-use-adjacent constraint).
- `min_cost_climbing_stairs`: `min(prev1 + cost, prev2 + cost)`
  (cheapest of two predecessor paths).
- `decode_ways`: a gated version of `climbing_stairs` — each of the
  two "step sizes" (one digit / two digits) only contributes if it
  passes a validity check first.

Recognizing "this problem's rolling-pair combination function is
`+`, `max`, `min`, or gated-`+`" is often the fastest way to solve a
new problem in this shape live.

### 2. Reducing a structural wrinkle to two calls of the simpler version (`03`)
`house_robber_ii`'s only difference from `02` is that the first and
last houses are also adjacent (circular, not linear). Rather than
deriving new circular-aware DP logic, the wraparound constraint is
sidestepped entirely: any valid plan excludes house 0 or excludes the
last house (never robs both), so the answer is just the better of two
ordinary linear subproblems, each solved with `02`'s unchanged
function. Worth remembering as a general move: a small structural
complication in a problem statement doesn't always need a structural
complication in the DP — sometimes it just needs the easier version
called twice.

### 3. Full DP array — more than a constant number of predecessors matter (`05`, `06`, `07`, `08`)
When `dp[i]` could depend on any of several earlier states (not just
the fixed previous one or two), a rolling pair isn't enough — the
full `dp` array is needed so any earlier value can be looked up.
- `coin_change`: `dp[a]` depends on `dp[a-c]` for *every* coin `c` —
  however many denominations there are, that many possible
  predecessors.
- `longest_increasing_subsequence`: `dp[i]` depends on `dp[j]` for
  every `j < i` with `nums[j] < nums[i]` — a data-dependent, variable
  number of predecessors.
- `word_break`: `dp[i]` depends on `dp[j]` for every valid split
  point `j` — same "try every earlier position" shape.

### 4. Same array, opposite loop order, different question (`05` vs `06`)
`coin_change` (minimum coins) and `coin_change_ii` (number of
combinations) operate on the exact same kind of `dp[amount]` array,
but `coin_change_ii` requires coins as the *outer* loop and amount as
the *inner* loop — the opposite of what feels natural coming from
`05`. That ordering is what prevents counting `{1,2}` as two separate
results ("1 then 2" and "2 then 1"): processing one coin denomination
completely before moving to the next means a combination is only ever
built in one fixed order. Swapping the loop order back counts
*permutations* instead — a genuinely different question that happens
to use nearly identical code. This is the single most instructive
"same-looking code, different loop order, different answer" example
in the folder.

### 5. Reachability DP instead of enumeration (`08`)
`word_break` asks "can this be done" (yes/no), which is what turns
what would otherwise be exponential backtracking (as in
`10_recursion_backtracking/08_palindrome_partitioning`, which
enumerates *every* valid partition) into polynomial DP — each `dp[i]`
is computed once and reused by every later position that needs it,
instead of being re-explored from scratch down every branch of a
search tree.

### 6. Tracking two running extremes instead of one (`10`)
`maximum_product_subarray` looks like Kadane's algorithm
(`01_arrays_strings/04_max_subarray`) with multiplication swapped in
for addition, but that substitution alone is broken: a very negative
running product can become the *maximum* the instant another negative
number multiplies it. The fix is tracking both a running max *and* a
running min at every position, since either one could flip into the
new best value depending on the sign of the next element. Whenever a
running Kadane's-style accumulator involves multiplication (or any
operation where sign flips can invert the ranking), that's the signal
to track a min alongside the max, not just the max alone.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | climbing_stairs | O(n) | O(1) |
| 02 | house_robber | O(n) | O(1) |
| 03 | house_robber_ii | O(n) | O(1) |
| 04 | min_cost_climbing_stairs | O(n) | O(1) |
| 05 | coin_change | O(amount · num_coins) | O(amount) |
| 06 | coin_change_ii | O(amount · num_coins) | O(amount) |
| 07 | longest_increasing_subsequence | O(n^2) | O(n) |
| 08 | word_break | O(n^2) (n^3 with slicing cost) | O(n) |
| 09 | decode_ways | O(n) | O(1) |
| 10 | maximum_product_subarray | O(n) | O(1) |

`07`'s O(n^2) has a well-known O(n log n) alternative (patience
sorting with binary search) — worth knowing it exists and roughly how
it works, but the O(n^2) version here is the one to have completely
solid first, since it's what most interviewers expect derived live
before asking about the optimization.

## Common interview follow-ups to be ready for

- `climbing_stairs`: "what if you could climb 1, 2, or 3 steps?" —
  the rolling-pair becomes a rolling-triple (`prev3 + prev2 + prev1`);
  good to show the pattern generalizes rather than being memorized
  for exactly two step sizes.
- `house_robber`: "can you reconstruct *which* houses were robbed,
  not just the total?" — needs the full dp array (not rolling
  variables) plus a backtrack from the end, choosing "robbed" whenever
  `dp[i] != dp[i-1]`.
- `coin_change`: "what if a solution isn't guaranteed to exist?" —
  already handled here (`-1` return); make sure to state the
  `float('inf')` sentinel trick explicitly if asked to explain it.
- `coin_change_ii`: be ready to swap the loop order live and explain
  *in words* why it changes combinations into permutations — this is
  the question most likely to come up as a live follow-up here.
- `longest_increasing_subsequence`: "can you get O(n log n)?" — sketch
  patience sorting: maintain a list of smallest tail values for
  increasing subsequences of each length, binary search for where
  each new element belongs, and the final list's length is the answer.
- `word_break`: "can you return one valid segmentation, not just
  yes/no?" — store a `break_point` array alongside `dp`, or switch to
  the backtracking version from
  `10_recursion_backtracking/08_palindrome_partitioning`'s shape if
  *all* segmentations are needed instead of just one.
- `maximum_product_subarray`: "why track a running min if the
  question only asks for a max?" — be ready with the sign-flip
  explanation as a one-liner, since this is the most commonly
  misunderstood part of the solution.

## Self-check before moving on

You should be able to, without looking at the code:
- State which of `01`/`02`/`04`/`09` uses which combination function
  (`+`, `max`, `min`, gated `+`) from memory.
- Explain the "reduce circular to two linear calls" trick from `03`
  and identify when a similar reduction would apply to a new problem.
- Explain, in one sentence each, why `coin_change` needs a full array
  while `climbing_stairs` only needs two variables.
- Swap `coin_change_ii`'s loop order on paper and explain what the
  swapped version would actually be counting.
- Explain why `maximum_product_subarray` needs both a running max and
  a running min, with a concrete 3-element example that breaks a
  max-only version.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to
`14_dynamic_programming_2d`.
