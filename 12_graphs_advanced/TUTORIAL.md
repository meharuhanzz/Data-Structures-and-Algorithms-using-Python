# Graphs Advanced — Tutorial

Covers the 10 problems solved in this folder: Union-Find and three
applications, then the shortest-path family (Dijkstra, a minimax
variant, Bellman-Ford, Floyd-Warshall), then Minimum Spanning Trees
via both Kruskal's and Prim's. Where `11_graphs` was almost entirely
BFS/DFS, this topic is about *weighted* graphs and the specific
algorithm each weight-related question calls for.

## The patterns

### 1. Union-Find as a foundation (`01`)
Every node starts as its own set; `find(x)` walks to the set's root
with path compression (repointing visited nodes directly to the
root, so future lookups are near O(1)); `union(x, y)` merges two
sets by attaching the smaller-rank tree under the larger one. The
single most useful fact about it: `union()`'s return value (whether
the two nodes were already connected) *is* a cycle/redundancy check,
for free — no separate DFS needed.

### 2. Union-Find for explicit-edge cycle/component problems (`02`, `03`)
- `redundant_connection`: process edges in order, union each pair;
  the first edge whose endpoints are already connected is the one
  closing a cycle.
- `number_of_provinces`: union every directly-connected pair from an
  adjacency matrix; the number of distinct roots left is the number
  of components (the same question `11_graphs/06` solved via DFS —
  worth comparing both approaches side by side to build the instinct
  for recognizing this problem shape either way).

### 3. Union-Find over derived relationships, not explicit edges (`04`)
`accounts_merge` doesn't start with a graph at all — the "edges" are
inferred from shared emails between account entries. This generalizes
the pattern: whenever records need merging based on *any* shared
key (not just an explicit adjacency list), Union-Find over record
indices, with unions triggered by shared-key collisions, is the tool.

### 4. Dijkstra — single-source shortest path, non-negative weights (`05`)
A min-heap always pops the currently-closest unfinalized node, and
because weights are non-negative, that popped distance is guaranteed
final the moment it's popped — no cheaper path could ever be found
through a node that's farther away. The `if d > dist[node]: continue`
guard discards stale heap entries left over from before a better path
was found. This guarantee is exactly what breaks with negative edges
(a "farther" node could still lead to a big negative-weight shortcut
later), which is why Dijkstra requires non-negative weights and why
`07` exists for the case where that assumption doesn't hold.

### 5. Turning Dijkstra into a minimax shortest path (`06`)
`path_with_minimum_effort` keeps every part of Dijkstra's structure
except one line: the relaxation formula changes from
`current + weight` (accumulate) to `max(current, weight)` (worst
step wins). Recognizing that a single formula swap adapts Dijkstra
to "minimize the worst edge" instead of "minimize the total" is a
reusable trick, not a new algorithm to memorize separately.

### 6. Bellman-Ford — shortest path bounded by edge count (`07`)
Dijkstra finds the *unconstrained* cheapest path, which may use more
edges than allowed. Bellman-Ford instead relaxes *every* edge for
exactly k+1 rounds, where round i finds the best cost reachable using
at most i edges — directly modeling an edge-count limit that Dijkstra
has no way to express. The critical implementation detail: each round
must relax against a *snapshot* of the previous round's distances,
never the array being mutated live, or a single round could silently
chain multiple relaxations together and exceed the edge budget it's
supposed to represent.

### 7. Floyd-Warshall — all-pairs shortest path (`10`)
When shortest paths are needed *between every pair* of nodes (not
just from one source), Floyd-Warshall computes all of them in one
O(n^3) pass: for every candidate intermediate city k, check whether
routing i -> k -> j beats the current known i -> j distance, over the
whole matrix. This trades a higher complexity bound for getting every
pair's answer in a single unified pass instead of running a
single-source algorithm (like `05`) n separate times.

### 8. Kruskal's MST — cheapest edges first, via Union-Find (`08`)
Sort all edges by weight, then greedily accept any edge connecting
two currently-separate components (`union()` returning True is
exactly "this edge is useful"); reject any edge that would just
create a cycle (`union()` returning False). This is Union-Find's
other classic use, distinct from the connectivity-check role in
`02`-`04` — here it's the mechanism that prevents a spanning tree
from ever containing a cycle while it's being built greedily.

