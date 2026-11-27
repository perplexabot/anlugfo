"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t
    is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Example 4:
    Input: str1 = "AAAAAB", str2 = "AAA"
    Output: ""

Constraints:
    - 1 <= str1.length, str2.length <= 1000
    - str1 and str2 consist of English uppercase letters.

A:
    can size of s < t?
        yes, return ""
    what if size of t =  0
        not possible
    what if size of t = 1
        nothing special
    what if size of s = 1
        answer is s or ""
    is str1/str2 gaurenteed to be divisible by some s?
        no, LEET is a "prime" - only divisible by self or ""
    repeating pattern of size 1?
        utilize raw math?

D:
    Input: str1 = "ABABAB", str2 = "ABAB"
    smaller string: ABAB, gcd: AB (other than itself)
    Does str2 divide str1? no
    Does AB divide str1? yes
    return AB


    Input: str1 = "AAAAA", str2 = "AAA"
    smaller string: AAA, gcd: "A" (other than itself)
    Does str2 divide str1? no
    Does "A" divide larger string? Yes
    return A

P:
    kinda brute force
        get all repeat patterns in smaller one (including self)
        check these patterns divide the bigger str
        if none, return ""

O:
    size of small str is n, size of bigger one is m
    time
        get repeats of small (worst case):   O(n**2)
        check if repeats work in big str: O(n*m)
        O(n**2) + O(n*m) = O(nm)
    spac
        O(n**2) (worst case - saving the patterns whould would be n*(n/2) at most

T:
    "ABCABC", "ABC", ABC"
    "ABABAB", "ABAB", "AB"
    "LEET", "CODE", ""
    "AAAAAB", "AAA", ""
    "A", "A", "A"
    "AB", "A", ""
    "AA", "AA", "AA"
    "AA", "A", "A"
    "A", "AA", "A"
    "ABA", "AB", ""
    "AAAA", "AA", "AA"
    "AAAAA", "AA", A"
"""

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # size control
        smaller, bigger = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        patterns = set([smaller])
        for i in range(1, len(smaller) // 2 + 1):
            if len(smaller) % i == 0:
                # shift check
                good = True
                pattern = smaller[0:i]
                for j in range(i, len(smaller), i):
                    if smaller[j : j + i] != pattern:
                        good = False
                if good:
                    patterns.add(pattern)

        for p in sorted(patterns, key=lambda x: len(x), reverse=True):
            if len(bigger) % len(p) == 0:
                good = True
                for j in range(0, len(bigger), len(p)):
                    if bigger[j : j + len(p)] != p:
                        good = False
                        break
                if good:
                    return p

        return ""


cases = [
    (("ABABAB", "ABAB"), "AB"),
    (("ABCABC", "ABC"), "ABC"),
    (("ABC", "ABCABC"), "ABC"),
    (("LEET", "CODE"), ""),
    (("AAAAAB", "AAA"), ""),
    (("A", "A"), "A"),
    (("AB", "A"), ""),
    (("AA", "AA"), "AA"),
    (("AA", "A"), "A"),
    (("A", "AA"), "A"),
    (("ABA", "AB"), ""),
    (("AAAA", "AA"), "AA"),
    (("AAAAA", "AA"), "A"),
]

sol = Solution()

for case, expected in cases:
    assert (
        got := sol.gcdOfStrings(*case)
    ) == expected, f"WoOpSieEe case ({case}) failed. Expecting ({expected}), got ({got})."
