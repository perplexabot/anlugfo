"""
Given a string of English letters s, return the greatest English letter which occurs as both a
    lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such
    letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.

Example 1:
    Input: s = "lEeTcOdE"
    Output: "E"
    Explanation:
    The letter 'E' is the only letter to appear in both lower and upper case.

Example 2:
    Input: s = "arRAzFif"
    Output: "R"
    Explanation:
    The letter 'R' is the greatest letter to appear in both lower and upper case.
    Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

Example 3:
    Input: s = "AbCdEfGhIjK"
    Output: ""
    Explanation:
    There is no letter that appears in both lower and upper case.

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase and uppercase English letters.

A:
    empty s -> return empty string
    len(s) < 2: -> return empty string
    non alpha in s -> doesn't matter

D:
    Input: s = "AbCdEfGhIjK"
    A:
        cnts['a'].append('A')
    b:
        cnts['b'].append('b')
    C:
        cnts['c'].append('C')

    possible = [x for x in cnts if cnts[x] > 1]
    return max(possible)
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        from collections import defaultdict

        if len(s) < 2:
            return ""

        cnts = defaultdict(set)
        for c in s:
            cnts[c.upper()].add(c)

        return max([x for x in cnts if len(cnts[x]) > 1], default="")


cases = [
    ("lEeTcOdE", "E"),
    ("arRAzFif", "R"),
    ("AbCdEfGhIjK", ""),
    ("A", ""),
    ("Aa", "A"),
    ("Ab", ""),
    ("ab", ""),
    ("Aba", "A"),
]

sol = Solution()
for (s, exp) in cases:
    assert (
        got := sol.greatestLetter(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
