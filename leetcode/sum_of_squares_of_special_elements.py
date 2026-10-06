"""
You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

Return the sum of the squares of all special elements of nums.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 21
    Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2]
        since 2 divides 4, and nums[4] since 4 divides 4.
    Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] +
        nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.

Example 2:
    Input: nums = [2,7,1,19,18,3]
    Output: 63
    Explanation: There are exactly 4 special elements in nums: nums[1] since 1 divides 6, nums[2]
        since 2 divides 6, nums[3] since 3 divides 6, and nums[6] since 6 divides 6.
    Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] +
        nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 +
        3 * 3 = 63.

Constraints:
    - 1 <= nums.length == n <= 50
    - 1 <= nums[i] <= 50

A:
    nums of size 0
        not possible
    nums of size 1
        return nums[0]**2
    negativives in nums
        not possible
    what if the same special element is id'd N times?
        use once or use N times?
        data insufficient to answer this...

D:
                   1 2 3 4  5  6
    Input: nums = [2,7,1,19,18,3]
                   x x x       x
                   2**2 + 7**2 + 1**2 + 3**2
                   4    + 49   + 1    + 9   = 63

P:
    final = 0
    for i in range(1,len(nums)+1):
        if i % len(nums) == 0:
            final += nums[i-1]
    return final

O:
    1 pass, no extra ds
    time is O(n)
    space is O(1)

T:
    ([1,2,3,4], 21),
    ([2,7,1,19,18,3], 63),
    ([10], 100),
    ([1,2], 5),
    ([4,2,3,4], 36),
"""


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l = len(nums)
        final = 0
        for i in range(1, l + 1):
            if not l % i:
                final += nums[i - 1] ** 2
        return final


cases = [
    ([1, 2, 3, 4], 21),
    ([2, 7, 1, 19, 18, 3], 63),
    ([10], 100),
    ([1, 2], 5),
    ([4, 2, 3, 4], 36),
]

sol = Solution()
for nums, expected in cases:
    assert (
        got := sol.sumOfSquares(nums)
    ) == expected, f"Failed case ({nums}) - expecting ({expected}), got ({got})."
