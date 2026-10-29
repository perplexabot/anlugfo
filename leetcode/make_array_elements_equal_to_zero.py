"""
You are given an integer array nums.
Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement
    direction of either left or right.
After that, you repeat the following process:
    - If curr is out of the range [0, n - 1], this process ends.
    - If nums[curr] == 0, move in the current direction by incrementing curr if you are moving
        right, or decrementing curr if you are moving left.
    - Else if nums[curr] > 0:
        - Decrement nums[curr] by 1.
        - Reverse your movement direction (left becomes right and vice versa).
        - Take a step in your new direction.

A selection of the initial position curr and movement direction is considered valid if every
    element in nums becomes 0 by the end of the process.
Return the number of possible valid selections.

Example 1:
    Input: nums = [1,0,2,0,3]
    Output: 2
    Explanation:
    The only possible valid selections are the following:
        Choose curr = 3, and a movement direction to the left.
            [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2]
            -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1]
            -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1]
            -> [0,0,0,0,0].
        Choose curr = 3, and a movement direction to the right.
            [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2]
            -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0]
            -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].

Example 2:
    Input: nums = [2,3,4,0,4,1,0]
    Output: 0
    Explanation:
        There are no possible valid selections.

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 100
    - There is at least one element i where nums[i] == 0.

A:
    none 0 or positives
        no
    empty arr
        no
    arr size 1
        if 0 return 1 else 0
    all zeros
        return size of arr
    no zeros
        return 0

D:
                   0 1 2 3 4 5 6
    Input: nums = [2,3,4,0,4,1,0]
        try index 3:
            [2,3,4,0,4,1,0]
            [2,3,0,0,0,1,0]
            [2,2,0,0,0,0,0]
            [2,2,0,0,0,0,0]
            FAIL
        try index 6
            FAIL

                   0 1 2 3 4
    Input: nums = [1,0,2,0,3]
        try index 1
            [1,0,2,0,3]
            [0,0,1,0,3]
            FAIL
        try index 3
            [1,0,2,0,3]
            [1,0,1,0,2]
            [1,0,0,0,1]
            PASS. Does a pass always count as two ways?
                not if the initial starting point was at index 0 or len(nums) - 1
                    then if there are methods, the total methods is 1

                OR

    Input: nums = [2,3,4,0,4,1,0]
        try index 3:
            [2,3,4,0,4,1,0]
             2+3+4 | 4+1+0
             8     | 5
             8 - 5 > 1 so FAIL
        try index 6:
            [2,3,4,0,4,1,0]
             2+3+4+0+4+1|0
             14         |0
             14 - 0 > 1 so FAIL

    Input: nums = [1,0,2,0,3]
        try index 1:
            [1,0,2,0,3]
             1 | 2+0+3
             1 | 5
             5 - 1 > 1 so FAIL
        try index 3:
            [1,0,2,0,3]
             1+0+2 | 3
             3     | 3
             3 - 3 <= 1 so PASS

    Input: nums = [0, 1, 0]
        try index 0:
            [0,1,0]
           0 | 1+0
           0 | 1
            1 - 0 <= 1 so PASS
        try index 2
            [0,1,0]
             0+1 | 0
             1   | 0
            1 - 0 <= 1 so PASS

    Input: nums = [0,1]
        try index 0:
            [0,1]
          0  | 1
          1 - 0 <= 1 so PASS

P:
    for each 0 in array
        while have not reached end indices:
            subtract closest left and right none 0 elements until one reaches 0
            if one reaches end and the other is at a none zero element:
                break
            if both indices are ends with values of zero:
                ways += 2
                break

O:

    time: O(n**2) since: finding zeros * checking zeros = n**2
    spac: O(n) using a temp array with same size as input array

    updated:
        time: O(n), only iterate once while keeping track of sums
        spac: O(1), no longer using secondary array


T:
    [1,0,2,0,3] 2
    [2,3,4,0,4,1,0] 0
    [0,0,0] 2
    [1,0,1] 2
    [0,0,0] 2
    [0] 2
    [1] 0
    [1,1,1] 0
"""

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ways = 0
        rightSum = sum(nums)

        if len(nums) == 1:
            if nums[0] == 0:
                return 2

        if nums[0] == 0:
            if rightSum == 0:
                ways += 2
            if rightSum == 1:
                ways += 1
        if nums[-1] == 0:
            if rightSum == 0:
                ways += 2
            if rightSum == 1:
                ways += 1

        leftSum = nums[0]
        rightSum -= nums[0]
        for i in range(1, len(nums) - 1):
            leftSum += nums[i]
            rightSum -= nums[i]
            if nums[i] == 0:
                if (diff := abs(leftSum - rightSum)) <= 1:
                    ways += 1 if diff == 1 else 2

        return ways


cases = [
    ([1, 0, 2, 0, 3], 2),
    ([2, 3, 4, 0, 4, 1, 0], 0),
    ([1, 0, 1], 2),
    ([0, 0, 0], 6),
    ([0], 2),
    ([1], 0),
    ([1, 1, 1], 0),
    ([0, 1, 0], 2),
    ([0, 0, 1], 2),
    ([1, 0, 0], 2),
    ([0, 1], 1),
]

sol = Solution()

for case, expected in cases:
    print(f"Testing {case}")
    assert (
        got := sol.countValidSelections(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
