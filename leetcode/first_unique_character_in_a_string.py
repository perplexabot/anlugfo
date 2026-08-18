"""
Given a string s, find the first non-repeating character in it and return its index. If it does not
    exist, return -1.

Example 1:
    Input: s = "leetcode"
    Output: 0

Example 2:
    Input: s = "loveleetcode"
    Output: 2

Example 3:
    Input: s = "aabb"
    Output: -1

Constraints:
    1 <= s.length <= 105
    s consists of only lowercase English letters.

A:
    empty s:
        return -1
    len(s) == 1:
        return [0]
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict

        d = defaultdict(int)
        to_ind = {}
        for ind, c in enumerate(s):
            to_ind[c] = ind
            d[c] += 1

        for k in d:
            if d[k] == 1:
                return to_ind[k]

        return -1


cases = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
]

sol = Solution()
for s, exp in cases:
    assert (
        got := sol.firstUniqChar(s)
    ) == exp, f'Failed case ({s}) - expecting ({exp}), got ({got}).'
