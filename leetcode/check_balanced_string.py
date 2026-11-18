"""
You are given a string num consisting of only digits. A string of digits is called balanced if the
    sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.

Example 1:
    Input: num = "1234"
    Output: false
    Explanation:
        The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
        Since 4 is not equal to 6, num is not balanced.

Example 2:
    Input: num = "24123"
    Output: true
    Explanation:
        The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
        Since both are equal the num is balanced.

Constraints:
    - 2 <= num.length <= 100
    - num consists of digits only

A:
    empty num?
        no
    1 size
        no
    2 size?
        nums[0] == nums[1]
    none ints
        no
    odd number of nums
        so what
D:
    1234
    1 + 3 != 4 + 2

P:
    sum_even_indices == sum_odd_indices

O:
    O(n) in time O(1) in space

T:
    "1234" false
    "24123" true
    "00" true
    "000" true
"""


class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(int(num[i]) for i in range(0, len(num), 2)) == sum(
            int(num[i]) for i in range(1, len(num), 2)
        )


cases = [
    ("1234", False),
    ("24123", True),
    ("00", True),
    ("000", True),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.isBalanced(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
