"""
You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another
number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form
    of an array.

Example 1:
    Input: nums = [1,2,2,4]
    Output: [2,3]

Example 2:
    Input: nums = [1,1]
    Output: [1,2]

Constraints:
    - 2 <= nums.length <= 10^4
    - 1 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = sorted(list(nums))

        p = 0
        missing_num = None
        repeated_num = None
        for n in l:
            if n - p == 0:
                repeated_num = n

            if n - p > 1:
                missing_num = p + 1
            p = n

        return (
            [repeated_num, missing_num]
            if missing_num is not None
            else [repeated_num, repeated_num + 1 if len(l) == 2 else max(l) + 1]
        )


cases = [([1, 2, 2, 4], [2, 3]), ([1, 1], [1, 2]), ([1, 5, 3, 2, 2, 7, 6, 4, 8, 9], [2, 10])]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.findErrorNums(case)
    ) == exp, f"Failed case ({case}) - got ({got}), expecting ({exp})."
