# DSA in Python — Interview Prep

Personal practice repo for Data Structures & Algorithms, aimed at
industry-level (product company) coding interviews. Python 3, solving
problems topic by topic, one folder per topic.

## How this repo works

- Each topic below gets its own folder (created as I reach it).
- **10 curated problems per topic**, numbered `01_` to `10_`, covering
  the sub-patterns of that data structure from easy to harder.
- Each problem is a single `.py` file: `NN_snake_case_problem_name.py`.
- Every solution file has:
  - A short docstring: problem statement + link (LeetCode/source).
  - The solution function(s).
  - A `if __name__ == "__main__":` block with a couple of test cases.
- **After all 10 problems in a topic are done**, that topic folder gets
  a `TUTORIAL.md` — a write-up covering the data structure/pattern
  itself, the sub-patterns seen across its 10 problems, complexity
  notes, and common interview variations/follow-ups.
- Commit after each problem (or small batch), message = `topic: problem name`.

## Syllabus — order to cover

### Phase 0 — Foundations (review, since Python is already solid)
- [ ] Big-O time/space complexity, best/avg/worst case
- [ ] Python performance gotchas: list vs deque, string concat, `in` on
      list vs set/dict, mutable default args, copy vs deepcopy

### Phase 1 — Core Data Structures

