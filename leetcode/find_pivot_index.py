"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is
    equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements
    to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.

Example 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
    - 1 <= nums.length <= 10^4
    - -1000 <= nums[i] <= 1000

A:
    empty arr:
        return -1
    arr size of 1
        if elem == 0 return 0
    none positive ints?
        possible

D:
            0 1 2 3 4 5
    nums = [1,7,3,6,5,6]

    piv = 0
    left = 0
    right = sum(nums) - nums[piv] = 27

    left != right, left += nums[piv] = 1, piv += 1 = 1, right -= nums[piv] = 20
    left != right, left += nums[piv] = 8, piv += 1 = 2, right -= nums[piv] = 17
    left != right, left += nums[piv] = 11, piv += 1 = 3, right -= nums[piv] = 11
    left == right, return piv
    
P:
    piv = 0
    left = 0
    right = sum(nums) - nums[piv]
    while True
        if left == right:
            return piv

        if piv == len(nums):
            return -1
        
        left += nums[piv]
        piv += 1
        right -= nums[piv]


        
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        piv = 0
        left = 0
        right = sum(nums) - nums[0]
        while True:
            if left == right:
                return piv

            left += nums[piv]
            piv += 1

            if piv >= len(nums):
                return -1

            right -= nums[piv]


cases = [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),
    ([0], 0),
    ([0, 0, 0], 0),
    ([1, 0, 1], 1),
    ([-1, 0, -1], 1),
    ([-1, 0, -1, -1, 1], 1),
    ([1, 2, 3], -1),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.pivotIndex(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
