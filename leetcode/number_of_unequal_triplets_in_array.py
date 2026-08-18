"""
You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k)
    that meet the following conditions:
    - 0 <= i < j < k < nums.length
    - nums[i], nums[j], and nums[k] are pairwise distinct.
        - In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].

Return the number of triplets that meet the conditions.

Example 1:
    Input: nums = [4,4,2,4,3]
    Output: 3
    Explanation: The following triplets meet the conditions:
    - (0, 2, 4) because 4 != 2 != 3
    - (1, 2, 4) because 4 != 2 != 3
    - (2, 3, 4) because 2 != 4 != 3
    Since there are 3 triplets, we return 3.
    Note that (2, 0, 4) is not a valid triplet because 2 > 0.

Example 2:
    Input: nums = [1,1,1,1,1]
    Output: 0
    Explanation: No triplets meet the conditions so we return 0.

Constraints:
    - 3 <= nums.length <= 100
    - 1 <= nums[i] <= 1000

A:
    all same
        return 0
    len(array) < 3
        return 0
    array has non positive ints?
        not possible

D:
    nums = [x0, ... xi]
    size(nums) = L
    how many "sequential trips"?
        first choice count = index_0
        second choice count = L - (index_0 + 1) 
        third choirce count = L - 
        


    

"""

from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if len(set([nums[i], nums[j], nums[k]])) == 3:
                        cnt += 1
        return cnt


sol = Solution()
cases = [([4, 4, 2, 4, 3], 3), ([1, 1, 1, 1, 1], 0), ([1, 2, 3], 1), ([3, 2, 1], 1)]

for case, exp in cases:
    assert (
        got := sol.unequalTriplets(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
