"""
Given a string s and a character letter, return the percentage of characters in s that equal letter
    rounded down to the nearest whole percent.

Example 1:
    Input: s = "foobar", letter = "o"
    Output: 33
    Explanation:
    The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded
        down, so we return 33.

Example 2:
    Input: s = "jjjj", letter = "k"
    Output: 0
    Explanation:
    The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.

Constraints:
    1 <= s.length <= 100
    s consists of lowercase English letters.
    letter is a lowercase English letter.

A:
    empty(s) -> return 0
    letter not in s -> return 0
    letter is empty -> return 0
    letter is empty and s is empty -> ?
"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((s.count(letter) / len(s)) * 100)


cases = [
    ("foobar", "o", 33),
    ("jjjj", "k", 0),
    ("j", "j", 100),
    ("kj", "k", 50),
    ("kj", "j", 50),
    ("jjj", "j", 100),
    ("j", "k", 0),
]

sol = Solution()
for (s, letter, exp) in cases:
    assert (
        got := sol.percentageLetter(s, letter)
    ) == exp, f"Failed case ({s}, {letter}) - expecting ({exp}), got ({got})."
