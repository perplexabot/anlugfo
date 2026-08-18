"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a
    function to search target in nums. If target exists, then return its index. Otherwise,
    return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 10**4
    -10**4 < nums[i], target < 10**4
    All the integers in nums are unique.
    nums is sorted in ascending order.

A:
    empty nums -> return -1
    target not found return -1
    list assumed to be ordered
    repeats in nums? no

D:
    l = 0
    r = len(nums)

    while True:
        if l >= r:
            return -1

        mid = (r - l) // 2

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l = 0
        r = len(nums) - 1
        while True:
            if l > r:
                return -1

            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1


cases = [
    #  0  1  2  3  4  5
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([-1, 0, 3, 5, 9, 12], 12, 5),
    ([1], 1, 0),
    ([1], 2, -1),
    ([1, 2], 1, 0),
    ([1, 2], 2, 1),
]

sol = Solution()
for (nums, target, exp) in cases:
    assert (
        got := sol.search(nums, target)
    ) == exp, f"Failed case ({nums}, {target}) - expecting ({exp}), got ({got})."
