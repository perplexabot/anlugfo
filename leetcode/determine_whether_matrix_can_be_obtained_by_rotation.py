"""
Given two n x n binary matrices mat and target, return true if it is possible
    to make mat equal to target by rotating mat in 90-degree increments, or
    false otherwise.

Example 1:
    Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
    Output: true
    Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
    Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
    Output: false
    Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
    Output: true
    Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

Constraints:
    - n == mat.length == target.length
    - n == mat[i].length == target[i].length
    - 1 <= n <= 10
    - mat[i][j] and target[i][j] are either 0 or 1.
"""

from typing import List


class Solution:

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        def rot(a):
            return [list(x[::-1]) for x in list(zip(*a))]

        curr = mat
        for i in range(3):
            if (r := rot(curr)) == target:
                return True
            curr = r
        return False


cases = [
    ([[0, 1], [1, 0]], [[1, 0], [0, 1]], True),
    ([[0, 1], [1, 1]], [[1, 0], [0, 1]], False),
    ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]], True),
]

sol = Solution()
for matrix, target, exp in cases:
    assert (
        got := sol.findRotation(matrix, target)
    ) == exp, f"Failed case ({matrix}, {target}) - expecting ({exp}), got ({got})."
