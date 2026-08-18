"""
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

    - maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered
        around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

Example 1:
    Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    Output: [[9,9],[8,6]]
    Explanation: The diagram above shows the original matrix and the generated matrix.
    Notice that each value in the generated matrix corresponds to the largest value of a
        contiguous 3 x 3 matrix in grid.

Example 2:
    Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    Output: [[2,2,2],[2,2,2],[2,2,2]]
    Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.

Constraints:
    - n == grid.length == grid[i].length
    - 3 <= n <= 100
    - 1 <= grid[i][j] <= 100

A:
    Always able to get at least 1 3x3?
        yes
    nxn?
        yes
    none negatives
        yes, positive actually

D:
    Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    len(grid) = 4x4

    iterate with:
        x goes from 1 to len(grid) - 2
        y goes from 1 to len(grid) - 2

    at each point:
        check above: (x - 1,y)
        check below: (x + 1,y)
        check left: (x,y - 1)
        check right: (x,y + 1)
        check topleft: (x-1,y-1)
        check topright: (x-1,y+1)
        check bottomleft: (x+1,y-1)
        check bottomright: (x+1,y+1)
"""

from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        final = []
        for x in range(1, len(grid) - 1):
            tmp = []
            for y in range(1, len(grid) - 1):
                tmp.append(
                    max(
                        grid[x][y],
                        grid[x - 1][y],
                        grid[x + 1][y],
                        grid[x][y - 1],
                        grid[x][y + 1],
                        grid[x - 1][y - 1],
                        grid[x - 1][y + 1],
                        grid[x + 1][y - 1],
                        grid[x + 1][y + 1],
                    )
                )
            final.append(tmp)
        return final


sol = Solution()

cases = [
    ([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]], [[9, 9], [8, 6]]),
    (
        [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
    ),
    ([[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]], [[9, 9], [9, 9]]),
]

for case, exp in cases:
    assert (
        got := sol.largestLocal(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
