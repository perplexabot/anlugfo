"""
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are
    divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

Example 1:
    Input: n = 7
    Output: 21
    Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The
        sum of these numbers is 21.

Example 2:
    Input: n = 10
    Output: 40
    Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7,
        9, 10. The sum of these numbers is 40.

Example 3:
    Input: n = 9
    Output: 30
    Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9.
        The sum of these numbers is 30.

Constraints:
    1 <= n <= 10**3

A:
    n = 1
        return []
    n < 3
        return []

D:
    n = 7
        1 2 3 4 5 6 7
            x   x x x
    return 3 + 5 + 6 + 7 = 21
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(x for x in range(1, n + 1) if (x % 3 == 0 or x % 5 == 0 or x % 7 == 0))


cases = [(7, 21), (10, 40), (9, 30), (1, 0), (2, 0), (3, 3)]

sol = Solution()
for n, exp in cases:
    assert (
        got := sol.sumOfMultiples(n)
    ) == exp, f"Failed case ({n}) - expecting ({exp}), got ({got})."
