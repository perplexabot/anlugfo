"""
Given two strings s and t, return true if they are equal when both are typed into empty text
    editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".

Example 2:
    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

Example 3:
    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".

Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

A:
    only "#" in both:
        return true

    s starts with "#":
        remove leading '#'

D:
    regex to remove ('*#') for s0
    regex to remove ('*#') for s1
    compare s0 and s1
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        import re

        c = re.compile(r'^#{1,}')
        sn = c.sub('', s)
        tn = c.sub('', t)

        c = re.compile(r'[a-z]#')
        stimes = sn.count('#')
        for i in range(stimes):
            sn = c.sub('', sn)

        ttimes = tn.count('#')
        for i in range(ttimes):
            tn = c.sub('', tn)

        c = re.compile(r'^#{1,}')
        sn = c.sub('', sn)
        tn = c.sub('', tn)
        return sn == tn


cases = [
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("a#c", "b", False),
    ("###", "#####", True),
    ("#a", "#a", True),
    ("#a", "#b", False),
    ("b#a", "c#a", True),
    ("a#", "b#", True),
    ("##a", "####a", True),
    ("##b", "####a", False),
    ("a##c", "#a#c", True),
]

sol = Solution()
for s, t, exp in cases:
    assert (
        got := sol.backspaceCompare(s, t)
    ) == exp, f"Failed case ({s}, {t}) - expecting ({exp}), got ({got})."
