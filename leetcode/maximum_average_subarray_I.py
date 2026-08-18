"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return
    this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000

Constraints:
    n == nums.length
    1 <= k <= n <= 10**5
    -10**4 <= nums[i] <= 10**4

A:
    empty nums -> not possible
    nums = 1 -> return nums
    k > len(nums) -> not possible
    k == len(nums) = return average of nums
    nums has negatives

D:
    k = 3
            0 1 2 3
    nums = [1,2,3,4]
    curr = k = 3
        ave = nums[curr-k:curr] = nums[0:3]
    curr += 1 = 4
        ave = nums[curr-k:curr] = nums[1:curr]



    max_ave = float(-inf)
    end = k - 1
    while end < len(nums):
        max_ave = max(max_ave, sum(nums[end
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ave = sum(nums[:k])
        curr_ave = max_ave
        end = k
        while end < len(nums):
            curr_ave = curr_ave - nums[end - k] + nums[end]
            max_ave = max(max_ave, curr_ave)
            end += 1
        return max_ave / k


cases = [
    ([1, 12, -5, -6, 50, 3], 4, 12.75000),
    ([5], 1, 5.00000),
    ([1, 10], 1, 10),
    ([1, 10], 2, 5.5),
    ([0, 0, 0], 3, 0),
    ([0, 0, 0], 2, 0),
    ([0, 0, 0], 1, 0),
]

sol = Solution()
for (nums, k, exp) in cases:
    assert (
        got := sol.findMaxAverage(nums, k)
    ) == exp, f"Failed case ({nums}, {k}) - expecting ({exp}), got ({got})."
