"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a
    string s of length n where:
    - s[i] == 'I' if perm[i] < perm[i + 1], and
    - s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid
    permutations perm, return any of them.

Example 1:
    Input: s = "IDID"
    Output: [0,4,1,3,2]

Example 2:
    Input: s = "III"
    Output: [0,1,2,3]

Example 3:
    Input: s = "DDI"
    Output: [3,2,0,1]

Constraints:
    1 <= s.length <= 105
    s[i] is either 'I' or 'D'.

A:
    s = "I"  ->  return [0,1]
    s = "D"  ->  return [0,-1] -> [1,0]

D:
    right = 0
    left = 0
    perm = [0]
    for c in s:
        if c == "I"
            start += 1
            perm.append(start)
        else:
            left -= 1
            perm.append(left)

    return [x + abs(left) for x in perm]
            
"""

from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        right = 0
        left = 0
        perm = [0]
        for c in s:
            if c == "I":
                right += 1
                perm.append(right)
            else:
                left -= 1
                perm.append(left)

        return [x - left for x in perm]


cases = [
    ("IDID", [0, 4, 1, 3, 2]),
    ("III", [0, 1, 2, 3]),
    ("DDI", [3, 2, 0, 1]),
    ("", []),
    ("I", [0]),
    ("H", [0]),
]

sol = Solution()
for (s, exp) in cases:
    assert (
        got := sol.diStringMatch(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
