"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest
    number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both
    numbers.

Example 1:
    Input: nums = [2,5,6,9,10]
    Output: 2
    Explanation:
    The smallest number in nums is 2.
    The largest number in nums is 10.
    The greatest common divisor of 2 and 10 is 2.

Example 2:
    Input: nums = [7,5,6,8,3]
    Output: 1
    Explanation:
    The smallest number in nums is 3.
    The largest number in nums is 8.
    The greatest common divisor of 3 and 8 is 1.

Example 3:
    Input: nums = [3,3]
    Output: 3
    Explanation:
    The smallest number in nums is 3.
    The largest number in nums is 3.
    The greatest common divisor of 3 and 3 is 3.

Constraints:
    2 <= nums.length <= 1000
    1 <= nums[i] <= 1000

A:
    nums is empty -> not possible
    nums has 1 number -> not possible
    0 is min -> return max

D:
    Input: nums = [2,5,6,9,10]
    min = 2, max = 10
    gcd(2,10) -> gcd(2, 10 % 2) = gcd (2, 0) = 2

    Input: nums = [7,5,6,8,3]
    min = 2, max = 8
    gcd(2,8) -> gcd(3, 8 % 3) = gcd(3, 2) -> gcd(3 % 2, 2) -> gcd(1,2) -> gcd(1,2%1) = gcd(1,0) = 1

    Input: nums = [3,3]
    min = 3, max = 3, return 3
"""

from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n = min(nums)
        x = max(nums)

        def gcd(a, b):
            if not a:
                return b
            if not b:
                return a

            if a > b:
                return gcd(a % b, b)
            else:
                return gcd(a, b % a)

        if n == x:
            return n
        else:
            return gcd(n, x)


cases = [([2, 5, 6, 9, 10], 2), ([7, 5, 6, 8, 3], 1), ([3, 3], 3), ([0, 10], 10)]

sol = Solution()
for (nums, exp) in cases:
    assert (
        got := sol.findGCD(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