*(Each topic's 10-problem list is filled in here once we reach it.)*

- [ ] `01_arrays_strings` — traversal, in-place ops, prefix sums, sorting-based tricks
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. reverse_string (two-pointer)
      2. move_zeroes (two-pointer, in-place)
      3. remove_duplicates_sorted_array (two-pointer, in-place)
      4. max_subarray — Kadane's algorithm
      5. rotate_array (in-place via reversal, O(1) space)
      6. product_except_self (prefix/suffix arrays, no division)
      7. best_time_to_buy_sell_stock (single-pass, track min)
      8. merge_sorted_array (two-pointer from the back)
      9. valid_palindrome (string, two-pointer + char filtering)
      10. longest_common_prefix (string, vertical scan)
- [ ] `02_hashing` — dict/set based problems, frequency counting, grouping
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. two_sum (complement lookup)
      2. contains_duplicate (set membership)
      3. valid_anagram (frequency counting)
      4. group_anagrams (canonical-key grouping)
      5. top_k_frequent_elements (frequency + bucket sort)
      6. longest_consecutive_sequence (set-based O(n) run detection)
      7. subarray_sum_equals_k (prefix-sum + hash)
      8. intersection_of_two_arrays (set operations)
      9. isomorphic_strings (bijective two-way mapping)
      10. first_unique_character (frequency counting, two-pass)
- [ ] `03_two_pointers_sliding_window` — fixed/variable window, fast-slow pointers
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. max_average_subarray (fixed-size window)
      2. longest_substring_without_repeating (variable window, grow/shrink-on-invalid)
      3. minimum_size_subarray_sum (variable window, shrink-while-valid)
      4. longest_repeating_character_replacement (variable window + frequency budget)
      5. permutation_in_string (fixed window + count-dict matching)
      6. two_sum_sorted (converging two-pointer on sorted data)
      7. three_sum (sort + converging two-pointer per fixed element)
      8. container_with_most_water (converging two-pointer, greedy elimination)
      9. sort_colors (three-pointer partition, Dutch national flag)
      10. find_the_duplicate_number (fast-slow pointer, Floyd's cycle detection)
- [ ] `04_linked_list` — singly/doubly, reversal, cycle detection, merge, fast-slow
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. reverse_linked_list (in-place reversal)
      2. merge_two_sorted_lists (dummy head + splice)
      3. linked_list_cycle (fast-slow, detect)
      4. linked_list_cycle_ii (fast-slow, find cycle start)
      5. middle_of_linked_list (fast-slow, find middle)
      6. remove_nth_node_from_end (two-pointer fixed gap)
      7. palindrome_linked_list (middle + reversal + compare)
      8. reorder_list (middle + reversal + alternate merge)
      9. intersection_of_two_linked_lists (two-pointer list-switching)
      10. lru_cache (doubly linked list + hashmap, O(1) design)
- [ ] `05_stacks_queues` — monotonic stack, valid parens, queue via stacks, deque
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. valid_parentheses (plain LIFO matching)
      2. min_stack (auxiliary stack for O(1) queries)
      3. evaluate_reverse_polish_notation (postfix evaluation)
      4. daily_temperatures (monotonic decreasing stack)
      5. next_greater_element (monotonic stack + hashmap)
      6. largest_rectangle_in_histogram (monotonic increasing stack)
      7. implement_queue_using_stacks (two stacks, lazy transfer)
      8. implement_stack_using_queues (deque rotation)
      9. sliding_window_maximum (monotonic deque)
      10. decode_string (stack-based nested parsing)
- [ ] `06_binary_search` — classic + on answer space (binary search the answer)
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. binary_search (exact-match baseline)
      2. search_insert_position (left-boundary search)
      3. first_and_last_position (left-boundary search, twice)
      4. search_rotated_sorted_array (search on broken sortedness)
      5. find_minimum_rotated_sorted_array (rotation break-point)
      6. find_peak_element (search on slope, not order)
      7. search_2d_matrix (flattened 2D search)
      8. koko_eating_bananas (binary search on answer space)
      9. capacity_to_ship_packages (binary search on answer space)
      10. median_of_two_sorted_arrays (binary search on a partition point)
- [ ] `07_trees` — traversals (recursive/iterative), BST ops, height/diameter, LCA
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. binary_tree_inorder_traversal (iterative DFS with explicit stack)
      2. maximum_depth_of_binary_tree (simplest recursion template)
      3. invert_binary_tree (recursive tree rebuild)
      4. level_order_traversal (BFS with queue)
      5. symmetric_tree (structural mirror comparison)
      6. diameter_of_binary_tree (global answer during per-node pass)
      7. balanced_binary_tree (early-exit sentinel, avoid recomputation)
      8. validate_bst (range threaded through recursion)
      9. lowest_common_ancestor_bst (exploit BST ordering)
      10. lowest_common_ancestor_binary_tree (general-tree LCA, both subtrees)
- [ ] `08_heaps_priority_queue` — kth largest, merge k lists, top-k patterns
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. last_stone_weight (direct max-heap simulation)
      2. kth_largest_element_in_array (size-k min-heap)
      3. kth_largest_element_in_a_stream (size-k heap, persisted across calls)
      4. k_closest_points_to_origin (size-k max-heap over derived key)
      5. meeting_rooms_ii (heap over end times)
      6. task_scheduler (max-heap + cooldown queue)
      7. merge_k_sorted_lists (k-way merge via heap)
      8. ugly_number_ii (heap-driven generation)
      9. reorganize_string (greedy max-heap + one-step delay)
      10. find_median_from_data_stream (two heaps, balanced split)
- [ ] `09_tries` — prefix trees, word search/autocomplete style problems
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. implement_trie (foundational insert/search/starts_with)
      2. add_and_search_word (wildcard search via DFS)
      3. replace_words (stop at first/shortest match)
      4. longest_word_in_dictionary (constrained traversal)
      5. map_sum_pairs (aggregate stored at every node)
      6. word_search_ii (trie-guided grid backtracking)
      7. search_suggestions_system (autocomplete, precomputed top-3)
      8. short_encoding_of_words (reversed-word trie for suffixes)
      9. maximum_xor_of_two_numbers (binary trie over bits)
      10. prefix_and_suffix_search (combined-key trick)

### Phase 2 — Algorithmic Patterns
- [ ] `10_recursion_backtracking` — subsets, permutations, combinations, N-queens, sudoku
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. subsets (record at every node, start index)
      2. subsets_ii (same-level duplicate skip)
      3. permutations (used array, record only at leaves)
      4. combination_sum (reuse allowed, target-sum pruning)
      5. combination_sum_ii (no reuse + duplicate skip + break optimization)
      6. generate_parentheses (counter-gated choices, no input array)
      7. letter_combinations_of_phone_number (pure Cartesian product)
      8. palindrome_partitioning (backtrack over cut points)
      9. n_queens (O(1) constraint checks via auxiliary sets)
      10. sudoku_solver (boolean short-circuit on first solution)
- [ ] `11_graphs` — BFS/DFS, connected components, topological sort, cycle detection
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. flood_fill (grid DFS base template)
      2. number_of_islands (grid DFS, component counting)
      3. max_area_of_island (grid DFS, combine children's answers)
      4. rotting_oranges (multi-source BFS, minimum time)
      5. clone_graph (explicit graph traversal + visited dict)
      6. number_of_connected_components (explicit graph, component counting)
      7. course_schedule (directed cycle detection, 3-state DFS)
      8. course_schedule_ii (topological sort, Kahn's BFS)
      9. graph_valid_tree (undirected connectivity + acyclicity)
      10. pacific_atlantic_water_flow (reversed multi-source traversal)
- [ ] `12_graphs_advanced` — union-find (DSU), Dijkstra, Bellman-Ford, MST (Kruskal/Prim)
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. union_find (foundational DSU: find + union, path compression + union by rank)
      2. redundant_connection (DSU cycle detection on explicit edges)
      3. number_of_provinces (DSU component counting)
      4. accounts_merge (DSU over derived/shared-key relationships)
      5. network_delay_time (Dijkstra, single-source shortest path)
      6. path_with_minimum_effort (Dijkstra minimax variant)
      7. cheapest_flights_within_k_stops (Bellman-Ford, edge-count bounded)
      8. connecting_cities_minimum_cost (Kruskal's MST via DSU)
      9. min_cost_to_connect_all_points (Prim's MST via heap)
      10. find_the_city (Floyd-Warshall, all-pairs shortest path)
- [ ] `13_dynamic_programming_1d` — climbing stairs, house robber, coin change, LIS
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. climbing_stairs (rolling-pair, Fibonacci sum)
      2. house_robber (rolling-pair, max under adjacency constraint)
      3. house_robber_ii (circular reduced to two linear calls)
      4. min_cost_climbing_stairs (rolling-pair, min of two predecessors)
      5. coin_change (full DP array, minimum count, unbounded)
      6. coin_change_ii (full DP array, combination count, loop-order matters)
      7. longest_increasing_subsequence (full DP array, variable predecessors)
      8. word_break (reachability DP over split points)
      9. decode_ways (rolling-pair, gated Fibonacci)
      10. maximum_product_subarray (running max + min, sign-flip handling)
- [ ] `14_dynamic_programming_2d` — grid DP, knapsack, LCS, edit distance, palindromes
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. unique_paths (grid DP, count paths)
      2. minimum_path_sum (grid DP, min-cost path)
      3. longest_common_subsequence (two-string DP, match/mismatch)
      4. edit_distance (two-string DP, three-way min)
      5. zero_one_knapsack (foundational skip-or-take DP)
      6. partition_equal_subset_sum (knapsack disguised as subset-sum feasibility)
      7. target_sum (knapsack disguised as subset-sum counting, via algebra)
      8. longest_palindromic_substring (palindrome table, length-order fill)
      9. palindromic_substrings (same table, different readout)
      10. interleaving_string (two-string DP against a fixed third string)
- [ ] `15_greedy` — interval scheduling, jump game, gas station
      **(10/10 problems solved, see TUTORIAL.md — not yet self-practiced, so unchecked)**
      1. lemonade_change (prefer the more flexible resource)
      2. best_time_to_buy_and_sell_stock_ii (decompose optimum into local gains)
      3. jump_game (running farthest-reach tracking)
      4. jump_game_ii (implicit BFS via farthest-reach levels)
      5. gas_station (reset search boundary, skip failed stretch)
      6. non_overlapping_intervals (sort by end time, count rejections)
      7. minimum_arrows_to_burst_balloons (sort by end time, count coverage)
      8. partition_labels (extend boundary to cover active elements)
      9. candy (two passes for a bidirectional constraint)
      10. queue_reconstruction_by_height (processing order avoids self-interference)
- [ ] `16_intervals` — merge/insert intervals, meeting rooms
- [ ] `17_bit_manipulation` — XOR tricks, bitmasking, subsets via bits

### Phase 3 — Interview Readiness
- [ ] `18_mixed_mock_practice` — timed, random-topic problems (simulate real rounds)
- [ ] Revisit weak topics flagged during Phase 1–2
- [ ] Mock interviews (explain approach out loud, code in ~25–30 min, no IDE hints)

## Progress tracking

Check off syllabus items above as topics are *comfortable*, not just
"done once." A topic counts as done when a new problem in that pattern
can be solved without looking up the technique.

## Setup

```bash
python3 --version   # 3.x
# no external deps needed to start — pure Python stdlib
```

## Remote

https://github.com/meharuhanzz/dsa
