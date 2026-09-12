# Graphs — Tutorial

Covers the 10 problems solved in this folder. A graph problem is
almost always one of two underlying questions dressed up differently:
"what can I reach from here" (traversal/connectivity) or "in what
order must these things happen" (ordering under dependency
constraints). Grids are graphs in disguise — each cell is a node,
each 4-directional neighbor relationship is an edge — which is why
this folder starts on grids before moving to explicit adjacency-list
graphs.

## The patterns

### 1. Grid DFS — the base template (`01`, `02`, `03`)
One guard clause (bounds check + validity check) at the top of the
recursive call, then recurse to all 4 neighbors. What differs across
these three problems is only *what the DFS accomplishes*:
- `flood_fill`: mutates cells as it visits them.
- `number_of_islands`: uses a separate `visited` set (keeps input
  unmodified) and counts how many times a *new* DFS had to start from
  an unvisited cell — that count is the number of components.
- `max_area_of_island`: the DFS *returns a value* (1 + sum of what
  each neighbor call returns) instead of just marking cells — the
  same "combine children's answers" recursive shape from the trees
  topic, applied to a grid's implicit graph.

### 2. Multi-source BFS (`04`)
`rotting_oranges` needs *minimum time*, which requires BFS, not DFS —
BFS naturally processes cells in order of distance from a source,
which corresponds exactly to elapsed time here. "Multi-source" means
seeding the queue with *every* initially-rotten orange at once
(distance/time 0 for all of them simultaneously), not just one
starting point — the queue then expands the rot outward from all
sources in lockstep, and the last time popped is the total time
needed.

### 3. Traversing an explicit graph with cycles (`05`)
`clone_graph` is the first problem here on an explicit adjacency-list
graph (not a grid), and the first where a *plain* DFS would infinite-
loop without a visited check, since undirected neighbor relationships
create cycles by nature. The `original -> clone` dict does double
duty: it's the visited-check (already a key means already fully
handled) and it's how neighbor references get wired to the correct
existing clone instead of creating duplicates.

### 4. Component counting on an explicit graph (`06`)
Directly generalizes `02`'s island-counting from a grid's implicit
adjacency to an explicit edge list: build an adjacency list from the
edges once, then the exact same "scan for unvisited nodes, DFS from
each one found, count how many times a new DFS started" logic applies
unchanged.

### 5. Directed-graph cycle detection with 3 states (`07`)
Undirected cycle detection (`09`) only needs visited/unvisited,
because re-encountering *any* visited neighbor (other than the
immediate parent) means a cycle. Directed graphs need a third state:
unvisited, *currently on the recursion stack* ("visiting"), and fully
done. A cycle exists specifically when DFS reaches a node still in
the "visiting" state — a back edge to an ancestor on the current
path — not just any previously-visited node, since two different
paths in a DAG can legitimately converge on an already-*done* node
without that being a cycle.

### 6. Topological sort via BFS on in-degree (`08`)
Kahn's algorithm answers "in what order" using the same "peel off
what's currently unblocked" idea as `07`'s cycle check, but built on
in-degree counting and BFS instead of DFS coloring. Nodes with
in-degree 0 have no unmet dependencies, so they're immediately
takeable; taking one conceptually removes it from the graph by
decrementing its neighbors' in-degrees, and any neighbor that drops
to 0 becomes takeable in turn. If the final processed count is less
than the total node count, some nodes were stuck depending on each
other in a cycle and never reached in-degree 0 — this is actually an
alternative way to detect the same cycles `07` finds via coloring.

### 7. Undirected connectivity + acyclicity together (`09`)
`graph_valid_tree` needs both "no cycle" and "fully connected" to
hold simultaneously. The `edges == n - 1` check is a free O(1) filter
(a tree-shaped graph has exactly that many edges by definition); the
DFS then only needs to check for cycles (skip the immediate parent —
that's just the edge you arrived on, not a real cycle — but treat any
*other* already-visited neighbor as one) and confirm every node got
reached.

