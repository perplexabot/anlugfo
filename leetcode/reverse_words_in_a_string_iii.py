"""
Given a string s, reverse the order of characters in each word within a sentence while still
    preserving whitespace and initial word order.

Example 1:
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
    Input: s = "God Ding"
    Output: "doG gniD"

Constraints:
    1 <= s.length <= 5 * 10**4
    s contains printable ASCII characters.
    s does not contain any leading or trailing spaces.
    There is at least one word in s.
    All the words in s are separated by a single space.

A:
    empty string
        not possible
    string with one word:
        just reverse
    string with two words:
        reverse words only
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split()])


cases = [
    ("abc", "cba"),
    ("A", "A"),
    ("Abc", "cbA"),
    ("I love hell", "I evol lleh"),
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("God Ding", "doG gniD"),
]

sol = Solution()
for s, exp in cases:
    assert (
        got := sol.reverseWords(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
