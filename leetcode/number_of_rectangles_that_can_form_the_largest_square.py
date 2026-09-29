"""
You are given an array rectangles where rectangles[i] = [li, wi] represents the
    ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi.
    For example, if you have a rectangle [4,6], you can cut it to get a square with a side length
    of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.

Example 1:
    Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
    Output: 3
    Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
    The largest possible square is of length 5, and you can get it out of 3 rectangles.

Example 2:
    Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
    Output: 3

Constraints:
    - 1 <= rectangles.length <= 1000
    - rectangles[i].length == 2
    - 1 <= li, wi <= 10**9
    - li != wi

A:
    no rectangles:
        not possible
    rectangle with negative lengths/widths
        not possible
    recrangle with missing length/width
        not possible
    recrangle with length/width of 0
        not possible
    recrangle with length == width
        who cares

A:
    ?

D:
    Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
    2, 3, 3, 3
    three 3s so return 3

P:
    best = float(-inf)
    total = 0
    for rec in recs:
        s = min(rec)
        if s == best:
            total += 1

        if s > best:
            total = 1
            best = s

O:
    do in one pass, no extra list

T:

    [[5,8],[3,9],[5,12],[16,5]], 3
    [[2,3],[3,7],[4,3],[3,7]], 3
    [[1,1],[1,1]], 2
    [[100,2]], 1
    [[100,1], [100,1]], 2
    [[100,2], [100,1]], 1
    [[100,2], [100,1], [100,2]], 2
"""

from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        total = 0
        best = float('-inf')
        for rect in rectangles:
            s = min(rect)
            if s == best:
                total += 1
            elif s > best:
                best = s
                total = 1
        return total


cases = [
    ([[5, 8], [3, 9], [5, 12], [16, 5]], 3),
    ([[2, 3], [3, 7], [4, 3], [3, 7]], 3),
    ([[1, 1], [1, 1]], 2),
    ([[100, 2]], 1),
    ([[100, 1], [100, 1]], 2),
    ([[100, 2], [100, 1]], 1),
    ([[100, 2], [100, 1], [100, 2]], 2),
]

sol = Solution()
for rects, expected in cases:
    assert (
        got := sol.countGoodRectangles(rects)
    ) == expected, f"Woops, failed case ({rects}) - expecting ({expected}), got ({got})."
