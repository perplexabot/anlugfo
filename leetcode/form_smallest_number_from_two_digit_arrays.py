"""
Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least
    one digit from each array.

Example 1:
    Input: nums1 = [4,1,3], nums2 = [5,7]
    Output: 15
    Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can
        be proven that 15 is the smallest number we can have.

Example 2:
    Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
    Output: 3
    Explanation: The number 3 contains the digit 3 which exists in both arrays.

Constraints:
    1 <= nums1.length, nums2.length <= 9
    1 <= nums1[i], nums2[i] <= 9
    All digits in each array are unique.

A:
    0 in array?
        no
"""

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        a1 = set(nums1)
        a2 = set(nums2)
        a = min(a1.intersection(a2), default=None)

        if a:
            return a

        m1 = min(a1)
        m2 = min(a2)
        if m1 < m2:
            return int(str(m1) + str(m2))
        else:
            return int(str(m2) + str(m1))


cases = [
    ([4, 1, 3], [5, 7], 15),
    ([3, 5, 2, 6], [3, 1, 7], 3),
    ([1], [1], 1),
    ([1, 2], [2, 1], 1),
    ([1, 2], [3, 4], 13),
    ([10, 15], [11, 23], 1011),
]

sol = Solution()
for n1, n2, exp in cases:
    assert (
        got := sol.minNumber(n1, n2)
    ) == exp, f"Failed case ({n1}, {n2}) - expecting ({exp}), got ({got})"
