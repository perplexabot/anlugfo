"""
Given an array nums, you can perform the following operation any number of times:
    - Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist,
        choose the leftmost one.
    - Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous
    element (if it exists).

Example 1:
    Input: nums = [5,2,3,1]
    Output: 2
    Explanation:
        The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
        The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
    The array nums became non-decreasing in two operations.

Example 2:
    Input: nums = [1,2,2]
    Output: 0
    Explanation:
    The array nums is already sorted.

Constraints:
    - 1 <= nums.length <= 50
    - -1000 <= nums[i] <= 1000

A:
    empty arr
        no
    arr of size 1
        return 0
    arr of size 2
        if arr[1] > arr[0], return 0 else

D:
                   0 1 2 3
    Input: nums = [5,2,3,1], not sorted
    5 + 2 = 7
    2 + 3 = 5
    3 + 1 = 4 min

    nums = [5,2,4], not sorted
    5 + 2 = 7
    2 + 4 = 6 min

    nums = [5,6], sorted
    return 2

P:
    n = nums[:]
    while True:
        sums = {}
        sorted = True
        for i in range(0,len(n)-1):
            if n[i] > n[i+1]:
                sorted = False

            sums[i] = sum(n[i:i+1])

        if not sorted:
            find smallest pair
            modify n
        else:
            break

"""

from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = nums[:]
        cnt = 0
        while True:
            sums = {}
            isSorted = True
            for i in range(len(n) - 1):
                isSorted = False if n[i] > n[i+1] else isSorted
                sums[i] = sum(n[i : i + 2])

            if not isSorted:
                cnt += 1
                minpair_index = min(sums.items(), key=lambda x: x[1])[0]
                n = (
                    n[:minpair_index]
                    + [sum(n[minpair_index : minpair_index + 2])]
                    + n[minpair_index + 2 :]
                )
            else:
                return cnt
        return -1


sol = Solution()

cases = [
    ([5, 2, 3, 1], 2),
    ([1, 2, 2], 0),
    ([1], 0),
    ([1, 2], 0),
    ([1, 2, 3], 0),
    ([5, 0, 0, 1], 3),
    ([5, 3], 1),
    ([1, 1], 0),
]

for nums, exp in cases:
    assert (
        got := sol.minimumPairRemoval(nums)
    ) == exp, f"Failed case ({nums}) - expecting ({exp}), got ({got})."
