"""
You are given an integer array nums. In one operation, you can add or subtract 1 from any element of
    nums.
Return the minimum number of operations to make all elements of nums divisible by 3.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 3
    Explanation:
    All array elements can be made divisible by 3 using 3 operations:
        - Subtract 1 from 1.
        - Add 1 to 2.
        - Subtract 1 from 4.

Example 2:
    Input: nums = [3,6,9]
    Output: 0

Constraints:
    - 1 <= nums.length <= 50
    - 1 <= nums[i] <= 50

A:
    empty list
        return 0
    list of size 1
        check and return
    nums less than 0
        not possible
    none ints
        not possible

D:
    for i in nums:
        check left until 0 
        check right until hit
        tots = += min(left_path, right_path)
"""

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        tot = 0
        for i in nums:
            tmp0, tmp1 = i, i
            while (tmp0 % 3 != 0) and (tmp1 % 3 != 0):
                tmp0 -= 1
                tmp1 += 1
                tot += 1
        return tot


cases = [
    ([1, 2, 3, 4], 3),
    ([3, 6, 9], 0),
    ([], 0),
    ([3], 0),
    ([0], 0),
    ([99], 0),
    ([1, 1, 1], 3),
    ([13], 1),
]

sol = Solution()
for case, exp in cases:
    print(f'- Testing {case}')
    assert (
        got := sol.minimumOperations(case)
    ) == exp, f"Failed case ({case}) - got ({got}), expecting ({exp})."
