# Dynamic Programming (2D) — Tutorial

Covers the 10 problems solved in this folder. Same underlying idea as
`13_dynamic_programming_1d` — build up from smaller subproblems — but
the state now needs *two* indices to describe: a position in each of
two strings, a row and column in a grid, or an item index paired with
a remaining capacity. Several of the "hardest" problems here (06, 07)
don't look like grid/knapsack problems at all from their statements —
recognizing the disguise is most of the difficulty.

## The patterns

### 1. Grid DP — position determined by (row, col) (`01`, `02`)
The most literal 2D DP: dp[r][c] describes something about reaching
cell (r, c), built from the cells directly above and to the left
(the only ways in, given the allowed moves). `unique_paths` sums the
two predecessors (count of ways); `minimum_path_sum` takes their
`min` plus the current cell's own cost. Same shape, different
combining operation — the same lesson as 1D DP's rolling-pair
problems, just one dimension up.

### 2. Two-string DP — comparing prefixes of two sequences (`03`, `04`, `10`)
dp[i][j] describes a relationship between the first i characters of
one string and the first j characters of another. The recurrence
almost always branches on whether the *current* characters match:
- `longest_common_subsequence`: match -> extend diagonally
  (dp[i-1][j-1] + 1); mismatch -> best of dropping one side
  (`max(dp[i-1][j], dp[i][j-1])`).
- `edit_distance`: match -> carry forward unchanged (dp[i-1][j-1]);
  mismatch -> `1 + min` of three specific edits, each mapping to a
  specific neighbor cell (replace = diagonal, delete = up, insert =
  left). Structurally LCS with `max` replaced by `min` and an
  unconditional `+1` added for the mismatch case.
- `interleaving_string`: a variant where i and j don't get compared
  to *each other* — they jointly point at a fixed position in a
  *third* string, and the question is whether either side's next
  character can extend a valid interleaving.

### 3. 0/1 Knapsack and its disguises (`05`, `06`, `07`)
`zero_one_knapsack` is the base case: for each item, skip it
(dp[i-1][cap] unchanged) or take it (dp[i-1][cap-weight] + value, only
if it fits) — critically reading from row **i-1** (not row i), since
each item can only be used once. This is what distinguishes it from
`13_dynamic_programming_1d`'s coin-change problems, where items
(coins) can repeat and the lookup stays on the same row/pass.
- `partition_equal_subset_sum`: not phrased as a knapsack at all, but
  "does some subset sum to total/2" is exactly "is capacity
  total/2 exactly fillable" with each item's value equal to its
  weight — a boolean reachability version of the knapsack table.
- `target_sum`: an algebra trick (`sum(P) - sum(N) = target`,
  `sum(P) + sum(N) = total`, solved together) reduces "assign +/-
  signs" down to "count subsets summing to a fixed target" — the
  *counting* version of 06's feasibility check.

Recognizing "this is secretly 0/1 knapsack" is the single most
valuable pattern-matching skill this folder builds — neither 06 nor
07 mentions weights, values, or capacity anywhere in its problem
statement.

### 4. Palindrome table filled by increasing length (`08`, `09`)
dp[i][j] = "is s[i..j] a palindrome?" True when the outer characters
match *and* the strictly-inside substring is also a palindrome
(dp[i+1][j-1]). The fill order matters here in a way it didn't for
grid DP: the table must be filled by increasing *substring length*,
not row-by-row or column-by-column, because computing a length-L
answer needs a strictly shorter substring's answer to already be
finalized. Once this table exists, different final questions read off
of it almost for free: `08` tracks the best (longest) True cell seen;
`09` just counts every True cell — same table, two different
one-line readouts.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | unique_paths | O(m·n) | O(m·n) |
| 02 | minimum_path_sum | O(m·n) | O(m·n) |
| 03 | longest_common_subsequence | O(m·n) | O(m·n) |
| 04 | edit_distance | O(m·n) | O(m·n) |
| 05 | zero_one_knapsack | O(n·capacity) | O(n·capacity) |
| 06 | partition_equal_subset_sum | O(n·target) | O(target) |
| 07 | target_sum | O(n·subset_sum) | O(subset_sum) |
| 08 | longest_palindromic_substring | O(n^2) | O(n^2) |
| 09 | palindromic_substrings | O(n^2) | O(n^2) |
| 10 | interleaving_string | O(m·n) | O(m·n) |

`06` and `07` show 1D space (not 2D) despite being knapsack-shaped —
because each item is only used once, the capacity dimension can be
collapsed to a single rolling array *if* it's iterated backward per
item (same reasoning as `13_dynamic_programming_1d/06_coin_change_
ii`'s loop-order requirement, adapted to the no-reuse setting).

## Common interview follow-ups to be ready for

- `unique_paths` / `minimum_path_sum`: "what if some cells are
  blocked/obstacles?" — set dp[r][c] = 0 (unreachable) or skip that
  cell in the min entirely for blocked cells; the rest of the
  recurrence is unchanged.
- `longest_common_subsequence`: "can you reconstruct the actual
  subsequence, not just its length?" — walk backward from dp[m][n]:
  on a match go diagonally and record the character; on a mismatch,
  step toward whichever neighbor the max came from.
- `edit_distance`: "can you print the actual sequence of edits?" —
  same backward-walk idea as LCS, tracking which of the three options
  (replace/delete/insert) produced each cell's value.
- `partition_equal_subset_sum`: "what if you needed exactly k
  subsets of equal sum, not just 2?" — a genuinely harder problem
  (partition into k equal-sum subsets), usually solved with
  backtracking + pruning rather than a direct DP extension; good to
  know this doesn't trivially generalize.
- `target_sum`: be ready to derive the `sum(P) = (target + total) / 2`
  algebra live, not just state the formula — that derivation is
  usually exactly what's being tested.
- `longest_palindromic_substring`: "can you do this in O(n) instead
  of O(n^2)?" — yes, Manacher's algorithm; know it exists as the
  advanced follow-up, but the O(n^2) DP here is the expected
  first-derived solution.
- `interleaving_string`: "what if there were three source strings
  interleaving into a fourth?" — the 2D table would need to become
  3D (one dimension per source string), same core recurrence idea
  extended by one more dimension.

## Self-check before moving on

You should be able to, without looking at the code:
- Write the grid-DP recurrence for both `unique_paths` and
  `minimum_path_sum` from memory and state what changes between them.
- Explain the LCS match/mismatch recurrence, then adapt it live into
  edit distance's three-way min.
- Explain why `zero_one_knapsack` reads from row i-1 while
  `13_dynamic_programming_1d/05_coin_change` reads from the same
  row/pass, and connect that difference to "each item used once" vs.
  "unlimited reuse."
- Derive `target_sum`'s reduction to subset-sum counting on paper,
  starting from the two equations.
- Explain why the palindrome table in `08`/`09` must be filled by
  increasing substring length rather than row-by-row.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `15_greedy`.
