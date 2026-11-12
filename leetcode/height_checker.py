"""
A school is trying to take an annual photo of all the students. The students are asked to stand in a
    single file line in non-decreasing order by height. Let this ordering be represented by the
    integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing
    in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Example 1:
    Input: heights = [1,1,4,2,1,3]
    Output: 3
    Explanation:
    heights:  [1,1,4,2,1,3]
    expected: [1,1,1,2,3,4]
    Indices 2, 4, and 5 do not match.

Example 2:
    Input: heights = [5,1,2,3,4]
    Output: 5
    Explanation:
    heights:  [5,1,2,3,4]
    expected: [1,2,3,4,5]
    All indices do not match.

Example 3:
    Input: heights = [1,2,3,4,5]
    Output: 0
    Explanation:
    heights:  [1,2,3,4,5]
    expected: [1,2,3,4,5]
    All indices match.

Constraints:
    - 1 <= heights.length <= 100
    - 1 <= heights[i] <= 100


A:
    height size 1
        return 0
    height size 0
        not possible
    none positive heights
        no
    same heights
        yes

D:
    Input: heights = [5,1,2,3,4]
    sort(heights0 =  [1,2,3,4,5]
                      x x x x x

P:
    sort(heights)
    loop and compare
    return diff

O:
    time comp: O(nlogn) + O(n) = O(nlogn)
    spac comp: using extra array for sorted, so O(n)

    anyway to reduce nlogn? we would have to figure out wrong spots without sorting...
    anyway to remove O(n) space?

    could do initial O(n) iteration to check good case, if not start sorting and counting

T:
    [1,1,4,2,1,3],3
    [5,1,2,3,4],5
    [1,2,3,4,5],0
    [1], 0
    [2], 0
    [1,2],0
    [2,1],2
"""


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        if len(heights) < 2:
            return 0

        broken = False
        for i in range(len(heights) - 1):
            if heights[i] > heights[i + 1]:
                broken = True

        if not broken:
            return 0

        return sum(1 for a, b in zip(heights, sorted(heights)) if a != b)


cases = [
    ([1, 1, 4, 2, 1, 3], 3),
    ([5, 1, 2, 3, 4], 5),
    ([1, 2, 3, 4, 5], 0),
    ([1], 0),
    ([2], 0),
    ([1, 2], 0),
    ([2, 1], 2),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.heightChecker(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
