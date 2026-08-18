"""
Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with
    equal sum. Note that the two subarrays must begin at different indices.
Return true if these subarrays exist, and false otherwise.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [4,2,4]
    Output: true
    Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.

Example 2:
    Input: nums = [1,2,3,4,5]
    Output: false
    Explanation: No two subarrays of size 2 have the same sum.

Example 3:
    Input: nums = [0,0,0]
    Output: true
    Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
    Note that even though the subarrays have the same content, the two subarrays are considered
        different because they are in different positions in the original array.

Constraints:
    2 <= nums.length <= 1000
    -10**9 <= nums[i] <= 10**9

A:
    len(nums) < 3   ->  return false

D:
    Input: nums = [1,2,3,4,5]
    1 + 2 = 3
    2 + 3 = 5
    3 + 4 = 7
    4 + 5 = 9
    false

    Input: nums = [4,2,4]
    4 + 2 = 6
    2 + 4 = 6
    true
"""

from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        sums = set()
        for i in range(0, len(nums)):
            if len(nums[i : i + 2]) > 1:
                if sum(nums[i : i + 2]) in sums:
                    return True
                sums.add(sum(nums[i : i + 2]))
        return False


sol = Solution()

cases = [
    ([4, 2, 4], True),
    ([1, 2, 3, 4, 5], False),
    ([0, 0, 0], True),
    ([0, 0], False),
    ([1, 2, 3, 1, 0, 2], False),
    # 1 + 2 = 3
    # 2 + 3 = 5
    # 3 + 1 = 4
    # 1 + 0 = 1
    # 0 + 2 = 2
]

sol = Solution()
for (nums, exp) in cases:
    assert (
        got := sol.findSubarrays(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
