# Trees — Tutorial

Covers the 10 problems solved in this folder, plus the shared
`tree_node.py` (a `TreeNode` class and `build_tree`/`to_level_order`/
`find_node` helpers used by every test harness here).

Almost every tree problem is a variation on the same shape: define
what a function should compute *for a single node*, assuming its
children already know the answer for themselves (recursion handles
the "assuming" part for free), then combine those child answers at
the current node. The 10 problems below are really 10 different
answers to "what do you combine, and how."

## The patterns

### 1. Depth-first traversal — recursive vs. explicit stack (`01`)
Recursive inorder (`inorder(left); visit(node); inorder(right)`) is
one line, but it's secretly using the call stack as storage. Making
that storage explicit: push every node down a left-child chain onto
a stack (mirrors "go as far left as possible"), pop and visit one,
then repeat the same left-chain push starting from its right child.
Worth doing once by hand, since interviewers sometimes specifically
ask for the iterative version to check this isn't just memorized.

### 2. Simplest recursion — compute one value per subtree (`02`)
`max_depth` is the template every later pattern builds on: base case
returns a trivial value for an empty subtree (0), recursive case
combines the two children's answers with the current node's own
contribution (`1 + max(...)`). Nothing more complex than this
shape is needed for most "compute a number about this tree" problems.

### 3. Rebuilding instead of computing (`03`)
`invert_tree` uses the exact same recursive shape as pattern 2, but
returns a (modified) *node* instead of a number. Swap `root.left` and
`root.right` using the recursively-inverted versions of each — since
Python evaluates both call results before assigning, there's no risk
of overwriting one child before the other has been inverted.

### 4. Breadth-first traversal (`04`)
Every pattern so far is depth-first. Level order needs a queue
instead of a stack/recursion, and the one non-obvious detail is
snapshotting `len(queue)` *before* the inner loop that processes one
level — otherwise the children being pushed during that loop would
grow the count being iterated over and blur where one level ends and
the next begins.

### 5. Structural comparison across two subtrees (`05`)
`is_symmetric` compares two subtrees against each other rather than
computing one value for one tree. The key subtlety: mirror symmetry
means comparing `a.left` to `b.right` (outer-to-outer, inner-to-inner
swapped), not `a.left` to `b.left` (which would just check the two
sides are identical copies, a different and easier problem).

