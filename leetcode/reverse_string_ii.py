"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting
    from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but
    greater than or equal to k characters, then reverse the first k characters and leave the other
    as original.

Example 1:
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Example 2:
    Input: s = "abcd", k = 2
    Output: "bacd"

Constraints:
    - 1 <= s.length <= 10**4
    - s consists of only lowercase English letters.
    - 1 <= k <= 10**4

A:
    empty s:
        return s
    len of s == 1:
        return s
    len of s < k:
        return reverse s
    len of s == k:
        return reverse s

A:
    what if k == 0:
        not possible

D:
    Input: s = "abcdefg", k = 2
    abcd -> bacd
    efg  -> feg
    return bacdfeg

P:
    last = 0
    chunks = []
    ssize = len(s)
    while last < ssize:
        if ssize - last < k:
            chunks.append(s[last:][::-1])
        elif ssize - last < 2k:
            chunk0 = s[last:last+k]
            chunk1 = s[last+k:]
            chunks.append(chunk0)
            chunks.append(chunk1)
        else 
            chunk0 = s[last:last+k]
            chunk1 = s[last+k:last+(2*k)]
            chunks.append(chunk0)
            chunks.append(chunk1)
        last += 2k
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        last = 0
        chunks = []
        ssize = len(s)
        while last < ssize:
            if ssize - last < k:
                chunks.append(s[last:][::-1])
            elif ssize - last < (2 * k):
                chunks.append(s[last : last + k][::-1])
                chunks.append(s[last + k :])
            else:
                chunks.append(s[last : last + k][::-1])
                chunks.append(s[last + k : last + (2 * k)])
            last += 2 * k
        return ''.join(chunks)


cases = [
    ("abcdefg", 2, "bacdfeg"),
    ("abcd", 2, "bacd"),
    ("abc", 3, "cba"),
    ("abc", 2, "bac"),
    ("aa", 10, "aa"),
    ("ab", 1, "ab"),
]

sol = Solution()
for s, k, exp in cases:
    assert (
        got := sol.reverseStr(s, k)
    ) == exp, f"Failed case ({s}, {k}) - expecting ({exp}), got ({got})."
