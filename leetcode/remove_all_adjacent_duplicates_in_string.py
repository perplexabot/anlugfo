"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of
    choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the
    answer is unique.

Example 1:
    Input: s = "abbaca"
    Output: "ca"
    Explanation:
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this
        is the only possible move.  The result of this move is that the string is "aaca", of which
        only "aa" is possible, so the final string is "ca".

Example 2:
    Input: s = "azxxzy"
    Output: "ay"

Constraints:
    1 <= s.length <= 105
    s consists of lowercase English letters.

A:
    empty s -> not possible
    s is only repeat -> return ""
    len(s) < 2 -> return s

D:
    Input: s = "azxxzy"
        -> azzy
        -> zy

    Input: s = "axxyya"
        -> axxa
        -> aa
        -> ""
P:
    curr = s
    prev_size = len(s)
    new_size = None
    while True:
        old_size = len(curr)

        if old_size < 2:
            break

        for i in range(1, len(curr)):
            if curr[i-1] == cur[i]:
                curr = curr[:i-1] + curr[i+1:]

        if len(curr) == old_size:
            break
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        tmp = []
        for c in s:
            if tmp and tmp[-1] == c:
                tmp.pop()
            else:
                tmp.append(c)
        return ''.join(tmp)


cases = [
    ("abbaca", "ca"),
    ("azxxzy", "ay"),
    ("x", "x"),
    ("xx", ""),
    ("abba", ""),
]

sol = Solution()
for (s, exp) in cases:
    assert (
        got := sol.removeDuplicates(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
