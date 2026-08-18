"""Given a string s, find any substring of length 2 which is also present in the reverse of s.

Return true if such a substring exists, and false otherwise.

Example 1:
    Input: s = "leetcode"
    Output: true
    Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

Example 2:
    Input: s = "abcba"
    Output: true
    Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also
        present in reverse(s) == "abcba".

Example 3:
    Input: s = "abcd"
    Output: false
    Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.

Constraints:
    - 1 <= s.length <= 100
    - s consists only of lowercase English letters.

A:
    empty s?
        not possible
    s of size 1:
        return false
"""


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        if len(s) < 2:
            return False

        r = s[::-1]
        for i in range(len(s) - 1):
            if s[i : i + 2] in r:
                return True
        return False


cases = [
    ("leetcode", True),
    ("abcba", True),
    ("abcd", False),
    ("a", False),
    ("ab", False),
    ("aa", True),
    ("", False),
]

sol = Solution()
for s, exp in cases:
    assert (
        got := sol.isSubstringPresent(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
