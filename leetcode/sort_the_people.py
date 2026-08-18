"""
You are given an array of strings names, and an array heights that consists of distinct positive
    integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Example 1:
    Input: names = ["Mary","John","Emma"], heights = [180,165,170]
    Output: ["Mary","Emma","John"]
    Explanation: Mary is the tallest, followed by Emma and John.

Example 2:
    Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
    Output: ["Bob","Alice","Bob"]
    Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Constraints:
    n == names.length == heights.length
    1 <= n <= 103
    1 <= names[i].length <= 20
    1 <= heights[i] <= 10**5
    names[i] consists of lower and upper case English letters.
    All the values of heights are distinct.

A:
    len(heights) <= 1 -> return names as is
    len(heights) != len(names) -> not possible
    heights all positive (true)
    name in list twice -> just continue as is
    names with same hieghts -> not possible

D:
    sort by height
"""

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        person_and_height = list(zip(names, heights))
        person_and_height.sort(key=lambda x: x[1], reverse=True)
        return [x for x, y in person_and_height]


cases = [
    (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
    (["Alice", "Bob", "Bob"], [155, 185, 150], ["Bob", "Alice", "Bob"]),
    (["Alice"], [120], ["Alice"]),
    (["Alice", "Bob"], [180, 120], ["Alice", "Bob"]),
    (["Alice", "Bob"], [120, 180], ["Bob", "Alice"]),
]

sol = Solution()
for (names, heights, exp) in cases:
    assert (
        got := sol.sortPeople(names, heights)
    ) == exp, f"Failed case ({names}, {heights}) - expecting ({exp}),  got ({got})."
