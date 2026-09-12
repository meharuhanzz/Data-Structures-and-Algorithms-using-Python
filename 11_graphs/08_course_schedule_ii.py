"""
Problem: Same setup as 07, but return a valid order to take all
courses in, or [] if no valid order exists (a cycle).
Source : LeetCode 210 - Course Schedule II

Example:
    Input:  num_courses = 4,
            prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0, 1, 2, 3]  (or [0, 2, 1, 3] - either is valid)

Idea: Kahn's algorithm - topological sort via BFS instead of DFS,
built on in-degree (how many prerequisites a course still has left
unmet) rather than the 3-state coloring from 07. Any course with
in-degree 0 has no unmet prerequisites, so it's safe to take right
now - seed the queue with all such courses. Taking a course
conceptually removes it from the graph, which is simulated by
decrementing the in-degree of everything it was a prerequisite for;
any neighbor whose in-degree drops to 0 as a result becomes takeable
and joins the queue. If every course gets processed this way, the
order they were dequeued in is a valid topological order; if some
courses are left with in-degree > 0 at the end, they're stuck in a
cycle with each other and no valid order exists.
"""

from collections import deque


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    adj: dict[int, list[int]] = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []


def _is_valid_order(order, num_courses, prerequisites):
    if len(order) != num_courses:
        return False
    position = {course: i for i, course in enumerate(order)}
    return all(position[prereq] < position[course] for course, prereq in prerequisites)


if __name__ == "__main__":
    tests = [
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
        (2, [[1, 0], [0, 1]], False),
        (1, [], True),
    ]

    for i, (num_courses, prereqs, should_have_valid_order) in enumerate(tests, 1):
        got = find_order(num_courses, prereqs)
        if should_have_valid_order:
            status = "PASS" if _is_valid_order(got, num_courses, prereqs) else "FAIL"
        else:
            status = "PASS" if got == [] else "FAIL"
        print(f"Test {i}: {status} (got {got})")
