"""
Problem: Given people as pairs [h, k] - height h, and k = the number
of people in front of this person with height >= h - reconstruct and
return the queue (any order satisfying every pair's constraint).
Source : LeetCode 406 - Queue Reconstruction by Height

Example:
    Input:  [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Idea: the trickiest greedy in this folder because the two coordinates
pull in different directions and have to be untangled in the right
order. Sort by height *descending*, and for equal heights, by k
*ascending*. Then insert people one at a time, each at index k in the
result built so far. Why this works: processing tallest-first means
every person already placed is >= the current person's height, so
inserting the current person at position k automatically has exactly
k taller-or-equal people in front of them - insertion doesn't disturb
that count for people already placed, either, since inserting a
*shorter* person anywhere never counts toward any already-placed
taller person's own k requirement. This is the general lesson from
this greedy: when two constraints interact, look for an order to
process them in where satisfying one *doesn't retroactively break*
the other - here, tallest-first is exactly that order.
"""


def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    people = sorted(people, key=lambda p: (-p[0], p[1]))
    result: list[list[int]] = []
    for person in people:
        result.insert(person[1], person)
    return result


if __name__ == "__main__":
    tests = [
        ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
         [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
        ([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]],
         [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]),
    ]

    for i, (people, expected) in enumerate(tests, 1):
        got = reconstruct_queue(people)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
