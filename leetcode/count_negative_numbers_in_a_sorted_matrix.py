"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
    return the number of negative numbers in grid.

Example 1:
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.

Example 2:
    Input: grid = [[3,2],[1,0]]
    Output: 0

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 100
    - -100 <= grid[i][j] <= 100

A:
    matrix of size [] or [[]]
        not possible
    matrix of size 1x1
        possible
"""

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for row in grid[::-1]:
            if row[-1] > -1:
                break

            for elem in row[::-1]:
                if elem > -1:
                    break
                total += 1
        return total


cases = [
    ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8),
    ([[3, 2], [1, 0]], 0),
    ([[1]], 0),
    ([[0]], 0),
    ([[-1]], 1),
    ([[-1, -1]], 2),
    ([[-1], [-1]], 2),
    ([[0], [-1]], 1),
    ([[0], [0]], 0),
    ([[10], [3]], 0),
    ([[2, 3]], 0),
    ([[2, -1]], 1),
    ([[2, -1], [1, -2], [-1, -3]], 4),
]

sol = Solution()
for grid, exp in cases:
    assert (
        got := sol.countNegatives(grid)
    ) == exp, f"Failed case ({grid}) - expecting ({exp}), got ({got})."
