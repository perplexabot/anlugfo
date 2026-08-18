"""
Given an integer array nums, find three numbers whose product is maximum and return the
    maximum product.

Example 1:
    Input: nums = [1,2,3]
    Output: 6

Example 2:
    Input: nums = [1,2,3,4]
    Output: 24

Example 3:
    Input: nums = [-1,-2,-3]
    Output: -6

Constraints:
    - 3 <= nums.length <= 104
    - -1000 <= nums[i] <= 1000

A:
    len(nums) == 3:
        return prod of nums
    len(nums) < 3:
        not possible
A:
    repeated numbers?
        possible

D:
    [1,2,3,4]
    mins = [1,2], pmins = 2*1 = 2
    maxs = [3,4], pmaxs = 3*4 = 12

    pmaxs >= pmins
        nums[-3] = 2 > nums[0] = 1:
            return pmaxs * 2 = 24

    [-1,-2,0,1,2]
    mins = [-1,-2], pmins = 2
    maxs = [1,2], pmaxs = 2

    pmaxs >= pmins
        nums[-3] = 0 > nums[0] = -1
            return pmaxs * 0 = 0

    [-3,-2,-1]
    mins = [-3,-2], pmins = -3*-2 = 6
    maxs = [-2,-1], pmaxs = -2*-1 = 2

    pmins > pmaxs:
        nums[2] == -1 > nums[-1] == -1
            return pmins * -1 = -6

    WRONG!

P:
    sort nums
    get smallest two nums
    get highest two nums
    see which product is highest and use
    then find third highest number
"""

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        from functools import reduce

        nums.sort()
        mins = nums[:2]
        maxs = nums[-2:]

        pmins = reduce(lambda x, y: x * y, mins)
        pmaxs = reduce(lambda x, y: x * y, maxs)

        possibles = set()
        possibles.add(pmins * nums[2])
        possibles.add(pmins * nums[-1])
        possibles.add(pmaxs * nums[-3])
        possibles.add(pmaxs * nums[0])
        return max(possibles)


cases = [
    ([1, 2, 3], 6),
    ([1, 2, 3, 4], 24),
    ([-1, -2, -3], -6),
    ([-1, -2, 0, 1, 2], 4),
    ([-8, -7, -2, 10, 20], 1120),
]

sol = Solution()
for nums, exp in cases:
    assert (
        got := sol.maximumProduct(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
