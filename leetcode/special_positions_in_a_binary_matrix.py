"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and
    column j are 0 (rows and columns are 0-indexed).

Example 1:
    Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
    Output: 1
    Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row
        1 and column 2 are 0.

Example 2:
    Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
    Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

Constraints:
    - m == mat.length
    - n == mat[i].length
    - 1 <= m, n <= 100
    - mat[i][j] is either 0 or 1.

AADPOCT
A
    non sym matrix
        yup
    matrix of size 1
        yee
    matrix of size 0
        nope
    none 0 or 1?
        nope
"""

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        yeee = 0
        for li in range(len(mat)):
            if mat[li].count(1) == 1:
                if [mat[i][mat[li].index(1)] for i in range(len(mat))].count(1) == 1:
                    yeee += 1
        return yeee


sol = Solution()

cases = [
    ([[1, 0, 0], [0, 0, 1], [1, 0, 0]], 1),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ([[1]], 1),
    ([[1, 0]], 1),
    ([[1, 1]], 0),
    ([[0, 0]], 0),
    ([[1], [0], [0]], 1),
    ([[1], [0], [1]], 0),
    ([[0], [0], [0]], 0),
]

for mat, exp in cases:
    assert (
        got := sol.numSpecial(mat)
    ) == exp, f"Failed case ({mat}) - expecting ({exp}), got ({got})."
