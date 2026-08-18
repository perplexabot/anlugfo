"""
You're given strings jewels representing the types of stones that are jewels, and stones
    representing the stones you have. Each character in stones is a type of stone you have. You
    want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3

Example 2:
    Input: jewels = "z", stones = "ZZ"
    Output: 0

Constraints:
    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.

A:
    jewels contains repeats -> not psossible
    jewels empty -> return 0
    stones empty -> return 0
    contain none alpha chars? -> not possible
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 for stone in stones if stone in jewels])


cases = [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0),
    ("", "abc", 0),
    ("ad", "", 0),
    ("abc", "d", 0),
    ("a", "A", 0),
]

sol = Solution()
for (jewels, stones, exp) in cases:
    assert (
        got := sol.numJewelsInStones(jewels, stones)
    ) == exp, f"Failed case ({jewels}, {stones}) - expecting ({exp}), got ({got})."
