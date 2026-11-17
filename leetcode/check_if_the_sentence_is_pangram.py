"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a
    pangram, or false otherwise.

Example 1:
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: true
    Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
    Input: sentence = "leetcode"
    Output: false

Constraints:
    - 1 <= sentence.length <= 1000
    - sentence consists of lowercase English letters.

A:
    more than once ok?
        yes
    caps vs lower?
        lowers only

D:
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: true

P:
    return set(alphabet_lower) == set(sentence)

O:
    time: O(n)
    spac: O(n)

    anyway to do this with space = O(1)?
        sort the array and ensure the diff between each consequtive elem is 1 or 0 (ascii) and
        the size is len(alphabets_lower) + (number of times diff between consquietive elements
        was 0). But time would be O(nlogn)

T:
    "thequickbrownfoxjumpsoverthelazydog" true
    "leetcode" false
    "a" false
    "" false
    "abcdefghijklmnopqrstuvwxyz" true
    "bcdefghijklmnopqrstuvwxyz" false
    "abcdefghijklmnopqrstuvwxy" false
"""

from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(sentence) == set(ascii_lowercase)


cases = [
    ("thequickbrownfoxjumpsoverthelazydog", True),
    ("leetcode", False),
    ("a", False),
    ("", False),
    ("abcdefghijklmnopqrstuvwxyz", True),
    ("bcdefghijklmnopqrstuvwxyz", False),
    ("abcdefghijklmnopqrstuvwxy", False),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.checkIfPangram(case)
    ) == expected, f"Woah! Failed case ({case})! Expecting ({got}), expecting ({expected})."
