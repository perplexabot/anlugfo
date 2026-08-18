"""
Given two strings s and goal, return true if and only if s can become goal after some number of
    shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
    - For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
    Input: s = "abcde", goal = "cdeab"
    Output: true

Example 2:
    Input: s = "abcde", goal = "abced"
    Output: false

Constraints:
    - 1 <= s.length, goal.length <= 100
    - s and goal consist of lowercase English letters.

A:
    goal size  != s size
        return false
    set(goal) - set(s) || set(s) - set(goal) != set()
        return false

A:
    does case matter:
        all case is lower

D:
    check if goal is in s+s
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in s + s if len(s) == len(goal) else False


cases = [
    ("abcde", "cdeab", True),
    ("abcde", "abced", False),
    ("ab", "ba", True),
    ("aa", "aa", True),
    ("a", "a", True),
    ("a", "b", False),
    ("abc", "cab", True),
    ("", "a", False),
    ("aa", "a", False),
]

sol = Solution()
for s, goal, exp in cases:
    assert (
        got := sol.rotateString(s, goal)
    ) == exp, f"Failed case ({s}, {goal}) - expecting ({exp}), got ({got})."
