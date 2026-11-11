"""
You are given an integer array nums of even length. You have to split the array into two parts
    nums1 and nums2 such that:
    - nums1.length == nums2.length == nums.length / 2.
    - nums1 should contain distinct elements.
    - nums2 should also contain distinct elements.

Return true if it is possible to split the array, and false otherwise.

Example 1:
    Input: nums = [1,1,2,2,3,4]
    Output: true
    Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

Example 2:
    Input: nums = [1,1,1,1]
    Output: false
    Explanation: The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both
        nums1 and nums2 do not contain distinct elements. Therefore, we return false.

Constraints:
    - 1 <= nums.length <= 100
    - nums.length % 2 == 0
    - 1 <= nums[i] <= 100

A
    Size less than 2?
        q says even but constraints say size 1 is possible?
    do we have to check if nums is even
        no

D
    Input: nums = [1,1,1,1]
    1 cnt[1] = 1
    1 cnt[1] = 2
    1 cnt[1] = 3 break

P
    cnts[] = {0}
    for i in nums:
        cnts[i]++
        if cnts[i] > 2:
            return False
    return True

O:
    O(n) in time
    O(1) in spac

T:
    [1,1,2,2,3,4], true
    [1,1,1,1], false
    [1,2], true
    [2,1], true
    [2,2], true
    [1,2,3,4], true
    [1,2,4,4], true
    [1,4,4,4], false
    [4,1,4,4], false
"""

from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return not any(x > 2 for x in Counter(nums).values())


cases = [
    ([1, 1, 2, 2, 3, 4], True),
    ([1, 1, 1, 1], False),
    ([1, 2], True),
    ([2, 1], True),
    ([2, 2], True),
    ([1, 2, 3, 4], True),
    ([1, 2, 4, 4], True),
    ([1, 4, 4, 4], False),
    ([4, 1, 4, 4], False),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.isPossibleToSplit(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
