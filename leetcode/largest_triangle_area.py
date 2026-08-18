"""
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the
    largest triangle that can be formed by any three different points. Answers within 10-5 of the
    actual answer will be accepted.

Example 1:
    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2.00000
    Explanation: The five points are shown in the above figure. The red triangle is the largest.

Example 2:
    Input: points = [[1,0],[0,0],[0,1]]
    Output: 0.50000

Constraints:
    - 3 <= points.length <= 50
    - -50 <= xi, yi <= 50
    - All the given points are unique.

A:
    points size less than 3, not possible
    same points exist, not possible
    negatives possible
A:
    ?
D:
    get all trios
        keep track of max
"""

from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        from itertools import combinations

        max_size = float('-inf')
        for A, B, C in combinations(points, 3):
            max_size = max(
                max_size,
                0.5 * abs(((A[0] - C[0]) * (B[1] - A[1])) - ((A[0] - B[0]) * (C[1] - A[1]))),
            )
        return max_size


sol = Solution()
cases = [([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2.00000), ([[1, 0], [0, 0], [0, 1]], 0.50000)]

for points, exp in cases:
    assert (
        got := sol.largestTriangleArea(points)
    ) == exp, f"Failed case ({points}) - expecting ({exp}), got ({got})."
