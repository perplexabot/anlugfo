"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such
    that |nums[i] - nums[j]| == k.

The value of |x| is defined as:
    - x if x >= 0.
    - -x if x < 0.

Example 1:
    Input: nums = [1,2,2,1], k = 1
    Output: 4
    Explanation: The pairs with an absolute difference of 1 are:
    - [1,2,2,1]
    - [1,2,2,1]
    - [1,2,2,1]
    - [1,2,2,1]

Example 2:
    Input: nums = [1,3], k = 3
    Output: 0
    Explanation: There are no pairs with an absolute difference of 3.

Example 3:
    Input: nums = [3,2,1,5,4], k = 2
    Output: 3
    Explanation: The pairs with an absolute difference of 2 are:
    - [3,2,1,5,4]
    - [3,2,1,5,4]
    - [3,2,1,5,4]

Constraints:
    - 1 <= nums.length <= 200
    - 1 <= nums[i] <= 100
    - 1 <= k <= 99

A:
    array of size < 2:
       return 0
    k < 0:
        return 0
    negatives in nums:
        that's cool
"""

from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        if k < 0 or len(nums) < 2:
            return 0

        cnt = 0
        for indi, numi in enumerate(nums[:-1]):
            for numj in nums[indi + 1 :]:
                if abs(numi - numj) == k:
                    cnt += 1
        return cnt


cases = [
    ([1, 2, 2, 1], 1, 4),
    ([1, 3], 3, 0),
    ([3, 2, 1, 5, 4], 2, 3),
    ([1], 1, 0),
    ([1, 1], 0, 1),
    ([1, 1], 2, 0),
    ([1, 2, 3, 4, 5], 4, 1),
]

sol = Solution()
for nums, k, exp in cases:
    assert (
        got := sol.countKDifference(nums, k)
    ) == exp, f"Failed case ({nums}, {k}) - expecting ({exp}), got ({got})."
