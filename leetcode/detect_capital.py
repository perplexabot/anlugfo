"""
We define the usage of capitals in a word to be right when one of the following cases holds:
    - All letters in this word are capitals, like "USA".
    - All letters in this word are not capitals, like "leetcode".
    - Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example 1:
    Input: word = "USA"
    Output: true

Example 2:
    Input: word = "FlaG"
    Output: false

Constraints:
    - 1 <= word.length <= 100
    - word consists of lowercase and uppercase English letters.

A:
    empty string?
        not possible
    single caps?
        true
    single lower?
        true?
    only numbers?
        not possible

D:
    Input: word = "FlaG"
    F. good
    l. good
    a. good
    G. bad

P:
    first_letter_is_caps?
        if yes:
            all should be lower or all should be upper
        if no:
            all should be lower

O:
    time: O(n)
    spac: O(1)

T:
    "USA", true
    "FlaG", false
    "F", true
    "b", true
    "Ha", true
    "HA", true
    "hA", false
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if word[0].isupper():
            return word[1:].islower() or word[1:].isupper()
        else:
            return word[1:].islower()


cases = [
    ("USA", True),
    ("FlaG", False),
    ("F", True),
    ("b", True),
    ("Ha", True),
    ("HA", True),
    ("hA", False),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.detectCapitalUse(case)
    ) == expected, f"Failed case ({case}) - got ({got}), expecting ({expected})."
