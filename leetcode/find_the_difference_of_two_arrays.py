"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
    - answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    - answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Example 1:
    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]
    Explanation:
    For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and
        nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
    For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and
        nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].

Example 2:
    Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    Output: [[3],[]]
    Explanation:
    For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3],
        their value is only included once and answer[0] = [3].
    Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Constraints:
    - 1 <= nums1.length, nums2.length <= 1000
    - -1000 <= nums1[i], nums2[i] <= 1000

A:
    include repeats in output?
        no
    empty list?
        not possible
    both the same,
        return two empty

D:
    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    s0 = (1,2,3), s1 = (2,4,6)
    return set diff
"""

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s0 = set(nums1)
        s1 = set(nums2)
        return [list(s0.difference(s1)), list(s1.difference(s0))]


sol = Solution()

cases = [
    ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
    ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
    ([1], [2], [[1], [2]]),
    ([1], [1], [[], []]),
    ([1, 2], [1, 2, 3], [[], [3]]),
    ([1, 2, 3], [1, 2], [[3], []]),
]

for nums1, nums2, exp in cases:
    got = sol.findDifference(nums1, nums2)
    for a in got:
        a.sort()
    for a in exp:
        a.sort()
    assert exp == got, f"Failed case ({nums1}, {nums2}) - expecting ({exp}), got ({got})."
