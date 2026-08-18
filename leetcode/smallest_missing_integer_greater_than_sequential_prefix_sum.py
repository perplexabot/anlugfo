"""
You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In
    particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to
    the sum of the longest sequential prefix.

Example 1:
    Input: nums = [1,2,3,2,5]
    Output: 6
    Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not
        in the array, therefore 6 is the smallest missing integer greater than or equal to
        the sum of the longest sequential prefix.

Example 2:
    Input: nums = [3,4,5,1,12,14,13]
    Output: 15
    Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13,
        and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing
        integer greater than or equal to the sum of the longest sequential prefix.

Constraints:
    - 1 <= nums.length <= 50
    - 1 <= nums[i] <= 50

A:
    empty array
        not possible
    size 1:
        return element + 1
    sorted?
        no
    if all sequential
        return sum
    ints less than 1
        not possible

D:
            0 1 2 3 4  5  6
    nums = [3,4,5,1,12,14,13]

    # len(nums) > 1

    # find longest prefix seq
    j = 1 (nums[j] - nums[j-1] == 1) continue
    j = 2 (nums[j] - nums[j-1] == 1) continue
    j = 3 (nums[j] - nums[j-1] == -4) stop, longest prefix seq is nums[:3]

    # find sum
    s = sum([nums[:3]) = 12
        
    # get x
    s (12) in nums, yes
    s+=1 (13) in nums, yes
    s+=1 (14) in nums, yes
    s+=1 (15) in nums, no
    return 15

P:
    if len(nums) < 2:
        return nums[0] + 1

    j = 1
    while j < len(nums):
        if nums[j] - nums[j-1] != 1:
            break

    s = sum(nums[:j])

    while True:
        if s not in nums:
            return s
        s += 1

"""

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0] + 1

        j = 1
        while j < len(nums):
            if nums[j] - nums[j - 1] != 1:
                break
            j += 1

        s = sum(nums[:j])

        n = set(nums)
        while True:
            if s not in n:
                return s
            s += 1


cases = [
    ([1, 2, 3, 2, 5], 6),
    ([3, 4, 5, 1, 12, 14, 13], 15),
    ([1], 2),
    ([1, 3], 2),
    ([3, 2, 1], 4),
    ([1, 2, 3], 6),
]

sol = Solution()
for nums, exp in cases:
    assert (
        got := sol.missingInteger(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
