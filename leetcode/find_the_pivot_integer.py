"""
Given a positive integer n, find the pivot integer x such that:
    - The sum of all elements between 1 and x inclusively equals the sum of all elements between x
        and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will
    be at most one pivot index for the given input.

Example 1:
    Input: n = 8
    Output: 6
    Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:
    Input: n = 1
    Output: 1
    Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:
    Input: n = 4
    Output: -1
    Explanation: It can be proved that no such integer exist.

Constraints:
    1 <= n <= 1000

A:
    int = 0 -> not possible only positive

D:
    n = 8
        1 2 3 4 5 6 7 8
         |
        1/2 (1 + 1) = 1  ==? (7/2) (8 + 2) = 35, false
        when is arithmatic sum on left equal to right:
            (i/2)(1+i) = ((n-i+1)/2)(i+n)
            => i(1+i) = (n-i+1)(i+n)
            => i+i**2 = ni-i**2+i+n**2-in+n
            => 2i**2 = n**2 + n
            => i = ((n**2 + n) / 2) ** (1/2)

"""


class Solution:
    def pivotIntegerBrute(self, n: int) -> int:
        if n == 1:
            return 1

        for i in range(2, n):
            if sum(range(1, i + 1)) == sum(range(i, n + 1)):
                return i
        return -1

    def pivotInteger(self, n: int) -> int:

        ans = ((n**2 + n) / 2) ** (1 / 2)
        return int(ans) if ans // 1 == ans else -1


cases = [
    (8, 6),
    (1, 1),
    (4, -1),
]

sol = Solution()
for (n, exp) in cases:
    assert (
        got := sol.pivotInteger(n)
    ) == exp, f"Failed case ({n}) - expecting ({exp}), got ({got})."
