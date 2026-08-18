"""
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note
    that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.

Example 1:
    Input: s = "XXX"
    Output: 1
    Explanation: XXX -> OOO
    We select all the 3 characters and convert them in one move.

Example 2:
    Input: s = "XXOX"
    Output: 2
    Explanation: XXOX -> OOOX -> OOOO
    We select the first 3 characters in the first move, and convert them to 'O'.
    Then we select the last 3 characters and convert them so that the final string contains
        all 'O's.

Example 3:
    Input: s = "OOOO"
    Output: 0
    Explanation: There are no 'X's in s to convert.

Constraints:
    3 <= s.length <= 1000
    s[i] is either 'X' or 'O'.

A:
    len(s) == 0: return 0
    len(s) < 4: return 1 if x inside else 0

D:
    find all x triplets, replace starting from left (where the left element is 'O')
    find all x doubles, replace starting from left (where the left element is 'O')
    find all x singles, replace starting from left (where the left element is 'O')
    --------
    find all ranges of x
    for each range, if len(range) <= 3, count += 1
                    if len(range) > 3, count += ceil(len(range)/3)
    return count


    x o o x x o x o x x x
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        curr = 0
        hits = 0
        while curr < len(s):
            if s[curr] == 'X':
                hits += 1
                curr += 3
            else:
                curr += 1
        return hits


cases = [
    ("XXX", 1),
    ("XXOX", 2),
    ("OOOO", 0),
    ("X", 1),
    ("XX", 1),
    ("XXX", 1),
    ("XXXX", 2),
    ("XXXXX", 2),
    ("XXXXXX", 2),
    ("XXXXXXX", 3),
    ("XXXOXXX", 2),
    ("XXXXOXXX", 3),
    ("O", 0),
    ("OO", 0),
    ("OOO", 0),
    ("OXOX", 1),
]

sol = Solution()
for (s, exp) in cases:
    assert (
        got := sol.minimumMoves(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
