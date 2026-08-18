"""
A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
    - <col> denotes the column number c of the cell. It is represented by alphabetical letters.
        - For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
    - <row> is the row number r of the cell. The rth row is represented by the integer r.

You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the
    column c1, <row1> represents the row r1, <col2> represents the column c2, and <row2>
    represents the row r2, such that r1 <= r2 and c1 <= c2.

Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be
    represented as strings in the format mentioned above and be sorted in non-decreasing order
    first by columns and then by rows.

Example 1:
    Input: s = "K1:L2"
    Output: ["K1","K2","L1","L2"]
    Explanation:
    The above diagram shows the cells which should be present in the list.
    The red arrows denote the order in which the cells should be presented.

Example 2:
    Input: s = "A1:F1"
    Output: ["A1","B1","C1","D1","E1","F1"]
    Explanation:
    The above diagram shows the cells which should be present in the list.
    The red arrow denotes the order in which the cells should be presented.

Constraints:
    s.length == 5
    'A' <= s[0] <= s[3] <= 'Z'
    '1' <= s[1] <= s[4] <= '9'
    s consists of uppercase English letters, digits and ':'.

A:
    cell0 == cell1?
        return cell0
    col0 == col1:
        iterate row only
    row0 == row1:
        iterate col only
    cell0 "greater than" cell1:
        find maxes and mins

A:
    ?

D:
    cells = []
    c0, r0 = cell0.split(':')
    c1, r1 = cell1.split(':')

    minc = min(c0,c1)
    ...

    for i in ascii_lowercase[ord(minc) - 96: ord(maxc) - 96 + 1]:
        for j in range(minr, maxr+1):
            cells.append(f"{i}{j}")
    return cells
"""

from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        from string import ascii_uppercase

        if not s:
            return []

        cells = []
        cell0, cell1 = s.split(':')
        col0, row0 = cell0
        col1, row1 = cell1
        mincol = min(col0, col1)
        maxcol = max(col0, col1)
        minrow = int(min(row0, row1))
        maxrow = int(max(row0, row1))

        for letter in ascii_uppercase[ord(mincol) - 65 : ord(maxcol) - 64]:
            for number in range(minrow, maxrow + 1):
                cells.append(f"{letter}{number}")

        return cells


cases = [
    ("K1:L2", ["K1", "K2", "L1", "L2"]),
    ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
    ("A1:A1", ["A1"]),
    ("F1:A1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
    ("", []),
    ("A1:A5", ["A1", "A2", "A3", "A4", "A5"]),
    ("A1:C1", ["A1", "B1", "C1"]),
]

sol = Solution()
for s, exp in cases:
    assert (
        got := sol.cellsInRange(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
