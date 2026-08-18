"""
You are given a 0-indexed integer array nums. Rearrange the values of nums according to the
    following rules:

    - Sort the values at odd indices of nums in non-increasing order.
        For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at
        odd indices 1 and 3 are sorted in non-increasing order.
    - Sort the values at even indices of nums in non-decreasing order.
        For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at
        even indices 0 and 2 are sorted in non-decreasing order.

Return the array formed after rearranging the values of nums.

Example 1:
    Input: nums = [4,1,2,3]
    Output: [2,3,4,1]
    Explanation:
    First, we sort the values present at odd indices (1 and 3) in non-increasing order.
    So, nums changes from [4,1,2,3] to [4,3,2,1].
    Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
    So, nums changes from [4,1,2,3] to [2,3,4,1].
    Thus, the array formed after rearranging the values is [2,3,4,1].

Example 2:
    Input: nums = [2,1]
    Output: [2,1]
    Explanation:
    Since there is exactly one odd index and one even index, no rearrangement of values takes place.
    The resultant array formed is [2,1], which is the same as the initial array.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100

A:
    nums = [], return []
    nums = [1] return [1]
    nums = [1,2], return [1,2]

A:?

D:
    Input: nums = [4,1,2,3]
    o = [1,3] -> [3,1]
    e = [4,2] -> [2,4]
    while e:
        final.append(e.pop())
        if o:
            final.append(o.pop())
    return final
"""

from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        if len(nums) < 3:
            return nums

        e = [x for ind, x in enumerate(nums) if not ind % 2]
        o = [x for ind, x in enumerate(nums) if ind % 2]

        e.sort(reverse=True)
        o.sort()

        final = []
        while e:
            final.append(e.pop())
            if o:
                final.append(o.pop())
        return final


cases = [
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([2, 1], [2, 1]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([5, 9666, 32], [5, 9666, 32]),
    ([32, 12222, 4], [4, 12222, 32]),
    ([4, 1, 2, 3], [2, 3, 4, 1]),
]

sol = Solution()
for (nums, exp) in cases:
    assert (
        got := sol.sortEvenOdd(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
