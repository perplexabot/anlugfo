"""
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j]
    represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other,
    forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.

Example 1:
    Input: grid = [[1,2],[3,4]]
    Output: 34

Example 2:
    Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
    Output: 32

Example 3:
    Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
    Output: 46

Constraints:
    - n == grid.length == grid[i].length
    - 1 <= n <= 50
    - 0 <= grid[i][j] <= 50

A:
    n = 0?
        no
    what is the def of surface area for a cell?
        assuming 1 surface = 1 surface area unit
    does top and bottom surface area count if v = 0 (is the surface area 0 or 1?)?
        v = 0 means 0 surface area

D:
       0 1
       ---
    0| 1 2
    1| 3 4

    // always has top and bottom, all the sides need to be checked before adding
    // some cells don't have 4 adjacent
    surface area of (0,0)
        first level = 2
        top bottom = 2
    surface area of (0,1)
        first level = 2
        second level = 3
        top bottom = 2
    surface area of (1,0)
        first level = 2
        second level = 3
        third level = 3
        top and bottom = 2
    surface area of (1,1)
        first level = 2
        second level = 2
        third level = 3
        forth level = 4
        top and bottom = 2
    total = sum of above
    ...


P:
    if N == 1
        return easy surface area
    if N == 2
        do corners
    if n == 3
        do corners
            grid[0][0]
            grid[0][-1]
            grid[-1][0]
            grid[-1][-1]
        do sides
            grid[0][1:-1]
            grid[-1][1:-1]
            grid[1:-1][0]
            grid[1:-1][-1]
        do middles
            grid[1:-1][1:i-1]

"""


class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        N = len(grid)
        if N == 1:
            return 2 + (grid[0][0] * 4) if grid[0][0] else 0

        tl = 0
        if grid[0][0]:
            tl = 2 + (grid[0][0] * 2)
            if grid[0][0] > grid[0][1]:
                tl += grid[0][0] - grid[0][1]
            if grid[0][0] > grid[1][0]:
                tl += grid[0][0] - grid[1][0]

        tr = 0
        if grid[0][-1]:
            tr = 2 + (grid[0][-1] * 2)
            if grid[0][-1] > grid[0][-2]:
                tr += grid[0][-1] - grid[0][-2]
            if grid[0][-1] > grid[1][-1]:
                tr += grid[0][-1] - grid[1][-1]

        bl = 0
        if grid[-1][0]:
            bl = 2 + (grid[-1][0] * 2)
            if grid[-1][0] > grid[-2][0]:
                bl += grid[-1][0] - grid[-2][0]
            if grid[-1][0] > grid[-1][1]:
                bl += grid[-1][0] - grid[-1][1]

        br = 0
        if grid[-1][-1]:
            br = 2 + (grid[-1][-1] * 2)
            if grid[-1][-1] > grid[-2][-1]:
                br += grid[-1][-1] - grid[-2][-1]
            if grid[-1][-1] > grid[-1][-2]:
                br += grid[-1][-1] - grid[-1][-2]

        if N == 2:
            return tl + tr + bl + br

        topRow = 0
        for i in range(1, len(grid) - 1):
            if grid[0][i]:
                left = grid[0][i] - grid[0][i - 1] if grid[0][i - 1] < grid[0][i] else 0
                right = grid[0][i] - grid[0][i + 1] if grid[0][i + 1] < grid[0][i] else 0
                down = grid[0][i] - grid[1][i] if grid[1][i] < grid[0][i] else 0
                up = grid[0][i]
                topRow += 2 + up + right + down + left  # 2 to account for above and below

        leftRow = 0
        for i in range(1, len(grid) - 1):
            if grid[i][0]:
                up = grid[i][0] - grid[i - 1][0] if grid[i - 1][0] < grid[i][0] else 0
                down = grid[i][0] - grid[i + 1][0] if grid[i + 1][0] < grid[i][0] else 0
                right = grid[i][0] - grid[i][1] if grid[i][1] < grid[i][0] else 0
                left = grid[i][0]
                leftRow += 2 + up + right + down + left

        rightRow = 0
        for i in range(1, len(grid) - 1):
            if grid[i][-1]:
                up = grid[i][-1] - grid[i - 1][-1] if grid[i - 1][-1] < grid[i][-1] else 0
                down = grid[i][-1] - grid[i + 1][-1] if grid[i + 1][-1] < grid[i][-1] else 0
                left = grid[i][-1] - grid[i][-2] if grid[i][-2] < grid[i][-1] else 0
                right = grid[i][-1]
                rightRow += 2 + up + right + down + left

        bottomRow = 0
        for i in range(1, len(grid) - 1):
            if grid[-1][i]:
                left = grid[-1][i] - grid[-1][i - 1] if grid[-1][i - 1] < grid[-1][i] else 0
                right = grid[-1][i] - grid[-1][i + 1] if grid[-1][i + 1] < grid[-1][i] else 0
                up = grid[-1][i] - grid[-2][i] if grid[-2][i] < grid[-1][i] else 0
                down = grid[-1][i]
                bottomRow += 2 + up + right + down + left

        middle = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                if grid[i][j]:
                    up = grid[i][j] - grid[i - 1][j] if grid[i][j] > grid[i - 1][j] else 0
                    dn = grid[i][j] - grid[i + 1][j] if grid[i][j] > grid[i + 1][j] else 0
                    lf = grid[i][j] - grid[i][j - 1] if grid[i][j] > grid[i][j - 1] else 0
                    rt = grid[i][j] - grid[i][j + 1] if grid[i][j] > grid[i][j + 1] else 0
                    middle += up + dn + lf + rt + 2
        return tl + tr + bl + br + topRow + leftRow + rightRow + bottomRow + middle


cases = [
    ([[1, 2], [3, 4]], 34),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 32),
    ([[2, 1, 1], [1, 0, 1], [1, 1, 1]], 36),
    ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 46),
    ([[5]], 2 + (5 * 4)),
    ([[1]], 6),
    ([[0]], 0),
    ([[0, 0], [0, 0]], 0),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 6),
    ([[0, 1, 0], [0, 0, 0], [0, 0, 0]], 6),
    ([[0, 0, 0], [0, 0, 0], [0, 1, 0]], 6),
    ([[0, 0, 0], [1, 0, 0], [0, 0, 0]], 6),
    ([[0, 0, 0], [0, 0, 1], [0, 0, 0]], 6),
    ([[2, 2], [2, 2]], 24),
    ([[2, 2, 2], [2, 0, 2], [2, 2, 2]], 48),
    ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 48),
    ([[5, 4, 1, 0], [1, 0, 2, 0], [3, 1, 4, 2], [3, 1, 2, 5]], 110),
]

sol = Solution()

for case, expected in cases:
    assert (
        got := sol.surfaceArea(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
