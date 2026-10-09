"""
You are given a string s and two distinct lowercase English letters x and y.
Rearrange the characters of s to construct a new string t such that:
    - t is a permutation of s.
    - Every occurrence of y appears before every occurrence of x in t.
Return any valid string t.

Example 1:
    Input: s = "aabc", x = "a", y = "c"
    Output: "cbaa"
    Explanation:
    The string "cbaa" is a permutation of "aabc", and every occurrence of 'c' appears before every
        occurrence of 'a'.

Example 2:
    Input: s = "dcab", x = "d", y = "b"
    Output: "cabd"
    Explanation:
    The string "cabd" is a permutation of "dcab", and every occurrence of 'b' appears before every
        occurrence of 'd'.

Example 3:
    Input: s = "axe", x = "o", y = "x"
    Output: "axe"
    Explanation:
    The string "axe" is already valid. Since 'o' does not occur in the string, the required
        condition is automatically satisfied.

Constraints:
    - 1 <= s.length <= 100
    - s consists of lowercase English letters.
    - x and y are lowercase English letters.
    - x != y

A:
    s only has x's or y's
        just return
    s has no x and no y
        just return
    s has either an x or a y
        just return
    s is empty
        just return
    s of size 1
        just return
    s of size 2
        ensure y before x
    x or y empty?
        no possible
    x == y
        not possible

D:
    Input: s = "dcab", x = "d", y = "b"
    bdca

P:
    news = []
    prefixCnt = 0
    for char in s:
        if s == y
            prefixCnt += 1
        else:
            news += char
    return ''.join([y]*prefixCnt + news)

O:
    with above algo:
        O(n) time complexity
        O(n) space complexity

    may be able to reduce space complexity by doing an inplace change upon s
        basically swap any time a y and x are found if y index > x index

T:
    ("aabc", "a", "c", "cbaa"),
    ("dcab", "d", "b", "cabd"),
    ("axe", "o", "x", "axe"),
    ("aaa", "a", "b", "aaa"),
    ("a", "a", "b", "a"),
    ("ab", "a", "b", "ba"),
    ("ab", "b", "a", "ab"),
    ("abc", "a", "b", "bac"),
    ("abc", "a", "c", "cab"),
    ("abc", "b", "c", "cab"),
"""


class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        news = []

        prefixCnt = 0
        for char in s:
            if char == y:
                prefixCnt += 1
            else:
                news += char
        return ''.join([y] * prefixCnt + news)


cases = [
    ("aabc", "a", "c", "caab"),
    ("dcab", "d", "b", "bdca"),
    ("axe", "o", "x", "xae"),
    ("aaa", "a", "b", "aaa"),
    ("a", "a", "b", "a"),
    ("ab", "a", "b", "ba"),
    ("ab", "b", "a", "ab"),
    ("abc", "a", "b", "bac"),
    ("abc", "a", "c", "cab"),
    ("abc", "b", "c", "cab"),
]

sol = Solution()
for s, x, y, expected in cases:
    assert (
        got := sol.rearrangeString(s, x, y)
    ) == expected, f"Failed case ({s}, {x}, {y}) - expecting ({expected}), got ({got})."
