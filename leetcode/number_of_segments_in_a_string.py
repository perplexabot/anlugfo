"""
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
    Input: s = "Hello, my name is John"
    Output: 5
    Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
    Input: s = "Hello"
    Output: 1

Constraints:
    - 0 <= s.length <= 300
    - s consists of lowercase and uppercase English letters, digits, or one of the following
        characters "!@#$%^&*()_+-=',.:".
    - The only space character in s is ' '.

A:
    only space characters?
        return 0
    tabs and other space types?
        doesn't matter
    spaces at the beginning or end
        strip them
    no spaces:
        return 1
D:
    'a b '
    return 2

O:
    O(n) + O(n) = O(n)

T:
    "Hello, my name is John", 5
    "Hello", 1
    "", 0
    " ", 0
    "    ", 0
    " r ", 1
    " a", 1
    "a a", 2
"""


class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


cases = [
    ("Hello, my name is John", 5),
    ("Hello", 1),
    ("", 0),
    (" ", 0),
    ("    ", 0),
    (" r ", 1),
    (" a", 1),
    ("a a", 2),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.countSegments(case)
    ) == exp, f"Failed case ({case}) - got ({got}), expected ({exp})."
