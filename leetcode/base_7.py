"""
Given an integer num, return a string of its base 7 representation.

Example 1:
    Input: num = 100
    Output: "202"

Example 2:
    Input: num = -7
    Output: "-10"

Constraints:
    - -10**7 <= num <= 10**7

A:
    num is none int
        nope
    integer is negative
        yes, how to represent?
        prepend sign, base convert abs(nums)

A:

D:
    5325

    7**0 + 7**1 + 7**2 + 7**3 + 7**4 + 7**5
    1    + 7    + 49   + 343  + 2401 + 16807

    2*7**4 + 1*7**3 + 3*7**2  + 4*7**1 + 5*7**0
    4802   + 343    + 147     + 28     + 5      = 5325

    2        1        3         4        5

    5325b10 -> 21345b7

P:
    find largest x such that 7**x <= num

    total = 0
    base7 = []
    for i in {x..0}:
        coefficient = 1
        while total + (s:=(coefficient * 7**i)) <= num:
            total += s
            coefficient += 1
            base7.append(coefficient)
        if total == num:
            return ''.join(base7)

O:

T:
    (100, "202"),
    (-7, "-10"),
    (5325, "21345"),
    (0, "0"),
    (1, "1"),
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"

        x = 0
        while 7**x <= abs(num):
            x += 1

        total = 0
        newbase = []
        for i in reversed(range(abs(x))):
            subtotal = 0
            coefficient = 0
            while total + (s := (coefficient * 7**i)) <= abs(num):
                subtotal = s
                coefficient += 1
            total += subtotal
            newbase.append(str(coefficient - 1))

        return ''.join(newbase) if num >= 0 else '-' + ''.join(newbase)


cases = [
    (100, "202"),
    (5325, "21345"),
    (7, "10"),
    (-7, "-10"),
    (1, "1"),
    (0, "0"),
]

sol = Solution()
for num, exp in cases:
    assert (
        got := sol.convertToBase7(num)
    ) == exp, f"Failed case ({num}) - expecting ({exp}), got ({got})."
