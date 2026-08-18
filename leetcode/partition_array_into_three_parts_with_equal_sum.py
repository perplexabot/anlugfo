"""
Given an array of integers arr, return true if we can partition the array into three non-empty parts
    with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... +
    arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... +
    arr[arr.length - 1])

Example 1:
    Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    Output: true
    Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
    Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
    Output: false

Example 3:
    Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
    Output: true
    Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Constraints:
    3 <= arr.length <= 5 * 104
    -10**4 <= arr[i] <= 10**4

A:
    can a partition be of size 0?
        no

D:
     0 1 2  3 4  5 6 7 8 9 10
    [0,2,1,-6,6,-7,9,1,2,0,1]

    i = 1
    2 * sum(0) ?= sum([2,1,-6,6,-7,9,1,2,0,1])

    i = 2
    2 * sum([0,2]) ?= sum([1,-6,6,-7,9,1,2,0,1])

    i = 3
    2 * sum([0,2,1]) ?= sum([-6,6,-7,9,1,2,0,1])
        i = 4
        sum([-6]) ?= sum([6,-7,9,1,2,0,1])
        i = 5
        sum([-6,6]) ?= sum([-7,9,1,2,0,1])
        i = 6
        sum([-6,6,-7]) ?= sum([9,1,2,0,1])
        i = 7
        sum([-6,6,-7,9]) ?= sum([1,2,0,1])
        i = 8
        sum([-6,6,-7,9,1]) ?= sum([2,0,1])
    return true

P:
    for i in range(1,len(arr) - 1):
        if 2 * sum(arr[:i]) == sum(arr[i:]):
            for j in range(i+1, len(arr):
                if sum(arr[i:j]) == sum(arr[j:]):
                    return True
    return False
"""
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        for i in range(1, len(arr) - 1):
            if 2 * sum(arr[:i]) == sum(arr[i:]):
                for j in range(i + 1, len(arr)):
                    if sum(arr[i:j]) == sum(arr[j:]):
                        return True
        return False


cases = [
    ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True),
    ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
    ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], True),
    ([1, 1, 1], True),
    ([1, 2, 3], False),
    ([0, -5, 5, 7, -7], True),
]

sol = Solution()
for arr, exp in cases:
    assert (
        got := sol.canThreePartsEqualSum(arr)
    ) == exp, f"Failed case ({arr}) - expecting ({exp}), got ({got})."
