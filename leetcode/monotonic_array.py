"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array
    nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
    Input: nums = [1,2,2,3]
    Output: true

Example 2:
    Input: nums = [6,5,4,4]
    Output: true

Example 3:
    Input: nums = [1,3,2]
    Output: false

Constraints:
    - 1 <= nums.length <= 10^5
    - -105 <= nums[i] <= 10^5

A:
    empty arr:
        not possible
    elems equal:
        that is cool
A:
    ?
D:
    mono_inc = true
    prev = -inf
    for x in nums:
        if x > prev:
            prev = x
        else:
            mono_inc = false
            break
    if mono_inc:
        return true

    mono_dec = true
    prev = inf
    for x in nums[::-1]:
        if x < prev:
            prev = x
        else:
            mono_dec = false
            break
    if mono_inc:
        return true

    return false

"""

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mono_inc = True
        prev = float('-inf')
        for x in nums:
            if x >= prev:
                prev = x
            else:
                mono_inc = False
                break
        if mono_inc:
            return True

        mono_dec = True
        prev = float('-inf')
        for x in nums[::-1]:
            if x >= prev:
                prev = x
            else:
                mono_dec = False
                break
        if mono_dec:
            return True

        return False


cases = [
    ([1, 2, 2, 3], True),
    ([6, 5, 4, 4], True),
    ([1, 3, 2], False),
    ([1], True),
    ([2, 1], True),
    ([1, 2], True),
    ([-1, 0, 1], True),
    ([1, 0, -1], True),
    ([1, -1, 0], False),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.isMonotonic(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
