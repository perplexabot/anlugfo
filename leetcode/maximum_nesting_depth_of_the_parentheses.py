"""
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum
    number of nested parentheses.

Example 1:
    Input: s = "(1+(2*3)+((8)/4))+1"
    Output: 3
    Explanation:
        Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
    Input: s = "(1)+((2))+(((3)))"
    Output: 3
    Explanation:
        Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
    Input: s = "()(())((()()))"
    Output: 3

Constraints:
    - 1 <= s.length <= 100
    - s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
    - It is guaranteed that parentheses expression s is a VPS.

A:
    empty string
        return 0
    invalid paren
        not possible
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        top = 0
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            if c == ')':
                top = max(top, cnt)
                cnt -= 1
        return top


cases = [
    ("(1+(2*3)+((8)/4))+1", 3),
    ("(1)+((2))+(((3)))", 3),
    ("()(())((()()))", 3),
]

sol = Solution()

for case, exp in cases:
    assert (
        got := sol.maxDepth(case)
    ) == exp, f'Failed case ({case}) - expecting ({exp}), got ({got}).'
