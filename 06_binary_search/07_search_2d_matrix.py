"""
Problem: Given an m x n matrix where each row is sorted ascending and
the first element of each row is greater than the last element of
the previous row (so the whole matrix is sorted if read row by row),
determine if target exists. O(log(m*n)).
Source : LeetCode 74 - Search a 2D Matrix

Example:
    Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            target = 3
    Output: True

Idea: the matrix's row-major layout means it's really just a sorted
1D array in disguise. Run 01's plain binary search over virtual
indices 0..(rows*cols - 1), converting each virtual index back to
(row, col) with divmod (`mid // cols`, `mid % cols`). No need to
first binary-search for the row and then the column separately - one
search over the flattened index space is simpler and still O(log(mn)).
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    tests = [
        (matrix, 3, True),
        (matrix, 13, False),
        ([[1]], 1, True),
        ([[1]], 2, False),
    ]

    for i, (m, target, expected) in enumerate(tests, 1):
        got = search_matrix(m, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
