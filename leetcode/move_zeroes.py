"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
    of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Constraints:
    - 1 <= nums.length <= 10**4
    - -2**31 <= nums[i] <= 2**31 - 1

Follow up: Could you minimize the total number of operations done?

A:
    empty list
        return
    list with no zero
        return
    list with zero at front
        move to end
    list with zeros at the end
        return
    list of size 1
        return
    return same list or new list?
        same list

D:
    Input: nums = [0,1,0,3,12]
    left = 0
    right = 12
        swap

    left = 1
    right = 3
    left = 0
    swap

    done
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            left = 0
            while True:

                while left < len(nums) and nums[left] != 0:
                    left += 1

                right = left + 1
                while right < len(nums) and nums[right] == 0:
                    right += 1

                if left > right or right >= len(nums):
                    break
                else:
                    nums[left], nums[right] = nums[right], nums[left]


sol = Solution()

cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([], []),
    ([0, 0], [0, 0]),
    ([1, 0], [1, 0]),
    ([0, 1], [1, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 0], [1, 2, 0]),
    ([0, 1, 2], [1, 2, 0]),
    ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]),
]

for case, exp in cases:
    sol.moveZeroes(case)
    assert case == exp, f'Failed case ({case}) - expecting ({exp}), got ({case}).'
