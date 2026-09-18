"""
You are given an integer array nums, an integer k, and an integer multiplier.
You need to perform k operations on nums. In each operation:
    - Find the minimum value x in nums. If there are multiple occurrences of the minimum value,
        select the one that appears first.
    - Replace the selected minimum value x with x * multiplier.

Return an integer array denoting the final state of nums after performing all k operations.

Example 1:
    Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
    Output: [8,4,6,5,6]
    Explanation:
    Operation	Result
    After operation 1	[2, 2, 3, 5, 6]
    After operation 2	[4, 2, 3, 5, 6]
    After operation 3	[4, 4, 3, 5, 6]
    After operation 4	[4, 4, 6, 5, 6]
    After operation 5	[8, 4, 6, 5, 6]

Example 2:
    Input: nums = [1,2], k = 3, multiplier = 4
    Output: [16,8]
    Explanation:
    Operation	Result
    After operation 1	[4, 2]
    After operation 2	[4, 8]
    After operation 3	[16, 8]

Constraints:
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100
    - 1 <= k <= 10
    - 1 <= multiplier <= 5

AADPOCT

A:
    empty arr
        return
    k = 0
        return
    non int multip
        not possible
    k < 0
        not possible
    all zeros
        return as is

A:
    in place or new?
        assume new ds

D:
    Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

    k = 0
        [2,2,3,5,6]
    k = 1
        [4,2,3,5,6]
    k = 2
        [4,4,3,5,6]
    k = 3
        [4,4,6,5,6]
    k = 4
        [8,4,6,5,6]

P:
    n = nums[:]
    if not n or not k:
        return n

    for i in range(k):
        min_val = inf
        min_ind = None
        for ind, j in enumerate(n):
            if j < min_val:
                min_val = j
                min_ind = ind
        n[min_ind] *= k
    return n

O:
    could use in place and not extra time and space constructing copy
    opting for new ds

T:
    ([], 10, 10, []),
    ([1], 10, 1, [1]),
    ([1], 3, 2, [8]),
    ([2,1,3,5,6], 5, 2 [8,4,6,5,6]),
    ([1,2],3,4, [16,8]),
"""


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        n = nums[:]

        if not n or not k:
            return n

        for i in range(k):
            min_val = float('inf')
            min_ind = None
            for ind, j in enumerate(n):
                if j < min_val:
                    min_val = j
                    min_ind = ind
            n[min_ind] *= multiplier
        return n


cases = [
    ([], 10, 10, []),
    ([1], 10, 1, [1]),
    ([1], 3, 2, [8]),
    ([2, 1, 3, 5, 6], 5, 2, [8, 4, 6, 5, 6]),
    ([1, 2], 3, 4, [16, 8]),
]

sol = Solution()
for nums, k, multiplier, expected in cases:
    assert (
        ans := sol.getFinalState(nums, k, multiplier)
    ) == expected, f"Woops, failed ({nums}, {k}, {multiplier}) - expecting {expected}, got {ans}."
