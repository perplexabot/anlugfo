"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate
    of a point. Check if these points make a straight line in the XY plane.

Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true

Example 2:
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false

Constraints:
    - 2 <= coordinates.length <= 1000
    - coordinates[i].length == 2
    - -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    - coordinates contains no duplicate point.

A:
    what if one coor
        not possible
    what if two coor
        nothing interesting
"""

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = (
            (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
            if (coordinates[0][0] - coordinates[1][0])
            else None
        )
        for coor in coordinates[2:]:
            new_slope = (
                ((coordinates[0][1] - coor[1]) / (coordinates[0][0] - coor[0]))
                if (coordinates[0][0] - coor[0])
                else None
            )
            if new_slope != slope:
                return False
        return True


cases = [
    ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
    ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
    ([[1, 1], [10, 5]], True),
    ([[0, 0], [1, 1], [0, 3]], False),
]

sol = Solution()
for coor, exp in cases:
    assert (
        got := sol.checkStraightLine(coor)
    ) == exp, f"Failed case ({coor}) - expecting ({exp}), got ({got})."
