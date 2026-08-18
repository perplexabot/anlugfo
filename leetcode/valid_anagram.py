"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word
    or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution
    to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        c0 = Counter(s)
        c1 = Counter(t)
        return c0 == c1


cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "b", False),
    ("a", "a", True),
    ("ab", "ba", True),
]

sol = Solution()
for (s, t, exp) in cases:
    assert (
        got := sol.isAnagram(s, t)
    ) == exp, f"Failed case ({s}, {t}) - expecting ({exp}), got ({got})."
