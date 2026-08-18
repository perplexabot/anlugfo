"""
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number
    in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
    Input: nums = [3,6,1,0]
    Output: 1
    Explanation: 6 is the largest integer.
    For every other number in the array x, 6 is at least twice as big as x.
    The index of value 6 is 1, so we return 1.

Example 2:
    Input: nums = [1,2,3,4]
    Output: -1
    Explanation: 4 is less than twice the value of 3, so we return -1.

Constraints:
    2 <= nums.length <= 50
    0 <= nums[i] <= 100
    The largest element in nums is unique.

A:
    empty nums -> not possible
    negative in nums -> not possible
    repeats possible -> not for largest elem tho

D:
    min0 = -1
    min1 = -2

    for num in nums:
        if min1 > min0:
            min0 = max(min0, num)
        else:
            min1 = max(min1, num)
    return min(min0,min1) * 2 =< max(min0,min1)
"""

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        min0 = -1
        min1 = -2

        for num in nums:
            if min1 > min0:
                min0 = max(min0, num)
            else:
                min1 = max(min1, num)

        return nums.index(max(min1, min0)) if min(min0, min1) * 2 <= max(min0, min1) else -1


cases = [
    ([3, 6, 1, 0], 1),
    ([1, 2, 3, 4], -1),
    ([1, 4], 1),
    ([1, 2], 1),
    ([1, 1], -1),
    ([3, 2], -1),
    ([0, 0, 0, 1], 3),
]

sol = Solution()
for (nums, exp) in cases:
    assert (
        got := sol.dominantIndex(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
