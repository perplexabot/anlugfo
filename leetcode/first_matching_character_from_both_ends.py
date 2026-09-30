"""
You are given a string s of length n consisting of lowercase English letters.

Return the smallest index i such that s[i] == s[n - i - 1].

If no such index exists, return -1.

Example 1:
    Input: s = "abcacbd"
    Output: 1
    Explanation:
        At index i = 1, s[1] and s[5] are both 'b'.
        No smaller index satisfies the condition, so the answer is 1.

Example 2:
    Input: s = "abc"
    Output: 1
    Explanation:
        At index i = 1, the two compared positions coincide, so both characters are 'b'.
        No smaller index satisfies the condition, so the answer is 1.

Example 3:
    Input: s = "abcdab"
    Output: -1
    Explanation:
        For every index i, the characters at positions i and n - i - 1 are different.
        Therefore, no valid index exists, so the answer is -1.

Constraints:
    - 1 <= n == s.length <= 100
    - s consists of lowercase English letters.

A:
    n = 0?
        not possible
    not possible
        return -1
    n = 1?
        s[0] should equal s[1-0-1], yes
        always true (return 0)
    n % 2 == 1 (odd)
        always true, need to find smallest i though, worst case n // 2

D:
    Input: s = "abcacbd"
    i = 0, a != d
    i = 1, b == b
    return 1

P:
    while i < n - i -1:
        if s[i] == s[n-i-1]:
            return i
    return -1

O:
    one pass, no extra ds

T:
    ('abcacbd', 1),
    ('abc', 1),
    ('abcdab' -1),
    ('a', 0),
    ('ab', -1),
    ('aa', 0),
    ('aba', 0),
    ('abcbd', 1),
"""


class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        i = 0
        n = len(s)
        while i <= n - i - 1:
            if s[i] == s[n - i - 1]:
                return i
            i += 1
        return -1


cases = [
    ('abcacbd', 1),
    ('abc', 1),
    ('abcdab', - 1),
    ('a', 0),
    ('ab', -1),
    ('aa', 0),
    ('aba', 0),
    ('abcbd', 1),
]

sol = Solution()

for s, expected in cases:
    assert (
        got := sol.firstMatchingIndex(s)
    ) == expected, f"Failed case ({s}) - expecting ({expected}), got ({got})."
