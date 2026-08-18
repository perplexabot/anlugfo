"""
Given an integer array nums and an integer k, modify the array in the following way:
    choose an index i and replace nums[i] with -nums[i].

You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

Example 1:
    Input: nums = [4,2,3], k = 1
    Output: 5
    Explanation: Choose index 1 and nums becomes [4,-2,3].

Example 2:
    Input: nums = [3,-1,0,2], k = 3
    Output: 6
    Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

Example 3:
    Input: nums = [2,-3,-1,5,-4], k = 2
    Output: 13
    Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

Constraints:
    1 <= nums.length <= 10**4
    -100 <= nums[i] <= 100
    1 <= k <= 10**4

A:
    nums empty -> not possible
    nums has 0 -> return sum

D:
    cnt = k
    sort(nums)
    for i in range(len(nums)):
        if k == 0:
            return sum(nums)

        if nums[i] < 0
            nums[i] *= -1

        if nums[i] == 0
            return sum(nums)

        if nums[i] > 0:
            break

    if cnt is even:
        return sum(nums)
    else:
        nums[i] *= -1
        return sum(nums)

===============================

get rid of as many negatives as possible
return if 0 exists
get rid of left over ks by toggling the smallest positive
"""

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        cnt = k
        nums.sort()

        for i in range(len(nums)):
            if cnt == 0 or nums[i] >= 0:
                break

            if nums[i] < 0:
                nums[i] *= -1
                cnt -= 1

        if 0 in nums or cnt <= 0:
            return sum(nums)

        if not cnt % 2:
            return sum(nums)
        else:
            smallest_elem_index = nums.index(min(nums))
            nums[smallest_elem_index] *= -1
            return sum(nums)


cases = [
    ([4, 2, 3], 1, 5),
    ([3, -1, 0, 2], 3, 6),
    ([2, -3, -1, 5, -4], 2, 13),
    ([-100], 1, 100),
    ([-100], 2, -100),
    ([-2, 5, 0, 2, -2], 3, 11),
]

sol = Solution()
for (nums, k, exp) in cases:
    assert (
        got := sol.largestSumAfterKNegations(nums, k)
    ) == exp, f"Failed case ({nums}, {k}) - expecting ({exp}), got ({got})."
