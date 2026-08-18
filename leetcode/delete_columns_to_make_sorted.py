"""
You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid.
    - For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
        abc
        bce
        cae
You want to delete the columns that are not sorted lexicographically. In the above example
    (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1
    ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

Example 1:
    Input: strs = ["cba","daf","ghi"]
    Output: 1
    Explanation: The grid looks as follows:
      cba
      daf
      ghi
    Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

Example 2:
    Input: strs = ["a","b"]
    Output: 0
    Explanation: The grid looks as follows:
      a
      b
    Column 0 is the only column and is sorted, so you will not delete any columns.

Example 3:
    Input: strs = ["zyx","wvu","tsr"]
    Output: 3
    Explanation: The grid looks as follows:
      zyx
      wvu
      tsr
    All 3 columns are not sorted, so you will delete all 3.

Constraints:
    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 1000
    strs[i] consists of lowercase English letters.

A:
    strings of not the same size?
        all same length
    strings of length 0
        return 0
    strings of length 1
        return 0 or 1
    string with non lowercase char?
        only lowercase english
    one string in list
        return 0


D:
    strs = ["cba","daf","ghi"]

    col = 0
        c, d, g -> good
    col = 1
        b, a, h -> bad
    col = 2
        z, f, i -> good
    return total bad = 1
"""

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) < 2:
            return 0

        bad = 0
        for cindex in range(len(strs[0])):
            curr = strs[0][cindex]
            for s in strs[1:]:
                if s[cindex] < curr:
                    bad += 1
                    break
                curr = s[cindex]

        return bad


cases = [
    (["cba", "daf", "ghi"], 1),
    (["a", "b"], 0),
    (["zyx", "wvu", "tsr"], 3),
    (["abc"], 0),
]

sol = Solution()
for strs, exp in cases:
    assert (
        got := sol.minDeletionSize(strs)
    ) == exp, f"Failed case ({strs}) - expecting ({exp}), got ({got})."
