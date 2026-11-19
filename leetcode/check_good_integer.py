"""
You are given a positive integer n.
Let digitSum be the sum of the digits of n, and let squareSum be the sum of the squares of the
    digits of n.
An integer is called good if squareSum - digitSum >= 50.
Return true if n is good. Otherwise, return false.

Example 1:
    Input: n = 1000
    Output: false
    Explanation:
        The digits of 1000 are 1, 0, 0, and 0.
        The digitSum is 1 + 0 + 0 + 0 = 1.
        The squareSum is 12 + 02 + 02 + 02 = 1.
        The squareSum - digitSum is 1 - 1 = 0. As 0 is not greater than or equal to 50, the output
            is false.

Example 2:
    Input: n = 19
    Output: true
    Explanation:
        The digits of 19 are 1 and 9.
        The digitSum is 1 + 9 = 10.
        The squareSum is 12 + 92 = 1 + 81 = 82.
        The squareSum - digitSum is 82 - 10 = 72. As 72 is greater than or equal to 50, the output
            is true.

Constraints:
    - 1 <= n <= 10**9

A:
    negatives
        no

D:
    12
    (4 + 1) - (1 + 2) >=? 50
    return false

P:
    s0 = 0
    s1 = 0
    while (n)
        d = n % 10
        n /= 10
        s0 += d
        s1 += d**2
    return s1 - s0 >= 50

O:
    O(d) in time (where d is digits in n)
    O(1) in spac

T:
    1000 false
    19  true
    8 true
    7 false
    12 false
    1 false
    11 false
    111 false
"""


class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s0 = 0
        s1 = 0
        while n:
            d = n % 10
            n //= 10
            s0 += d
            s1 += d**2
        return s1 - s0 >= 50


cases = [
    (1000, False),
    (19, True),
    (8, True),
    (7, False),
    (12, False),
    (1, False),
    (11, False),
    (111, False),
    (37, False),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.checkGoodInteger(case)
    ) == expected, f"WOoOpseeeee! Failed ({case}) - expecting ({expected}), got ({got})."
