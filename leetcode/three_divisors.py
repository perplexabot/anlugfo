"""
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.

Example 1:
    Input: n = 2
    Output: false
    Explantion: 2 has only two divisors: 1 and 2.

Example 2:
    Input: n = 4
    Output: true
    Explantion: 4 has three divisors: 1, 2, and 4.

Constraints:
    - 1 <= n <= 10**4

A:
    n<=0
        no
    n is none int:
        no
    same factor twice
        makes no sense

D:
    4
        1, 2, 4 yes

P:
    iterate up until n/2 and check divisbility

O:
    ?

T:
    2, False
    4, True
    1, False
    3, False
    7, False
    9, True
    15, False
"""


class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 2
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                cnt += 1
        return cnt == 3


cases = [
    (2, False),
    (4, True),
    (1, False),
    (3, False),
    (7, False),
    (9, True),
    (15, False),
]

sol = Solution()
for n, expected in cases:
    assert (
        got := sol.isThree(n)
    ) == expected, f"Failed case ({n}) - got ({got}), expecting ({expected})."
