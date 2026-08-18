"""
Given two non-negative integers, num1 and num2 represented as string, return the sum
    of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as
    BigInteger). You must also not convert the inputs to integers directly.

Example 1:
    Input: num1 = "11", num2 = "123"
    Output: "134"

Example 2:
    Input: num1 = "456", num2 = "77"
    Output: "533"

Example 3:
    Input: num1 = "0", num2 = "0"
    Output: "0"

Constraints:
    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.

A:
    leading zeros -> no
    empty string -> no

D:
    num1: "43228"
    num2: "543"

    ans = []
    carry = 0
    "43228"
    "00543"
    ------
    8+3, ans.append('1'), carry = '1'
    2+4, ans.append('7'), carry = '0'
    .
    .
    .
    if carry exists, ans.append(carry)


"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        from itertools import zip_longest

        carry = 0
        final = []
        for (a, b) in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
            z = int(a) + int(b) + carry
            final.append(str(z % 10))
            carry = z // 10
        if carry:
            final.append(str(carry))

        return ''.join(reversed(final))


cases = [
    ("11", "123", "134"),
    ("456", "77", "533"),
    ("0", "0", "0"),
]

sol = Solution()
for (a, b, exp) in cases:
    assert (
        got := sol.addStrings(a, b)
    ) == exp, f"Failed case ({a} + {b}) - expecting ({exp}), got ({got})."
