"""
The array-form of an integer num is an array representing its digits in left to right order.
    - For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the
    integer num + k.

Example 1:
    Input: num = [1,2,0,0], k = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234

Example 2:
    Input: num = [2,7,4], k = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455

Example 3:
    Input: num = [2,1,5], k = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

Constraints:
    1 <= num.length <= 10**4
    0 <= num[i] <= 9
    num does not contain any leading zeros except for the zero itself.
    1 <= k <= 10**4

A:
    empty arr:
        not possible
    leading zeros in arr:
        not possible

D:
    Input: num = [2,1,5], k = 806

    a = [5,1,2]
    b = [6,0,8]
    c = [1,2,0,1]
    return 1021


    a = 1234
    b = 4


"""

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        from itertools import zip_longest

        carry = 0
        ans = []
        for pair in zip_longest(reversed(num), reversed(list(str(k))), fillvalue='0'):
            a = sum(int(x) for x in pair) + carry
            carry, ones = divmod(a, 10)
            ans.append(ones)
        ans.append(carry)

        i = len(ans) - 1
        while ans[i] == 0:
            i -= 1

        ans = ans[: i + 1]

        return ans[::-1]


cases = [
    ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
    ([2, 7, 4], 181, [4, 5, 5]),
    ([2, 1, 5], 806, [1, 0, 2, 1]),
    ([1], 1, [2]),
    ([1, 9], 1, [2, 0]),
    ([9, 0], 1, [9, 1]),
]

sol = Solution()
for arr, k, exp in cases:
    assert (
        got := sol.addToArrayForm(arr, k)
    ) == exp, f"Failed case ({arr}, {k}) - expecting ({exp}), got ({got})."
