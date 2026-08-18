"""
Given an array of string words, return all strings in words that are a `substring` of another
    word. You can return the answer in any order.

Example 1:
    Input: words = ["mass","as","hero","superhero"]
    Output: ["as","hero"]
    Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
    ["hero","as"] is also a valid answer.

Example 2:
    Input: words = ["leetcode","et","code"]
    Output: ["et","code"]
    Explanation: "et", "code" are substring of "leetcode".

Example 3:
    Input: words = ["blue","green","bu"]
    Output: []
    Explanation: No string of words is substring of another string.

Constraints:
    - 1 <= words.length <= 100
    - 1 <= words[i].length <= 30
    - words[i] contains only lowercase English letters.
    - All the strings of words are unique.

A:
    empty array
        nope
    size 1
        return empty
    caps matter?
        nope - all lower
    letters only?
        ye
A:
    repeat words?
        no

"""

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        final = []
        words.sort(key=lambda x: len(x))
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    final.append(words[i])
                    break
        return final


sol = Solution()

cases = [
    (["mass", "as", "hero", "superhero"], ["as", "hero"]),
    (["leetcode", "et", "code"], ["et", "code"]),
    (["blue", "green", "bu"], []),
    (["a", "b"], []),
    (["ab", "ba", "bb"], []),
    (["aaa", "aaaa", "aaaaa"], ["aaa", "aaaa"]),
]

for case, exp in cases:
    assert (got := sorted(sol.stringMatching(case))) == sorted(
        exp
    ), f"Failed case ({case}) - expecting ({exp}), got ({got})."
