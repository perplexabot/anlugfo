"""
You are given an integer array nums. Transform nums by performing the following operations in the
    exact order specified:
    - Replace each even number with 0.
    - Replace each odd numbers with 1.
    - Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.

Example 1:
    Input: nums = [4,3,2,1]
    Output: [0,0,1,1]
    Explanation:
        Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1.
        Now, nums = [0, 1, 0, 1]. After sorting nums in non-descending order, nums = [0, 0, 1, 1].

Example 2:
    Input: nums = [1,5,1,4,2]
    Output: [0,0,1,1,1]
    Explanation:
        Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1.
        Now, nums = [1, 1, 1, 0, 0]. After sorting nums in non-descending order,
        nums = [0, 0, 1, 1, 1].

Constraints:
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 1000

AADPOCT

A:
    empty nums:
        return []
    nums of size 1:
        nothing special
    only odds:
        return 1s
    only evens:
        return 0s
"""

from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for ind, val in enumerate(nums):
            nums[ind] = 0 if val % 2 == 0 else 1
        nums.sort()
        return nums


cases = [
    ([4, 3, 2, 1], [0, 0, 1, 1]),
    ([1, 5, 1, 4, 2], [0, 0, 1, 1, 1]),
    ([], []),
    ([12], [0]),
    ([13], [1]),
    ([0, 0], [0, 0]),
    ([1, 1], [1, 1]),
    ([1, 2, 3], [0, 1, 1]),
    ([4, 5, 6], [0, 0, 1]),
]

sol = Solution()
for nums, exp in cases:
    assert (
        got := sol.transformArray(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
