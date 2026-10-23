"""
You are given two integers n and t. Return the smallest number greater than or equal to n such that
    the product of its digits is divisible by t.

Example 1:
    Input: n = 10, t = 2
    Output: 10
    Explanation:
    The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater
        than or equal to 10 that satisfies the condition.

Example 2:
    Input: n = 15, t = 3
    Output: 16
    Explanation:
    The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater
        than or equal to 15 that satisfies the condition.

Constraints:
    - 1 <= n <= 100
    - 1 <= t <= 10

A:
    n is zero
        no
    n is negative
        who cares
    t is negative?
        not possible

D:
    Input: n = 15, t = 3
    p = 5 % 3, nope
    p = 6 % 3, return 16

P:
    calculate digit sum of n
    check if divisible
    if yes return
    if not increment n and repeat

O:
    time complexity: O(n*i - t), s.t n*i is the lowest number to be divisible by t

T:
    10, 2, 10
    15, 3, 16
    11, 5, 14
    0, 50, 0
"""


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p = 1
            i = n
            while i:
                p *= i % 10
                i //= 10
            if p % t == 0:
                return n
            n += 1


sol = Solution()

cases = [
    (10, 2, 10),
    (15, 3, 16),
    (11, 5, 15),
]

for n, t, expected in cases:
    assert (
        got := sol.smallestNumber(n, t)
    ) == expected, f"Failed case ({n}, {t}) - expecting ({expected}), got ({got})."
