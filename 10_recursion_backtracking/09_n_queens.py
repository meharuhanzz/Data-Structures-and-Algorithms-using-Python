"""
Problem: Place n queens on an n x n chessboard so that no two queens
attack each other (no shared row, column, or diagonal). Return all
distinct solutions, each as a list of strings representing the board.
Source : LeetCode 51 - N-Queens

Example:
    Input:  n = 4
    Output: [
      [".Q..", "...Q", "Q...", "..Q."],
      ["..Q.", "Q...", "...Q", ".Q.."],
    ]

Idea: place one queen per row (so row conflicts are structurally
impossible - `placement[r]` is the column of the queen in row r,
never two queens sharing a row by construction), and use three sets
to track which columns and diagonals are already under attack:
`cols`, plus `diag1` for "/"-diagonals (constant `r - c`) and `diag2`
for "\"-diagonals (constant `r + c`) - every cell on the same
diagonal shares one of these two values, which is what makes O(1)
diagonal-conflict checks possible instead of scanning the board.
Trying every column at each row, skipping any that conflict, and
un-marking all three sets on backtrack is the same choose/explore/
un-choose shape as every earlier problem, just with a richer
constraint check.
"""


def solve_n_queens(n: int) -> list[list[str]]:
    result = []
    cols: set[int] = set()
    diag1: set[int] = set()  # r - c, constant along "/" diagonals
    diag2: set[int] = set()  # r + c, constant along "\" diagonals
    placement: list[int] = []

    def backtrack(row: int) -> None:
        if row == n:
            board = ["." * c + "Q" + "." * (n - c - 1) for c in placement]
            result.append(board)
            return
        for c in range(n):
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue
            cols.add(c)
            diag1.add(row - c)
            diag2.add(row + c)
            placement.append(c)

            backtrack(row + 1)

            placement.pop()
            cols.remove(c)
            diag1.remove(row - c)
            diag2.remove(row + c)

    backtrack(0)
    return result


if __name__ == "__main__":
    tests = [
        (4, 2),
        (1, 1),
        (2, 0),
        (8, 92),
    ]

    for i, (n, expected_count) in enumerate(tests, 1):
        got = solve_n_queens(n)
        status = "PASS" if len(got) == expected_count else "FAIL"
        print(f"Test {i}: {status} (n={n}, got {len(got)} solutions, expected {expected_count})")
