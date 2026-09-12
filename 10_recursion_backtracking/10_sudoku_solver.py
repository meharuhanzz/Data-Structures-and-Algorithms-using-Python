"""
Problem: Given a partially filled 9x9 Sudoku board ('.' for empty
cells), fill it in place so every row, column, and 3x3 box contains
the digits 1-9 exactly once.
Source : LeetCode 37 - Sudoku Solver

Example:
    Input:  a partially filled valid board
    Output: the board filled in, modified in place

Idea: the hardest problem in this folder, but structurally still the
same choose/explore/un-choose shape as every other one here - just
with a 2D grid and three simultaneous constraints instead of one.
Track which digits are already used in each row, column, and 3x3 box
with sets (same O(1)-conflict-check idea as 09's diagonal sets),
precomputed once from the board's initial filled cells. Recurse over
only the empty cells (found once up front, not re-scanned every
call): at each one, try every digit 1-9 not already conflicting in
that cell's row/column/box, place it, recurse to the next empty
cell, and undo the placement if no digit leads to a full solution.
Returning `True`/`False` from the recursion (instead of collecting
*all* solutions like 01-08) lets the search stop immediately once
one full solution is found, since Sudoku only asks for one.
"""


def solve_sudoku(board: list[list[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                empties.append((r, c))
            else:
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + c // 3].add(val)

    def backtrack(idx: int) -> bool:
        if idx == len(empties):
            return True

        r, c = empties[idx]
        b = (r // 3) * 3 + c // 3

        for digit in "123456789":
            if digit in rows[r] or digit in cols[c] or digit in boxes[b]:
                continue

            board[r][c] = digit
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[b].add(digit)

            if backtrack(idx + 1):
                return True

            board[r][c] = "."
            rows[r].remove(digit)
            cols[c].remove(digit)
            boxes[b].remove(digit)

        return False

    backtrack(0)


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    expected = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]

    solve_sudoku(board)
    status = "PASS" if board == expected else "FAIL"
    print(f"Test 1: {status}")
    if status == "FAIL":
        for row in board:
            print(row)
