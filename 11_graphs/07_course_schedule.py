"""
Problem: There are num_courses courses (0 to num_courses-1) and a
list of prerequisite pairs [course, prereq] meaning prereq must be
taken before course. Return True if it's possible to finish all
courses (i.e. the prerequisite graph has no cycle).
Source : LeetCode 207 - Course Schedule

Example:
    Input:  num_courses = 2, prerequisites = [[1, 0]]
    Output: True   (take 0, then 1)

    Input:  num_courses = 2, prerequisites = [[1, 0], [0, 1]]
    Output: False  (0 needs 1, 1 needs 0 - impossible)

Idea: "can all courses be finished" is exactly "does this directed
graph have a cycle" - if course A depends (transitively) on itself,
no valid order can ever satisfy every prerequisite. Cycle detection
on a *directed* graph needs 3 states per node, not the simple
visited/unvisited boolean that works for undirected graphs (as in
06): unvisited (0), currently-being-explored / "on the current DFS
path" (1), and fully-done (2). A cycle exists exactly when the DFS
reaches a node that's already in state 1 - a "back edge" to an
ancestor on the current path. Reaching a node in state 2 is fine
(it's a legitimately different path re-converging, not a cycle) and
should short-circuit as "no cycle found through here" without
re-exploring it.
"""


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj: dict[int, list[int]] = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        adj[course].append(prereq)

    UNVISITED, VISITING, DONE = 0, 1, 2
    state = [UNVISITED] * num_courses

    def has_cycle(node: int) -> bool:
        if state[node] == VISITING:
            return True
        if state[node] == DONE:
            return False

        state[node] = VISITING
        for neighbor in adj[node]:
            if has_cycle(neighbor):
                return True
        state[node] = DONE
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


if __name__ == "__main__":
    tests = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
        (3, [[0, 1], [1, 2], [2, 0]], False),
    ]

    for i, (num_courses, prereqs, expected) in enumerate(tests, 1):
        got = can_finish(num_courses, prereqs)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
