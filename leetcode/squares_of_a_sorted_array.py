"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 10**4
    -10**4 <= nums[i] <= 10**4
    nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an
    O(n) solution using a different approach?

A:
    empty list:
        return empty

    list of size 1:
        return square of list

    all negatives:
        return square of reverse list

    all positives:
        return square of list
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mid = None
        for ind, i in enumerate(nums):
            if i >= 0:
                mid = ind
                break

        if mid is None:
            poss = []
            negs = [x**2 for x in nums]
        elif mid == 0:
            poss = [x**2 for x in nums[::-1]]
            negs = []
        else:
            poss = [x**2 for x in nums[mid:][::-1]]
            negs = [x**2 for x in nums[:mid]]

        new = []
        while negs and poss:
            if negs[-1] < poss[-1]:
                new.append(negs.pop())
            else:
                new.append(poss.pop())

        while negs:
            new.append(negs.pop())
        while poss:
            new.append(poss.pop())

        return new


sol = Solution()

cases = [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([1], [1]),
    ([-1], [1]),
    ([-1, 0], [0, 1]),
    ([-5, -3, -2, -1], [1, 4, 9, 25]),
    ([1, 2, 3], [1, 4, 9]),
]

for nums, exp in cases:
    assert (
        got := sol.sortedSquares(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})"
