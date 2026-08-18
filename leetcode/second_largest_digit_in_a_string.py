"""
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 
    if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:
    Input: s = "dfa12321afd"
    Output: 2
    Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
    Input: s = "abc1111"
    Output: -1
    Explanation: The digits that appear in s are [1]. There is no second largest digit. 

Constraints:
    1 <= s.length <= 500
    s consists of only lowercase English letters and/or digits.
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        from string import digits

        ds = set()
        for c in s:
            if c in digits:
                ds.add(c)

        if len(ds) < 2:
            return -1

        ds.discard(max(ds))
        return int(max(ds))


cases = [
    ("dfa12321afd", 2),
    ("abc1111", -1),
]

sol = Solution()
for (s, exp) in cases:
    assert (
        got := sol.secondHighest(s)
    ) == exp, f"Failed case ({s}) - got ({got}), expecting ({exp})."
