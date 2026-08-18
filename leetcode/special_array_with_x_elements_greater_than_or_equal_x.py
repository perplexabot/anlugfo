"""
You are given an array nums of non-negative integers. nums is considered special if there exists a
    number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special,
    the value for x is unique.

Example 1:
    Input: nums = [3,5]
    Output: 2
    Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
    Input: nums = [0,0]
    Output: -1
    Explanation: No numbers fit the criteria for x.
    If x = 0, there should be 0 numbers >= x, but there are 2.
    If x = 1, there should be 1 number >= x, but there are 0.
    If x = 2, there should be 2 numbers >= x, but there are 0.
    x cannot be greater since there are only 2 numbers in nums.

Example 3:
    Input: nums = [0,4,3,0,4]
    Output: 3
    Explanation: There are 3 values that are greater than or equal to 3.

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 1000

A:
    empty arr:
        not possible
    arr of size one:
        return 1 if arr[0] == 1 else -1

D:
    a = [3,5]
"""

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        from bisect import bisect_left

        nums.sort()
        for i in range(nums[-1] + 1):
            if len(nums) - bisect_left(nums, i) == i:
                return i
        return -1


cases = [
    ([3, 5], 2),
    ([0, 0], -1),
    ([0, 4, 3, 0, 4], 3),
    ([0], -1),
    ([1], 1),
    ([3, 4], 2),
    ([3, 3], 2),
    ([10], 1),
]

sol = Solution()
for nums, exp in cases:
    assert (
        got := sol.specialArray(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
