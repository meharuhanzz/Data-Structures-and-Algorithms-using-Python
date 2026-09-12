# Recursion & Backtracking — Tutorial

Covers the 10 problems solved in this folder, opening Phase 2 of the
syllabus (Algorithmic Patterns) after Phase 1's 9 core data structure
topics. Every single problem here uses the exact same three-step
shape:

```python
def backtrack(state):
    if base_case:
        record_or_return
    for choice in options(state):
        make_choice(choice)      # choose
        backtrack(next_state)    # explore
        undo_choice(choice)      # un-choose
```

What changes between problems is *what counts as a choice*, *what
the base case is*, and *what pruning rule skips bad choices early*.
Once that shape is automatic, "backtracking problem" stops being
intimidating and becomes a fill-in-the-blanks exercise.

## The patterns

### 1. Record at every node vs. only at the leaves (`01`/`02` vs `03`)
Subsets are valid at *every* partial length — `[1]` and `[1,2]` are
both legitimate subsets of `[1,2,3]` — so `subsets` records `path`
into the result at the top of every call, before the loop even runs.
Permutations are only valid once *complete* — a partial arrangement
isn't a permutation of anything — so `permutations` only records at
the base case where `len(path) == len(nums)`. Knowing which of these
two a problem needs is often the first fork in the road.

### 2. `start` index vs. `used` array (`01`/`02` vs `03`)
Subsets and combinations care about *combinations*, not order, so a
`start` index ensures each element is only chosen after ones already
in the path — this alone prevents `[1,2]` and `[2,1]` from both
appearing. Permutations care about order, so instead of a `start`
index there's a `used` boolean array — every not-yet-used element is
a valid next choice regardless of position.

### 3. Skipping duplicates at the same tree level (`02`, `05`)
When the input has duplicate values but the output must not have
duplicate results, sort first (so equal values become adjacent), then
skip a candidate if it equals the *previous* candidate at the same
level of the loop (`i > start and nums[i] == nums[i-1]`). The
`i > start` guard is the whole trick: it allows two equal values to
be used *together* within one path (that's fine, produces a valid
combination), while blocking two equal values from each *starting* a
sibling branch at the same level (that would just regenerate the
same combination twice).

### 4. Reuse allowed vs. not allowed (`04` vs `05`)
Both are "find combinations summing to target," differing in one
line: `combination_sum` recurses with `backtrack(i, ...)`, allowing
the same index to be chosen again immediately (reuse); `combination_
sum_ii` recurses with `backtrack(i + 1, ...)`, moving strictly
forward (no reuse). Small change, and worth stating out loud in an
interview exactly *why* that one index matters.

### 5. Pruning as soon as a choice is provably bad (`04`, `05`)
`combination_sum` prunes the instant `remaining < 0` — no point
exploring further down a branch that already overshot the target.
`combination_sum_ii` goes further: because candidates are sorted,
the moment `candidates[i] > remaining`, *every later* candidate is
also too big, so the loop can `break` entirely rather than just
skip one option — pruning a whole remaining sub-branch at once.