### 6. Computing a global answer during a per-node pass (`06`)
`diameter_of_binary_tree` needs the *best* value seen at *any* node
in the tree, not just the value at the root. Rather than a separate
traversal to find the max, piggyback on the height computation
(pattern 2's shape) with a `nonlocal` variable updated as a side
effect on every call — each call still returns the height its caller
needs, while also recording "the diameter through me" into the
shared running maximum.

### 7. Early-exit sentinel to avoid recomputation (`07`)
A naive "is this balanced" check recomputes height from scratch at
every node while separately checking balance, costing O(n^2) on a
skewed tree. `is_balanced` reuses pattern 2's height function directly
but returns -1 as a sentinel the instant a subtree below is found
unbalanced, and every caller checks for and immediately re-propagates
that -1 without doing further work. Each node's height is then
computed exactly once — O(n) total — with early termination once
imbalance is already known anywhere below.

### 8. Threading a valid range through the recursion (`08`)
The naive "check each node against its immediate parent" approach for
BST validation is wrong — it misses violations from higher ancestors
(see the worked counterexample in `08_validate_bst.py`). The fix:
pass a `(low, high)` range *down* through the recursion, tightened by
every ancestor so far (left children tighten the upper bound to the
parent's value, right children tighten the lower bound), not just the
immediate parent.

### 9. Exploiting BST ordering to skip a subtree entirely (`09`)
`lowest_common_ancestor_bst` doesn't need to explore both children
at any step. Comparing p and q's values to the current node's value
directly says which single subtree could possibly contain the LCA —
both smaller means go left, both larger means go right, and the
moment they're not both on the same side, the current node itself is
the split point. One walk down, no recursion into both branches.

### 10. General-tree LCA without ordering (`10`)
Without a BST's ordering property, there's no shortcut for which
side to search, so `lowest_common_ancestor_binary_tree` must explore
both. A call returns early the moment it hits p or q itself (a node
can be its own ancestor). If both the left and right recursive calls
come back non-None, p and q were found on opposite sides, so the
*current* node is where their paths converge; if only one side is
non-None, both targets are in that one subtree, so that result just
passes upward unchanged.

## Complexity summary

| # | Problem | Time | Extra space |
|---|---|---|---|
| 01 | binary_tree_inorder_traversal | O(n) | O(h) |
| 02 | maximum_depth_of_binary_tree | O(n) | O(h) |
| 03 | invert_binary_tree | O(n) | O(h) |
| 04 | level_order_traversal | O(n) | O(n) |
| 05 | symmetric_tree | O(n) | O(h) |
| 06 | diameter_of_binary_tree | O(n) | O(h) |
| 07 | balanced_binary_tree | O(n) | O(h) |
| 08 | validate_bst | O(n) | O(h) |
| 09 | lowest_common_ancestor_bst | O(h) | O(1) |
| 10 | lowest_common_ancestor_binary_tree | O(n) | O(h) |

`h` is the tree's height — O(log n) for a balanced tree, O(n) for a
completely skewed one (a "linked list in disguise"), which is why
interviewers often ask "what's the worst case?" specifically for
trees: a "balanced" complexity claim can quietly assume balance that
isn't guaranteed. `09` is the one problem here that's genuinely
faster than O(n), and only because it exploits the BST property to
avoid visiting most of the tree at all.

## Common interview follow-ups to be ready for

- `binary_tree_inorder_traversal`: "can you also do preorder and
  postorder iteratively?" — preorder is a small tweak of this same
  stack; postorder is the hardest of the three (commonly done by
  reversing a modified preorder, or tracking a "last visited" node).
- `diameter_of_binary_tree` / `balanced_binary_tree`: "why not compute
  height separately and diameter/balance separately?" — be ready to
  state the complexity cost explicitly: separate passes risk O(n^2)
  on skewed trees, versus O(n) for the combined single-pass version.
- `validate_bst`: "what if the tree has duplicate values?" — this
  implementation uses strict `<`/`>`, so duplicates anywhere are
  correctly rejected; confirm that's the intended rule before coding,
  since some variants allow equal values on one side.
- `lowest_common_ancestor_bst`: "what if the tree weren't a BST?" —
  degrades to problem 10's approach; be ready to explain concretely
  *why* the BST-specific shortcut becomes invalid without ordering.
- `lowest_common_ancestor_binary_tree`: "what if p or q might not
  actually be in the tree?" — this implementation assumes both exist
  (per the problem statement); discuss what changes if that's not
  guaranteed (a separate existence check first, or returning a
  sentinel).
- General: "what if the tree is extremely unbalanced / very deep?" —
  every recursive solution here risks a stack overflow on a
  sufficiently skewed tree; know that an iterative rewrite (explicit
  stack, as in `01`) is the fix, and be ready to sketch one live.

## Self-check before moving on

You should be able to, without looking at the code:
- Write the iterative inorder traversal from memory.
- Explain why level order needs `len(queue)` snapshotted before the
  inner loop.
- State the "combine child answers, propagate a global side effect"
  shape shared by diameter and balanced-tree, and why it avoids the
  naive O(n^2).
- Explain why BST validation must track a range from every ancestor,
  not just the immediate parent, with the specific counterexample
  that breaks a parent-only check.
- State the one-sentence difference between the BST and general-tree
  LCA algorithms, and why the BST version doesn't need both subtrees.

If any of those aren't fluent yet, this topic isn't "done" per the
README's definition — revisit before moving to `08_heaps_priority_queue`.
