"""
You are given a 0-indexed integer array nums. An index i is part of a hill in
    nums if the closest non-equal neighbors of i are smaller than nums[i].
    Similarly, an index i is part of a valley in nums if the closest non-equal
    neighbors of i are larger than nums[i]. Adjacent indices i and j are part
    of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal
    neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.

Example 1:
    Input: nums = [2,4,1,1,6,5]
    Output: 3
    Explanation:
        At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill
            nor a valley.
        At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index
            1 is a hill.
        At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index
            2 is a valley.
        At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index
            3 is a valley, but note that it is part of the same valley as index 2.
        At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index
            4 is a hill.
        At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill
            nor a valley.
        There are 3 hills and valleys so we return 3.

Example 2:
    Input: nums = [6,6,5,5,4,1]
    Output: 0
    Explanation:
    At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill
        nor a valley.
    At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill
        nor a valley.
    At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index
        2 is neither a hill nor a valley.
    At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index
        3 is neither a hill nor a valley.
    At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index
        4 is neither a hill nor a valley.
    At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill
        nor a valley.
    There are 0 hills and valleys so we return 0.

Constraints:
    - 3 <= nums.length <= 100
    - 1 <= nums[i] <= 100

A:
    all the same
        return 0
    array of size 0
        return 0
    array of size 1
        return 0
    array of size 2
        return 0
    negative nums
        not possible
    floats
        not possible

D:
    nums = [6,6,5,5,4,1]
    clean = [6,5,4,1]
    5, nothing
    4, nothing
    return 0

P:
    gen new list with no repeats
    start from second elem and proceed til 2nd to last

"""

from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        clean = [nums[0]]

        prev = nums[0]
        for n in nums[1:]:
            if n != prev:
                clean.append(n)
                prev = n

        hv = 0
        for ind, n in enumerate(clean[1:-1], 1):
            if (clean[ind - 1] > n and clean[ind + 1] > n) or (
                clean[ind - 1] < n and clean[ind + 1] < n
            ):
                hv += 1
        return hv


cases = [
    ([2, 4, 1, 1, 6, 5], 3),
    ([6, 6, 5, 5, 4, 1], 0),
    ([1, 2, 3], 0),
    ([1, 1, 1], 0),
    ([2, 1, 2], 1),
    ([1, 2, 1], 1),
    ([3, 2, 1], 0),
    ([1, 2, 1, 2, 1, 2], 4),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.countHillValley(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
