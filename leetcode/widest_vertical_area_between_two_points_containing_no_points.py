"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area
    between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e.,
    infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Example 1:
    Input: points = [[8,7],[9,9],[7,4],[9,7]]
    Output: 1
    Explanation: Both the red and the blue area are optimal.

Example 2:
    Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    Output: 3

Constraints:
    - n == points.length
    - 2 <= n <= 10**5
    - points[i].length == 2
    - 0 <= xi, yi <= 10**9

A:
    1 point?
        not possible
    2 points?
        degenerate case, return x2 - x1
    2 points same line,
        valid, return 0

D:
    Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    extract 3,9,1,1,5,8
    sort    1,1,3,5,8,9
    diff      0,2,2,3,1
    return max(diff) = 3
"""

from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        s = sorted([point[0] for point in points])
        return max([s[i] - s[i - 1] for i in range(1, len(s))])


sol = Solution()

cases = [
    ([[8, 7], [9, 9], [7, 4], [9, 7]], 1),
    ([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]], 3),
    ([[1, 1], [1, 2]], 0),
    ([[1, 1], [1, 1]], 0),
    ([[1, 0], [101, 4]], 100),
]

for points, exp in cases:
    assert (
        got := sol.maxWidthOfVerticalArea(points)
    ) == exp, f"Failed case ({points}) - expecting ({exp}), got ({got})"
