"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two
    non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number
    of ones in the right substring.



Example 1:
    Input: s = "011101"
    Output: 5
    Explanation:
    All possible ways of splitting s into two non-empty substrings are:
    left = "0" and right = "11101", score = 1 + 4 = 5
    left = "01" and right = "1101", score = 1 + 3 = 4
    left = "011" and right = "101", score = 1 + 2 = 3
    left = "0111" and right = "01", score = 1 + 1 = 2
    left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
    Input: s = "00111"
    Output: 5
    Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
    Input: s = "1111"
    Output: 3

Constraints:
    - 2 <= s.length <= 500
    - The string s consists of characters '0' and '1' only.

A:
    empty s
        not possible
    string of size 1
        not possible
    string of no 0 or no 1
        not possible
    string of just 0s or just 1s
        return len - 1
    can a substring be empty?
        no

D:
                012345
    Input: s = "011101"
                01110 1
                s[:5] s[5:]
    0 11101 = 1 + 4
    01 1101 = 1 + 3
    011 101 = 1 + 2
    0111 01 = 1 + 1
    01110 1 = 2 + 1

P:
    r = 0
    for i in 1..len(s):
        r = max(r, s[:i].count(0) + s[i:].count(1))
    return r

O
    above time complexity is O(n**2) one loop to go through s, another loop to count nums
    above space complexity is O(1)
    could it be possible to count once and math out the count in each iteration?

T:
    "011101", 5
    "00111", 5
    "1111", 3
    "01", 2
    "10", 0
    "11", 1
    "00", 1
    "010", 2
    "101", 2
"""


class Solution:
    def maxScore(self, s: str) -> int:
        r = 0
        for i in range(1, len(s)):
            r = max(r, s[:i].count('0') + s[i:].count('1'))
        return r


cases = [
    ("011101", 5),
    ("00111", 5),
    ("1111", 3),
    ("01", 2),
    ("10", 0),
    ("11", 1),
    ("00", 1),
    ("010", 2),
    ("101", 2),
]

sol = Solution()
for s, expected in cases:
    assert (
        got := sol.maxScore(s)
    ) == expected, f"Failed case ({s}) - expecting ({expected}), got ({got})."
