"""
Given a string s, return the length of the longest substring between two equal characters, excluding
    the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "aa"
    Output: 0
    Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
    Input: s = "abca"
    Output: 2
    Explanation: The optimal substring here is "bc".

Example 3:
    Input: s = "cbzxy"
    Output: -1
    Explanation: There are no characters that appear twice in s.

Constraints:
    1 <= s.length <= 300
    s contains only lowercase English letters.

A:
    no repeats:
        return -1
    only repeats:
        return 0

A:
    ?

D:
    "abca"
    {a:0,3, b:1, c:2}
    return (3 - 0) - 1
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        from collections import defaultdict

        d = defaultdict(list)
        for ind, char in enumerate(s):
            d[char].append(ind)

        return max((max(d[char]) - min(d[char]) - 1 for char in d), default=-1)


cases = [
    ("aa", 0),
    ("abca", 2),
    ("cbzxy", -1),
    ("aaa", 1),
    ("a", -1),
    ("aaaa", 2),
    ("abccba", 4),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.maxLengthBetweenEqualCharacters(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