### 8. Two multi-source traversals instead of one per cell (`10`)
`pacific_atlantic_water_flow`'s brute-force framing ("does water from
this cell reach both oceans") would need one flood-fill per cell.
Reversing the question — "which cells could water flow backward into
from the ocean" — turns it into exactly two multi-source traversals
(one seeded from all Pacific-border cells, one from all
Atlantic-border cells), with the flow condition also reversed
(walking toward *higher or equal* ground instead of lower, since
that's what "backward" means here). The answer is just the
intersection of the two visited sets. This "run the traversal
backward from the target instead of forward from every possible
source" reframing is a generally useful trick whenever a problem
asks about reachability *to* something from *many* possible starting
points.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | flood_fill | O(rows·cols) | O(rows·cols) recursion depth |
| 02 | number_of_islands | O(rows·cols) | O(rows·cols) |
| 03 | max_area_of_island | O(rows·cols) | O(rows·cols) |
| 04 | rotting_oranges | O(rows·cols) | O(rows·cols) |
| 05 | clone_graph | O(V+E) | O(V) |
| 06 | number_of_connected_components | O(V+E) | O(V+E) |
| 07 | course_schedule | O(V+E) | O(V+E) |
| 08 | course_schedule_ii | O(V+E) | O(V+E) |
| 09 | graph_valid_tree | O(V+E) | O(V+E) |
| 10 | pacific_atlantic_water_flow | O(rows·cols) | O(rows·cols) |

Every problem here is linear in graph/grid size (V+E, or rows·cols) —
the recurring interview expectation for BFS/DFS-based graph problems.
If a proposed solution is worse than that (e.g. re-traversing from
every cell independently, as the brute-force framing of `10` would),
that's usually the signal to look for a multi-source or
reversed-direction reframing instead.

## Common interview follow-ups to be ready for

- `number_of_islands` / `max_area_of_island`: "can you do it with
  BFS instead of DFS?" — yes, swap the recursive calls for a queue;
  the visited-tracking logic is identical either way.
- `rotting_oranges`: "why not DFS?" — be ready to state precisely:
  DFS would reach some fresh oranges via a long path before reaching
  closer ones via a short path, giving wrong (too-large) times;
  BFS's level-by-level property is what guarantees correct minimums.
- `clone_graph`: "what if the graph were directed instead of
  undirected?" — the same dict-based DFS still works unchanged, since
  the visited-check doesn't depend on edges being bidirectional.
- `course_schedule` / `course_schedule_ii`: "DFS coloring vs. Kahn's
  BFS - which do you prefer and why?" — both are O(V+E); Kahn's is
  often preferred when the actual order is needed (it falls out
  naturally), while DFS coloring is often more direct when only a
  yes/no cycle answer is needed.
- `graph_valid_tree`: "what if the graph could be disconnected with
  extra edges, i.e. not exactly n-1 edges?" — the O(1) edge-count
  filter no longer applies; would need to check connectivity AND
  acyclicity as two fully separate conditions instead of getting one
  for free from the other.
- `pacific_atlantic_water_flow`: "what if there were three oceans (or
  k of them)?" — the two-traversal-then-intersect approach
  generalizes cleanly to k traversals intersected together.

## Self-check before moving on

You should be able to, without looking at the code:
- Write the grid-DFS guard clause (bounds + validity check) from
  memory and explain why it belongs in one place, not repeated per
  direction.
- Explain why `rotting_oranges` must use BFS and what breaks with DFS.
- State the 3-state coloring used for directed-cycle detection and
  explain why "already fully done" is different from "currently on
  the path" when deciding if a cycle was found.
- Explain Kahn's algorithm's in-degree-decrement step and why a node
  becomes takeable exactly when its in-degree hits 0.
- Explain the "traverse backward from the target" reframing used in
  `pacific_atlantic_water_flow` and why it avoids one traversal per
  cell.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `12_graphs_advanced`.
