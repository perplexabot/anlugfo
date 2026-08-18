"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key
    might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your
    friends name, with some characters (possibly none) being long pressed.

Example 1:
    Input: name = "alex", typed = "aaleex"
    Output: true
    Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
    Input: name = "saeed", typed = "ssaaedd"
    Output: false
    Explanation: 'e' must have been pressed twice, but it was not in the typed output.

Constraints:
    - 1 <= name.length, typed.length <= 1000
    - name and typed consist of only lowercase English letters.

A:
    name of size 0:
        not poss
    name of size 1:
        equality check

A:
    ?

D:
    groupby(name)
    groupby(typed)
    for lettern, lettert in zip_longest(fill=None):
        if lettern != lettert:
            return False

        if len(lettern) > len(lettert):
            return False
    return True
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        from itertools import groupby, zip_longest

        nameG = groupby(name)
        typedG = groupby(typed)

        for n, t in zip_longest(nameG, typedG):
            if not n or not t:
                return False

            nameChar, nameSeq = n
            typeChar, typeSeq = t
            nameCharCnt = sum(1 for _ in nameSeq)
            typeCharCnt = sum(1 for _ in typeSeq)

            if nameChar != typeChar:
                return False

            if nameCharCnt > typeCharCnt:
                return False
        return True


cases = [
    ("alex", "aaleex", True),
    ("saeed", "ssaaedd", False),
    ("a", "a", True),
    ("a", "aaaa", True),
    ("aa", "abbb", False),
]

sol = Solution()
for name, typed, exp in cases:
    assert (
        got := sol.isLongPressedName(name, typed)
    ) == exp, f"Failed case ({name}, {typed}) - expecting ({exp}), got ({got})."
