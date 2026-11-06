"""
Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in
    nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:
    Input: nums = [-3,2,-3,4,2]
    Output: 5
    Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
    step by step sum
    startValue = 4 | startValue = 5 | nums
      (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
      (1 +2 ) = 3  | (2 +2 ) = 4    |   2
      (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
      (0 +4 ) = 4  | (1 +4 ) = 5    |   4
      (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:
    Input: nums = [1,2]
    Output: 1
    Explanation: Minimum start value should be positive.

Example 3:
    Input: nums = [1,-2,-3]
    Output: 5

Constraints:
    - 1 <= nums.length <= 100
    - -100 <= nums[i] <= 100

A:
    no negatives:
        return 1
    all negatives:
        same problem
    first negative
        doesn't matter
    0s?
        yes, treat like a positive
    empty?
        nope
    one element?
        abs(nums[0])? no if negative figure it out else 1
    all negatives except last number?
        doesn't matter

D:
    Input: nums = [1,-2,-3]
    1
    1 + (-2) = -1
    -1 + (-3) = -4
    1 - (-4) = 5
    return 5

    input: nums = [1,2]
    1
    1 + 2 = 3
    1 - 3 < 0: return 1


P:
    find first positive's index
    sum nums[index+1:]

O:
    time complexity: O(n)
    spac complexity: O(1)

T:
    ([-3,2,-3,4,2],5)
    ([1,2],1)
    ([1,-2,-3],5)
    ([-1,-2,3],4)
    ([1],1)
    ([-1],2)
    ([-1,0,-1],3)

"""


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        mins = float('inf')
        running = 0
        for i in nums:
            running += i
            if running < mins:
                mins = running

        return 1 if (ans := 1 - mins) <= 0 else ans


cases = [
    ([-3, 2, -3, 4, 2], 5),
    ([1, 2], 1),
    ([1, -2, -3], 5),
    ([-1, -2, 3], 4),
    ([1], 1),
    ([-1], 2),
    ([-1, 0, -1], 3),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.minStartValue(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
