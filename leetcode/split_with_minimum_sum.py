"""
Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
    - The concatenation of num1 and num2 is a permutation of num.
        In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal
            to the number of occurrences of that digit in num.
    - num1 and num2 can contain leading zeros.

Return the minimum possible sum of num1 and num2.

Notes:

    - It is guaranteed that num does not contain any leading zeros.
    - The order of occurrence of the digits in num1 and num2 may differ from the order of
        occurrence of num.

Example 1:
    Input: num = 4325
    Output: 59
    Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can
        prove that 59 is indeed the minimal possible sum.

Example 2:
    Input: num = 687
    Output: 75
    Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal
        sum of 75.

Constraints:
    - 10 <= num <= 10^9

A:
    one digit number
        not possible
    return with leading zeros
        ok
    negative number
        not possible
A:
    ?
D:
    Input: num = 4325 -> "2345"
    n0 = 2, n1 = 3, num = "45"
    n0 = 24, n1 = 35, num = ""
    return 24 + 35 = 59
P:
    Input: num = 4325 -> "2345"
    toggle = 0
    num0, num1 = [], []
    s = sorted(int(num))
    for i in s:
        if not toggle:
            num0.append(i)
        else:
            num1.append(i)
        toggle = !toggle
O:

C:

T:
"""


class Solution:
    def splitNum(self, num: int) -> int:
        snum = sorted(str(num))
        num0, num1 = [], []
        toggle = True

        for i in snum:
            if not toggle:
                num0.append(i)
            else:
                num1.append(i)
            toggle = not toggle

        return int(''.join(num0)) + int(''.join(num1))


cases = [(4325, 59), (687, 75), (10, 1), (11, 2), (100, 1)]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.splitNum(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