### 9. Prim's MST — grow one tree outward, via a heap (`09`)
When the graph is *complete* (every pair of nodes is a potential
edge, as with points on a plane), listing and sorting all O(n^2)
edges up front for Kruskal's is wasteful. Prim's instead grows a
single tree from one starting node, repeatedly pulling in the
cheapest edge connecting the tree to any node not yet in it — same
"pop cheapest from a heap, skip if stale" shape as Dijkstra (`05`),
differing only in whether the heap key is distance-from-source or
distance-from-the-growing-tree. Distances to unvisited nodes are
computed on demand as each new node joins, rather than needing the
full edge list precomputed.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | union_find | ~O(1) amortized per op | O(n) |
| 02 | redundant_connection | ~O(n α(n)) | O(n) |
| 03 | number_of_provinces | O(n^2) | O(n) |
| 04 | accounts_merge | O(total emails · α(n)) | O(total emails) |
| 05 | network_delay_time | O(E log V) | O(V+E) |
| 06 | path_with_minimum_effort | O(rows·cols · log(rows·cols)) | O(rows·cols) |
| 07 | cheapest_flights_within_k_stops | O(k · E) | O(V) |
| 08 | connecting_cities_minimum_cost | O(E log E) | O(V) |
| 09 | min_cost_to_connect_all_points | O(n^2 log n) | O(n) |
| 10 | find_the_city | O(n^3) | O(n^2) |

(α(n) is the inverse Ackermann function — effectively constant for
any n that could ever appear in practice, which is the formal
justification behind calling Union-Find operations "near O(1)".)

## Common interview follow-ups to be ready for

- `union_find`: "what if you skipped path compression or union by
  rank?" — either one alone still gives correct results but degrades
  worst-case find() to O(n) (a long chain); be ready to explain why
  *both together* are what give the near-O(1) amortized bound.
- `redundant_connection`: "what if the graph were directed?" — plain
  Union-Find no longer directly applies (it's inherently for
  undirected connectivity); a directed cycle needs the 3-state DFS
  approach from `11_graphs/07` instead.
- `network_delay_time`: "what if edge weights could be negative?" —
  Dijkstra's correctness guarantee breaks immediately; that's
  precisely the scenario `07`'s Bellman-Ford handles instead.
- `path_with_minimum_effort`: "can you solve this with binary search
  instead?" — yes: binary search on the answer (the max allowed
  effort), with a BFS/DFS feasibility check at each candidate — a
  nice alternative to mention, connecting back to
  `06_binary_search`'s "binary search on the answer space" pattern.
- `cheapest_flights_within_k_stops`: "why not just use Dijkstra with
  a stop-count added to the state?" — actually a valid alternative
  (track (node, stops_used) as the Dijkstra state instead of just
  node); worth knowing as a second correct approach beyond
  Bellman-Ford.
- `connecting_cities_minimum_cost` / `min_cost_to_connect_all_points`:
  "when would you pick Kruskal's over Prim's, or vice versa?" — sparse
  explicit edge lists favor Kruskal's (sort once, O(E log E));
  dense/complete graphs favor Prim's (avoids materializing O(n^2)
  edges up front).
- `find_the_city`: "why not just run Dijkstra n times instead of
  Floyd-Warshall?" — n runs of Dijkstra cost O(n · E log V), which
  can beat O(n^3) on sparse graphs; Floyd-Warshall wins specifically
  when the graph is dense or when its simplicity outweighs the
  asymptotic difference for the given n.

## Self-check before moving on

You should be able to, without looking at the code:
- Write Union-Find's `find` (with path compression) and `union` (with
  union by rank) from memory.
- Explain precisely why Dijkstra requires non-negative weights and
  what specifically breaks with a negative edge.
- State the one-line relaxation-formula change that turns Dijkstra
  into the minimax path algorithm used in `06`.
- Explain why Bellman-Ford's per-round relaxation must use a snapshot
  of the previous round's distances, with a concrete example of what
  goes wrong without it.
- State when Kruskal's is preferable to Prim's and vice versa, in one
  sentence each.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to
`13_dynamic_programming_1d`.
