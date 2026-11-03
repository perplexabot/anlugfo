"""
You are given a string s of length n and an integer k.

A cyclic rotation of s is obtained by choosing a prefix of s whose length is between 0 and n - 1
    (inclusive), and moving it to the end of the string while preserving the order of all
    characters.

For every cyclic rotation of s, let its score be the number of indices i such that 0 <= i < n - 1
    and the characters at positions i and i + 1 are equal.

Return the number of cyclic rotations of s whose score equals k.

Example 1:
    Input: s = "aab", k = 1
    Output: 2
    Explanation:
    The cyclic rotations of s are:
        "aab": The characters at positions 0 and 1 are equal, so score = 1.
        "aba": No two adjacent characters are equal, so score = 0.
        "baa": The characters at positions 1 and 2 are equal, so score = 1.
    Since score equals k for 2 cyclic rotations of s, the answer is 2.

Example 2:
    Input: s = "abca", k = 0
    Output: 1
    Explanation:
        The cyclic rotations of s are:
            "abca": No two adjacent characters are equal, so score = 0.
            "bcaa": The characters at positions 2 and 3 are equal, so score = 1.
            "caab": The characters at positions 1 and 2 are equal, so score = 1.
            "aabc": The characters at positions 0 and 1 are equal, so score = 1.
        Since score equals k for only 1 cyclic rotation of s, the answer is 1.

Constraints:
    - 2 <= n == s.length <= 100
    - s only consists of lowercase English letters.
    - 0 <= k <= n - 1

A:
    len of s < 2:
        not possible
    len of s == 2:
        if k == 0
            if s[0] != S[1] return 1 else 0
        if k == 1:
            if s[0] == S[1] return 1 else 0
    score of roration 'aaa'?
        2
    does aa* have cyclic rotations?
        assuming yes
D:
    Input: s = "abca", k = 0
    news = s+s = abcaabca
                 01234567

    ind perm   score
    0-3 abca    0
    1-4 bcaa    1
    2-5 caab    1
    3-6 aabc    1

    number of cycles whos score is 0 = 1 (abca)

P:
    for i in {0..(len(s)-1}:
        if score(s[i:i+len(s)) == k:
            cnt ++

O:
    anyway to just reiterate over s instead of concating two s's?
        modulo?

T:
    "aab", 1, 2
    "abca", 0, 1
    "aa", 1, 2
    "aa", 0, 0
    "ab", 0, 1
    "ab", 1, 0
"""


class Solution:
    def countRotations(self, s: str, k: int) -> int:
        d = s + s
        total = 0
        for i in range(0, len(s)):
            score = [1 for j in range(i, i + len(s) - 1) if d[j] == d[j + 1]]
            total += 1 if sum(score) == k else 0
        return total


cases = [
    (("aab", 1), 2),
    (("abca", 0), 1),
    (("aa", 1), 2),
    (("aa", 0), 0),
    (("ab", 0), 2),
    (("ab", 1), 0),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.countRotations(*case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
sol.countRotations('aab', 1)
