"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k
    rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
    Input: n = 5
    Output: 2
    Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
    Input: n = 8
    Output: 3
    Explanation: Because the 4th row is incomplete, we return 3.

Constraints:
    - 1 <= n <= 2**31 - 1

A:
    n = 0
        return 0

D:
    n = 8, tot = 0
    s = 1, n = 8 - 1 = 7 > 0 -> tot += 1
    s = 2, n = 7 - 2 = 5 > 0 -> tot += 1
    s = 3, n = 5 - 3 = 2 > 0 -> tot += 1
    s = 4, n = 2 - 4 < 0 return tot = 3
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = 1
        tot = 0
        while True:
            n -= s
            if n >= 0:
                tot += 1
            else:
                return tot
            s += 1


cases = [(5, 2), (8, 3), (1, 1), (2, 1)]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.arrangeCoins(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
