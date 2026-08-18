"""
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select
    one index and remove the letter at that index from word so that the frequency of every letter
    present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are
    equal, and false otherwise.

Note:
    - The frequency of a letter x is the number of times it occurs in the string.
    - You must remove exactly one letter and cannot choose to do nothing.

Example 1:
    Input: word = "abcc"
    Output: true
    Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency
        of 1.

Example 2:
    Input: word = "aazz"
    Output: false
    Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency
        of "z" is 2, or vice versa. It is impossible to make all present letters have equal
        frequency.

Constraints:
    - 2 <= word.length <= 100
    - word consists of lowercase English letters only.

A:
    empty word:
        not possible
    len(word) == 1:
        not possible
    word only made of one letter:
        return true
    word already has equal frequency (w/ more than one letter):
        return false

D:
    ddaccb
        c0 {
            d: 2
            a: 1
            c: 2
            b: 1
        }

        c1 {
            2: 2
            1: 2
        }

        would need to remove 2 things (2 letters from the sets of size 2 (i.e: d and c))
    abcc
        c0 {
            a: 1
            b: 1
            c: 2
        }

        c1 {
            1: 2
            2: 1
        }
        would need to remove  1 thing


"""


class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter

        l = list(word)

        for i in range(len(l)):
            n = l[:i] + l[i + 1 :]
            if len(set(Counter(n).values())) == 1:
                return True
        return False


cases = [
    ("abcc", True),
    ("aazz", False),
    ("aa", True),
    ("abc", True),
    ("abacc", True),
    ("abca", True),
    ("ddaccb", False),
    ("cbccca", False),
    ("cccd", True),
]

sol = Solution()
for word, exp in cases:
    assert (
        got := sol.equalFrequency(word)
    ) == exp, f"Failed case ({word}) - expecting ({exp}), got ({got})."
