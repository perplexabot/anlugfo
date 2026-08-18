"""
You are given an array of distinct integers arr and an array of integer arrays pieces, where the
    integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces
    in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:
    Input: arr = [15,88], pieces = [[88],[15]]
    Output: true
    Explanation: Concatenate [15] then [88]

Example 2:
    Input: arr = [49,18,16], pieces = [[16,18,49]]
    Output: false
    Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 3:
    Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
    Output: true
    Explanation: Concatenate [91] then [4,64] then [78]

Constraints:
    - 1 <= pieces.length <= arr.length <= 100
    - sum(pieces[i].length) == arr.length
    - 1 <= pieces[i].length <= arr.length
    - 1 <= arr[i], pieces[i][j] <= 100
    - The integers in arr are distinct.
    - The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the
        integers in this array are distinct).

A:
    non unique:
        not possible
    both empty:
        return true
    one empty:
        return false

A:
    ?
D:
    Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
    91, yes [91]
    4, yes [4,64]
    78, yes [78]
    return True
P:
    final = []
    for a in arr:
        for p in pieces:
            if p[0] == a:
                final.extend(p)
    return final == arr
"""

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        final = []
        for a in arr:
            for p in pieces:
                if p[0] == a:
                    final.extend(p)
        return final == arr


cases = [
    ([15, 88], [[88], [15]], True),
    ([49, 18, 16], [[16, 18, 49]], False),
    ([91, 4, 64, 78], [[78], [4, 64], [91]], True),
    ([1, 2, 3], [[3], [2], [1]], True),
    ([1, 2, 3], [[1], [2], [3]], True),
    ([1, 2, 3], [[2], [1], [3]], True),
    ([1, 2, 3], [[2, 1], [3]], False),
    ([1, 2, 3], [[1, 2], [3]], True),
    ([1, 2, 3], [[1], [3]], False),
]

sol = Solution()
for arr, pieces, exp in cases:
    assert (
        got := sol.canFormArray(arr, pieces)
    ) == exp, f"Failed case ({arr}, {pieces}) - expecting ({exp}), got ({got})."
