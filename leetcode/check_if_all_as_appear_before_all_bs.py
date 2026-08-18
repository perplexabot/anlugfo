"""
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears
    before every 'b' in the string. Otherwise, return false.

Example 1:
    Input: s = "aaabbb"
    Output: true
    Explanation:
    The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
    Hence, every 'a' appears before every 'b' and we return true.

Example 2:
    Input: s = "abab"
    Output: false
    Explanation:
    There is an 'a' at index 2 and a 'b' at index 1.
    Hence, not every 'a' appears before every 'b' and we return false.

Example 3:
    Input: s = "bbb"
    Output: true
    Explanation:
    There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

Constraints:
    1 <= s.length <= 100
    s[i] is either 'a' or 'b'.

A:
    list of size less than 2:
        return true
    other than a and b
        not possible

D:
    find first b
    check if any a is after it
"""


class Solution:
    def checkString(self, s: str) -> bool:
        if len(s) < 2:
            return True

        if 'a' not in s or 'b' not in s:
            return True

        first_b_index = s.find('b')
        for i in s[first_b_index:]:
            if i == 'a':
                return False
        return True


cases = [
    ("aaabbb", True),
    ("abab", False),
    ("bbb", True),
    ("aaa", True),
    ("", True),
    ("a", True),
    ("b", True),
    ("ba", False),
    ("ab", True),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.checkString(case)
    ) == exp, f"Failed case ({case}) - got ({got}), expecting ({exp})."
