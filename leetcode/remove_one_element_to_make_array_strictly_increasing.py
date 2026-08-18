"""
Given a 0-indexed integer array nums, return true if it can be made strictly increasing after 
    removing exactly one element, or false otherwise. If the array is already strictly 
    increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each 
    index (1 <= i < nums.length).

 

Example 1:
    Input: nums = [1,2,10,5,7]
    Output: true
    Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
    [1,2,5,7] is strictly increasing, so return true.

Example 2:
    Input: nums = [2,3,1,2]
    Output: false
    Explanation:
    [3,1,2] is the result of removing the element at index 0.
    [2,1,2] is the result of removing the element at index 1.
    [2,3,2] is the result of removing the element at index 2.
    [2,3,1] is the result of removing the element at index 3.
    No resulting array is strictly increasing, so return false.

Example 3:
    Input: nums = [1,1,1]
    Output: false
    Explanation: The result of removing any element is [1,1].
    [1,1] is not strictly increasing, so return false.

Constraints:
    2 <= nums.length <= 1000
    1 <= nums[i] <= 1000

A:
    arr of size < 2: return True
    arr contains other than ints -> not possible

D:
    if len arr < 2:
        return true

    i = 1
    hits = false
    while i < len(arr):
        if arr[i] <= arr[i-1] and not hits:
            hits = true
        elif arr[i] <= arr[i-1] and hits:
            return false
    return true
"""

from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        i = 1
        cnts = 0
        while i < len(nums):
            if nums[i] <= nums[i - 1]:
                cnts += 1
                inds = i - 1
            i += 1

        if cnts == 0:
            return True

        print(inds)
        if cnts == 1:
            if inds == 0 or inds == len(nums) - 2:
                return True
            if nums[inds + 1] > nums[inds - 1] or (
                inds + 2 < len(nums) and nums[inds] < nums[inds + 2]
            ):
                return True

        return False


cases = [
    ([1, 2, 10, 5, 7], True),
    ([2, 3, 1, 2], False),
    ([1, 1, 1], False),
    ([1], True),
    ([], True),
    ([2, 1], True),
    ([1, 2], True),
    ([3, 2, 1], False),
    ([105, 924, 32, 968], True),
    ([100, 21, 100], True),
    ([512, 867, 904, 997, 403], True),
]

sol = Solution()
for (nums, exp) in cases:
    assert (
        got := sol.canBeIncreasing(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