### 6. Counters instead of an index for the base case (`06`)
`generate_parentheses` doesn't backtrack over a fixed input array at
all — the "choices" are just "add an open paren" or "add a close
paren," gated by two counters (`open_count < n`, `close_count <
open_count`) instead of a `start`/`used` structure. The second gate
is what keeps every *prefix* valid, not just the finished string —
worth noticing this is a stronger guarantee than checking validity
only at the end.

### 7. Pure Cartesian product, no pruning (`07`)
`letter_combinations` has no constraint to check at all — every
letter for the current digit is always a valid next choice. It's
included specifically to show that backtracking's value isn't always
about pruning; sometimes it's just a clean way to generate a nested
Cartesian product without knowing the nesting depth ahead of time.

### 8. Backtracking over where to cut, not what to pick (`08`)
`palindrome_partitioning` chooses *substring boundaries* rather than
elements from a fixed array — at each position, every possible end
point for the next piece is a candidate choice, filtered by whether
that specific substring is a palindrome. The base case is reaching
the end of the string with every character assigned to some valid
piece.

### 9. O(1) constraint checks via auxiliary sets (`09`)
N-Queens is the first problem here needing to check a *derived*
property (does this placement conflict with any earlier one)
efficiently. Placing one queen per row makes row-conflicts
structurally impossible by construction; column and diagonal
conflicts are checked in O(1) via sets keyed by the invariant that's
constant along each constraint (`c` for columns, `r-c` and `r+c` for
the two diagonal directions) — avoiding an O(n) board scan on every
single placement attempt.

### 10. Return-a-boolean to stop at the first solution (`10`)
Every earlier problem collects *all* valid results. Sudoku only needs
*one* solved board, so `solve_sudoku`'s backtrack function returns
`True`/`False` and the search short-circuits (`if backtrack(idx+1):
return True`) the instant a full solution is found, instead of
continuing to explore for alternatives that aren't needed. This
return-a-boolean-to-short-circuit shape is worth recognizing as a
distinct variant from the "collect everything" shape used everywhere
else in this folder — it changes how the un-choose step is guarded
(only undo if the recursive call *failed*).

## Complexity summary

| # | Problem | Time (worst case) | Extra space |
|---|---|---|---|
| 01 | subsets | O(n · 2^n) | O(n) recursion depth |
| 02 | subsets_ii | O(n · 2^n) | O(n) |
| 03 | permutations | O(n · n!) | O(n) |
| 04 | combination_sum | O(2^target) rough bound | O(target) |
| 05 | combination_sum_ii | O(2^n) | O(n) |
| 06 | generate_parentheses | O(4^n / sqrt(n)) (Catalan number) | O(n) |
| 07 | letter_combinations_of_phone_number | O(4^n) | O(n) |
| 08 | palindrome_partitioning | O(n · 2^n) | O(n) |
| 09 | n_queens | O(n!) rough bound | O(n) |
| 10 | sudoku_solver | O(9^(empty cells)) worst case | O(1) beyond the sets |

These are inherently exponential problems — the whole point of the
pruning tricks in patterns 3, 5, and 9 is to cut down the *constant
factor and practical branching* of that exponential search, not to
change its fundamental complexity class. Be ready to say this
explicitly: backtracking problems are rarely "optimized to
polynomial," they're "optimized to prune aggressively within an
exponential search."

## Common interview follow-ups to be ready for

- `subsets`/`permutations`: "can you generate them iteratively
  instead of recursively?" — subsets can be built iteratively (each
  existing subset doubles: with/without the next element); an
  iterative permutation generator (e.g. Heap's algorithm) is
  possible but far less natural to derive live than the recursive one.
- `combination_sum`: "what if negative numbers were allowed in
  candidates?" — the `remaining < 0` pruning stops working (a
  negative number could bring remaining back toward 0 later), and the
  search could become infinite with reuse allowed; discuss why the
  problem's constraints (positive candidates) make the pruning valid.
- `generate_parentheses`: "how many valid strings are there for a
  given n?" — the nth Catalan number; knowing this names the
  complexity precisely instead of a vague "exponential."
- `n_queens`: "what if you only needed the *count* of solutions, not
  every board?" — drop the `board` reconstruction and the `result`
  list, just increment a counter at the base case; saves the O(n)
  string-building cost per solution.
- `sudoku_solver`: "how would you speed this up further?" — pick the
  empty cell with the *fewest* remaining valid candidates first
  (most-constrained-variable heuristic) rather than processing empty
  cells in a fixed left-to-right order; dramatically prunes the
  search in practice even though worst-case complexity is unchanged.
- General: "what's the difference between backtracking and plain
  DFS?" — be ready with a one-sentence answer: backtracking is DFS
  over a space of *choices* with explicit undo, used to explore all
  valid combinations/arrangements/placements, versus DFS over a fixed
  graph/tree structure that already exists.

## Self-check before moving on

You should be able to, without looking at the code:
- Write the choose/explore/un-choose skeleton from memory and adapt
  it live to a new problem statement.
- Explain the difference between a `start` index and a `used` array,
  and state which one a new problem needs just from reading whether
  it asks for combinations or permutations.
- Explain the `i > start` duplicate-skip guard and why it's not the
  same as just checking `nums[i] == nums[i-1]` unconditionally.
- State why N-Queens' three constraint sets each use a different key
  (`c`, `r-c`, `r+c`) and what invariant each key captures.
- Explain why Sudoku's backtrack function returns a boolean while
  every other problem in this folder returns nothing and just
  appends to a shared result list.

This is the first topic of Phase 2 (Algorithmic Patterns) per the
README's syllabus, following Phase 1's 9 core data structure topics —
next up is `11_graphs`.
