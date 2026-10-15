"""
You are given a 0-indexed string array words.
Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
    isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2,
    and false otherwise.

For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and
    also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j, and
    isPrefixAndSuffix(words[i], words[j]) is true.

Example 1:
    Input: words = ["a","aba","ababa","aa"]
    Output: 4
    Explanation: In this example, the counted index pairs are:
    i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
    i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
    i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
    i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
    Therefore, the answer is 4.

Example 2:
    Input: words = ["pa","papa","ma","mama"]
    Output: 2
    Explanation: In this example, the counted index pairs are:
    i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
    i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
    Therefore, the answer is 2.

Example 3:
    Input: words = ["abab","ab"]
    Output: 0
    Explanation: In this example, the only valid index pair is i = 0 and j = 1, and isPrefixAndSuffix("abab", "ab") is false.
    Therefore, the answer is 0.

Constraints:
    - 1 <= words.length <= 50
    - 1 <= words[i].length <= 10
    - words[i] consists only of lowercase English letters.

A:
    no words:
        not possible
    1 word:
        return false
    2 words:
        1 check
    word of length 0
        not possible
    does something like 'a' and 'a' count?
        yes?

D:
                    0    1      2    3
    Input: words = ["pa","papa","ma","mama"]
    0 and 1 : yes
    0 and 2 : no
    0 and 3 : no
    1 and 2 : no
    1 and 3 : no
    2 and 3 : yes
    return 2

P:
    count = 0
    for ind, w1 in enumerate(words[:-1]):
        for w2 in words(ind:)
            if w2.startswith(w1) and w2.endswith(w1):
                count ++
    return count

O:
    O(n**2) in time
    O(1) in space

T:
    (["a","aba","ababa","aa"], 4)
    (["pa","papa","ma","mama"], 2)
    (["abab","ab"], 0)
    (["a", "b"], 0)
    (["a"], 0)
    (["a", "a"], 1)
    (["a", "aba"],1)
    (["b", "aba"],0)
    (["a", "aba", "a"],1)
"""

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for ind, w1 in enumerate(words[:-1]):
            for w2 in words[ind + 1 :]:
                if w2.startswith(w1) and w2.endswith(w1):
                    count += 1
        return count


cases = [
    (["a", "aba", "ababa", "aa"], 4),
    (["pa", "papa", "ma", "mama"], 2),
    (["abab", "ab"], 0),
    (["a", "b"], 0),
    (["a"], 0),
    (["a", "a"], 1),
    (["a", "aba"], 1),
    (["b", "aba"], 0),
    (["a", "aba", "a"], 2),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.countPrefixSuffixPairs(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
