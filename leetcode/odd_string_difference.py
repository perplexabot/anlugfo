"""
You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length
    n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the
    difference between two letters is the difference between their positions in the alphabet i.e.
    the position of 'a' is 0, 'b' is 1, and 'z' is 25.

    For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].

All the strings in words have the same difference integer array, except one. You should find that
    string.

Return the string in words that has different difference integer array.

Example 1:
    Input: words = ["adc","wzy","abc"]
    Output: "abc"
    Explanation:
    - The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
    - The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
    - The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
    The odd array out is [1, 1], so we return the corresponding string, "abc".

Example 2:
    Input: words = ["aaa","bob","ccc","ddd"]
    Output: "bob"
    Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].

Constraints:
    - 3 <= words.length <= 100
    - n == words[i].length
    - 2 <= n <= 20
    - words[i] consists of lowercase English letters.

A:
     empty words:
        return none
    words of size one:
        return string
    string of size 0:
        not possible, at least size 2

D:
    ds = []
    for each word in words
        for ind in word:
            d = [char_to_int(word[ind + 1]) - char_to_int(word[ind])]
            ds.append(d)

    if ds.count(ds[0]) == 1:
        return words[0]
    else:
        for ind in ds:
            if ds[i] i != ds[0]:
                return words[i]
"""

from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        from string import ascii_lowercase

        ds = []
        char_to_int = {char: ind for ind, char in enumerate(ascii_lowercase)}
        for word in words:
            d = []
            for i in range(len(word) - 1):
                d.append(char_to_int[word[i + 1]] - char_to_int[word[i]])
            ds.append(d)

        if ds.count(ds[0]) == 1:
            return words[0]
        else:
            for ind, _ in enumerate(ds):
                if ds[ind] != ds[0]:
                    return words[ind]


cases = [
    (["adc", "wzy", "abc"], "abc"),
    (["aaa", "bob", "ccc", "ddd"], "bob"),
    (["adc", "wzy", "abc"], "abc"),
]

sol = Solution()
for words, exp in cases:
    assert (
        got := sol.oddString(words)
    ) == exp, f"Failed case ({words}) - expecting ({exp}), got ({got})."
