"""You are given an array of integers nums.

   Return the length of the longest of nums which is either or.

Example 1:
    Input: nums = [1,4,3,3,2]
    Output: 2
    Explanation:
        The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
        The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
        Hence, we return 2.

Example 2:
    Input: nums = [3,3,3,3]
    Output: 1
    Explanation:
        The strictly increasing subarrays of nums are [3], [3], [3], and [3].
        The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
        Hence, we return 1.

Example 3:
    Input: nums = [3,2,1]
    Output: 3
    Explanation:
        The strictly increasing subarrays of nums are [3], [2], and [1].
        The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
        Hence, we return 3.

Constraints:
    - 1 <= nums.length <= 50
    - 1 <= nums[i] <= 50
"""

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        gmax = 1
        lcnt, rcnt = 1, 1
        for i, _ in enumerate(nums[:-1]):
            if nums[i + 1] > nums[i]:
                lcnt += 1
            else:
                gmax = max(lcnt, gmax)
                lcnt = 1

            if nums[i + 1] < nums[i]:
                rcnt += 1
            else:
                gmax = max(rcnt, gmax)
                rcnt = 1
        return max([gmax, lcnt, rcnt])


sol = Solution()

cases = [
    ([1, 4, 3, 3, 2], 2),
    ([3, 3, 3, 3], 1),
    ([3, 2, 1], 3),
    ([], 0),
    ([1], 1),
    ([-1, -2, -3], 3),
    ([1, 1, 1, 2], 2),
    ([2, 2, 2, 1], 2),
    ([1, 2, 2, 2], 2),
    ([2, 1, 1, 1], 2),
]

for nums, exp in cases:
    assert (
        got := sol.longestMonotonicSubarray(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
