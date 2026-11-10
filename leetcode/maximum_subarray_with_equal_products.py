"""
You are given an array of positive integers nums.
An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
    - prod(arr) is the product of all elements of arr.
    - gcd(arr) is the GCD of all elements of arr.
    - lcm(arr) is the LCM of all elements of arr.

Return the length of the longest product equivalent subarray of nums.

Example 1:
    Input: nums = [1, 2, 1, 2, 1, 1, 1]
    Output: 5
    Explanation:
        The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2,
        gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:
    Input: nums = [2, 3, 4, 5, 6]
    Output: 3
    Explanation:
        The longest product equivalent subarray is [3, 4, 5].

Example 3:
    Input: nums = [1, 2, 3, 1, 4, 5, 1]
    Output: 5

Constraints:
    - 2 <= nums.length <= 100
    - 1 <= nums[i] <= 10

A
    is a subarray that is product equivalent always present?
    is arr always greater than size 1?
    can a number be 0?

D:
                   0  1  2  3  4
    Input: nums = [2, 3, 4, 5, 6]
                  |             | 720 =? 60 * 1
                  |          |    120 =? 60 * 1
                    |           | 360 =? 60 * 1
                  |       |       24  =? 12 * 1
                    |        |    60  =? 60 * 1 return 3

P:
    while winsize > 1:
        for i in range(len(nums) - winsize + 1):
            if prod(nums[i:i+winsize]) == gcm(nums[i:i+winsize]) + lcm(nums[i:i+winsize])
                return winsize


O:
    Anyway to do this O(n)?
        ?
    rather than calculating subarray product for each shift div and mult removed and added elems
    might be possible to optimize gcd and lcm
        using python tho

T
    ([1, 2, 1, 2, 1, 1, 1], 5),
    ([2, 3, 4, 5, 6], 3),
    ([1, 2, 3, 1, 4, 5, 1], 5),
    ([1, 1], 2),
    ([1, 2], 2),
"""

import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        win = len(nums)
        while win:
            for start in range(len(nums) - win + 1):
                if math.prod(nums[start: start + win]) == math.gcd(
                    *nums[start: start + win]
                ) * math.lcm(*nums[start: start + win]):
                    return win
            win -= 1


cases = [
    ([1, 2, 1, 2, 1, 1, 1], 5),
    ([2, 3, 4, 5, 6], 3),
    ([1, 2, 3, 1, 4, 5, 1], 5),
    ([1, 1], 2),
    ([1, 2], 2),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.maxLength(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
