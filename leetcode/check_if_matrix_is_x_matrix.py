"""
A square matrix is said to be an X-Matrix if both of the following conditions hold:
    - All the elements in the diagonals of the matrix are non-zero.
    - All other elements are 0.

Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is
    an X-Matrix. Otherwise, return false.

Example 1:
    Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
    Output: true
    Explanation: Refer to the diagram above.
    An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
    Thus, grid is an X-Matrix.

Example 2:
    Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
    Output: false
    Explanation: Refer to the diagram above.
    An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
    Thus, grid is not an X-Matrix.

Constraints:
    n == grid.length == grid[i].length
    3 <= n <= 100
    0 <= grid[i][j] <= 105

A:
    non square matrix -> not possible
    matrix with None elem -> not possible
    matrix of size 1x1 -> return true
    [[]] vs [] -> return true either way
    n is even vs n is odd

D:
    Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]

    diag 0
        i = 0, row = [2,0,0,1]
            row[i] != 0, good
        i = 1, row = [0,3,1,0]
            row[i] != 0, good
        i = 2, row = [0,5,2,0]
            row[i] != 0, good
        i = 3, row = [4,0,0,2]
            row[i] != 0, good

    diag 1
        i = len(row) - 1  = 3, row = [2,0,0,1]
            row[i] != 0, good
        i = 2, row = [0,3,1,0]
            row[i] != 0, good
        i = 1, row = [0,5,2,0]
            row[i] != 0, good
        i = 0, row = [4,0,0,2]
            row[i] != 0, good

    nonediag
        i = 0, row = [2,0,0,1]
            row[i+1:len(row) - i - 1] == 0, good
        i = 1, row = [0,3,1,0]
            row[i+1:len(row) - i - 1] == 0, good
        i = 2, row = [0,5,2,0]
            row[i+1:len(row) - i - 1] == 0, good
        i = 3, row = [4,0,0,2]
            row[i+1:len(row) - i - 1] == 0, good
"""

from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        if not grid or not grid[0]:
            return True

        for row_ind, row in enumerate(grid):
            diag_ind0 = row_ind
            diag_ind1 = len(row) - row_ind - 1
            for col_ind, elem in enumerate(row):
                if col_ind == diag_ind0 or col_ind == diag_ind1:
                    if elem == 0:
                        return False
                else:
                    if elem != 0:
                        return False
        return True


cases = [
    ([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]], True),
    ([[5, 7, 0], [0, 3, 1], [0, 5, 0]], False),
]

sol = Solution()
for (grid, exp) in cases:
    assert (
        got := sol.checkXMatrix(grid)
    ) == exp, f"Failed case ({grid}) - expecting ({exp}), got ({got})."
