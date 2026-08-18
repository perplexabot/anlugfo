"""
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true
    if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:
    Input: points = [[1,1],[2,3],[3,2]]
    Output: true

Example 2:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: false

Constraints:
    - points.length == 3
    - points[i].length == 2
    - 0 <= xi, yi <= 100

A:
    less than 3 points, not possible
    more than 3 points, not possible

A:
    ?

D:
    get slope between point0 and point1
    get slope between point1 and point2
    compare
"""

from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return abs((points[0][0] * (points[1][1] - points[2][1])) + (points[1][0] * (points[2][1] - points[0][1])) + (points[2][0] * (points[0][1] - points[1][1]))) != 0


cases = [
    ([[1, 1], [2, 3], [3, 2]], True),
    ([[1, 1], [2, 2], [3, 3]], False),
    ([[0, 0], [1, 1], [1, 1]], False),
    ([[0, 0], [1, 2], [0, 1]], True),
]

sol = Solution()
for points, exp in cases:
    assert (
        got := sol.isBoomerang(points)
    ) == exp, f"Failed case ({points}) - expecting ({exp}), got ({got})."
