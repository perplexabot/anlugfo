"""
You are given an m x n 2D array grid of positive integers.
Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.
Zigzag pattern traversal is defined as following the below actions:
    - Start at the top-left cell (0, 0).
    - Move right within a row until the end of the row is reached.
    - Drop down to the next row, then traverse left until the beginning of the row is reached.
    - Continue alternating between right and left traversal until every row has been traversed.
Note that you must skip every alternate cell during the traversal.
Return an array of integers result containing, in order, the value of the cells visited during the
    zigzag traversal with skips.

Example 1:
    Input: grid = [[1,2],[3,4]]
    Output: [1,4]

Example 2:
    Input: grid = [[2,1],[2,1],[2,1]]
    Output: [2,1,2]

Example 3:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,3,5,7,9]

Constraints:
    - 2 <= n == grid.length <= 50
    - 2 <= m == grid[i].length <= 50
    - 1 <= grid[i][j] <= 2500

A:
    can m x n be 1x1?
        no, smallest is 2x2 - no column only or row only

D:
    m and n are even:
        1  2  3  4
        5  6  7  8
        9  10 11 12

        1 3
        8 6
        9 11

        next line has offset by 0

    m and n are odd
        1 2 3
        4 5 6
        7 8 9

        1 3
        5
        7 9

        next line has offset by 1 and 0 (alternating)

    n is odd m is even
        1  2  3
        4  5  6
        7  8  9
        10 11 12

        1 3
        5
        7 9
        11

        next line has offset by 1 and 0 (alternating)

P:
    ret = []
    if m or n is odd
        offset = 1
        for row in grid:
            offset = 1 - offset
            if offset:
                for e in reversed(row[offset::2]):
                    ret.append(e)
            else:
                for e in row[::2]:
                    ret.append(e)

    else
        for row in grid:
            offset = 1
            if offset:
                for e in reversed(row[::2]):
                    ret.append(e)
            else
                for e in row[::2]:
                    ret.append(e)

O:
    time complexity: O(n) since reversed is O(1) in time
    spac complexity: O(n) for ret list, reversed is O(1) in spac

T:
    ([[1,2],[3,4]], [1,4]),
    ([[2,1],[2,1],[2,1]], [2,1,2]),
    ([[1,2,3],[4,5,6],[7,8,9]], [1,3,5,7,9]),
    [[1 ,2 ,3],
    [4 ,5 ,6],       -->  [1,3,5,7,9,11]
    [7 ,8 ,9],
    [10,11,12]]

    [[1, 2 ,3 ,4],
    [5, 6 ,7 ,8],   --> [1,3,8,6,9,11]
    [9, 10,11,12]]
"""

from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ret = []
        offset = 1
        for row in grid:
            offset = 1 - offset
            if offset:
                for e in reversed(row[offset::2]):
                    ret.append(e)
            else:
                for e in row[::2]:
                    ret.append(e)
        return ret


cases = [
    ([[1, 2], [3, 4]], [1, 4]),
    ([[2, 1], [2, 1], [2, 1]], [2, 1, 2]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 3, 5, 7, 9]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], [1, 3, 5, 7, 9, 11]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 3, 8, 6, 9, 11]),
]

sol = Solution()

for grid, expected in cases:
    assert (
        got := sol.zigzagTraversal(grid)
    ) == expected, f"Failed case ({grid}) - expecting ({expected}), got ({got})."
