"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by
    rounding down the average of the cell and the eight surrounding cells (i.e., the average of
    the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not
    present, we do not consider it in the average (i.e., the average of the four cells in the red
    smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after
    applying the smoother on each cell of it.

Example 1:
    Input: img = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[0,0,0],[0,0,0],[0,0,0]]
    Explanation:
    For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
    For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
    For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:
    Input: img = [[100,200,100],[200,50,200],[100,200,100]]
    Output: [[137,141,137],[141,138,141],[137,141,137]]
    Explanation:
    For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
    For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6)
                                                    = floor(141.666667) = 141
    For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

Constraints:
    m == img.length
    n == img[i].length
    1 <= m, n <= 200
    0 <= img[i][j] <= 255

A:
    img = [] -> return []
    img = [[]] -> return [[]]
    img = [x] -> assuming not possible
    img = [[x]] -> return [[x]]
    m != n -> possible
    [[1,2,3]] -> [[floor(3/2), floor(6/3), floor(5/2)]]

D:
    Input: img = [[100,200,100],
                  [200,50,200],
                  [100,200,100]]

    (0,0) -> floor(550/4)
    (0,1) -> floor(850/6)
    (0,2) -> floor(550/4)
    (1,0) -> floor(850/6)
    (1,1) -> floor(1250/9)
    (1,2) -> floor(850/6)
    (2,0) -> floor(550/4)
    (2,1) -> floor(850/6)
    (2,2) -> floor(550/4)

    return [[137,141,137],[141,138,141],[137,141,137]

    x = 0, y = 0:
        elems:
            (x-1,y-1)
            (x-1,y+1)
            (x-1,y)
            (x+1,y+1)
            (x+1,y-1)
            (x+1,y)
            (x,y-1)
            (x,y+1)
            (x,y)
"""

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        new = []
        for i in range(m):
            new.append([])
            for j in range(n):
                cells = [
                    (i - 1, j - 1),
                    (i - 1, j + 1),
                    (i - 1, j),
                    (i + 1, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                    (i, j),
                ]
                cells = [x for x in cells if x[0] >= 0 and x[0] < m and x[1] >= 0 and x[1] < n]
                new[i].append(sum(img[x[0]][x[1]] for x in cells) // len(cells))
        return new


cases = [
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    (
        [[100, 200, 100], [200, 50, 200], [100, 200, 100]],
        [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
    ),
    ([[1, 2, 3]], [[1, 2, 2]]),
    ([[1]], [[1]]),
    ([[11]], [[11]]),
]

sol = Solution()
for (img, exp) in cases:
    assert (
        got := sol.imageSmoother(img)
    ) == exp, f"Failed case ({img}) - expecting ({exp}), got ({got})."
