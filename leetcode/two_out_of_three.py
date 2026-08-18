"""
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the
    values that are present in at least two out of the three arrays. You may return the values
    in any order.

Example 1:
    Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
    Output: [3,2]
    Explanation: The values that are present in at least two arrays are:
    - 3, in all three arrays.
    - 2, in nums1 and nums2.

Example 2:
    Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
    Output: [2,3,1]
    Explanation: The values that are present in at least two arrays are:
    - 2, in nums2 and nums3.
    - 3, in nums1 and nums2.
    - 1, in nums1 and nums3.

Example 3:
    Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
    Output: []
    Explanation: No value is present in at least two arrays.

Constraints:
    - 1 <= nums1.length, nums2.length, nums3.length <= 100
    - 1 <= nums1[i], nums2[j], nums3[k] <= 100

A:
    one of the nums is empty
        no prob
    all empty
        no prob
"""

from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d = []
        for i in range(101):
            bools = [1 for aList in [nums1, nums2, nums3] if i in aList]
            if sum(bools) > 1:
                d.append(i)
        return d


cases = [
    ([1, 1, 3, 2], [2, 3], [3], set([3, 2])),
    ([3, 1], [2, 3], [1, 2], set([2, 3, 1])),
    ([1, 2, 2], [4, 3, 3], [5], set([])),
]

sol = Solution()
for nums1, nums2, nums3, exp in cases:
    assert (
        got := set(sol.twoOutOfThree(nums1, nums2, nums3))
    ) == exp, f"Failed case ({nums1}, {nums2}, {nums3}) - expecting ({exp}), got ({got})."
