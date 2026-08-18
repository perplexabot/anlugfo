"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of
    positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative
    integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.

Example 1:
    Input: nums = [-2,-1,-1,1,2,3]
    Output: 3
    Explanation: There are 3 positive integers and 3 negative integers. The maximum count among
        them is 3.

Example 2:
    Input: nums = [-3,-2,-1,0,0,1,2]
    Output: 3
    Explanation: There are 2 positive integers and 3 negative integers. The maximum count among
        them is 3.

Example 3:
    Input: nums = [5,20,66,1314]
    Output: 4
    Explanation: There are 4 positive integers and 0 negative integers. The maximum count among
        them is 4.

Constraints:
    - 1 <= nums.length <= 2000
    - -2000 <= nums[i] <= 2000
    - nums is sorted in a non-decreasing order.

Follow up: Can you solve the problem in O(log(n)) time complexity?

A:
    empty array
        return 0
    array with 0s only
        return 0
    equal pos and negs
        return either
    array with only pos or negs
        return size of arr

A:
    ?

D:
    Input: nums = [-3,-2,-1,0,0,1,2]
    len = 7
    mid = len // 2 = 3
    if nums[mid] is positive and nums[mid-1] is negative: found interface
    if nums[mid] is negative and nums[mid+1] is positive: found interface
    if nums[mid] is zero, found interface
        find left bound zero        ind = 3
        find right bound zero       ind = 4
        get answer max(left_bound = 3, len - right_bound - 1 = 2) = 3

P:
    s = 0
    e = len(nums) - 1
    mid = s + [(e - s) // 2]
    if nums[mid] is + and before is negative (skip 0):
        do a calc
    if nums[mid] is - and after is positive (skip 0):
        do a calc
    if nums[mid] is 0:
        do a calc
    else:
        if nums[mid] is +:
            e = mid
        if nums[mid] is -:
            s = mid
"""

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if nums[0] > 0:
            return len(nums)
        if nums[-1] < 0:
            return len(nums)
        if nums[0] == 0:
            cnt = 1
            while cnt < len(nums) and nums[cnt] == 0:
                cnt += 1
            return len(nums) - cnt
        if nums[-1] == 0:
            print('here')
            cnt = 1
            while -1 - cnt >= 0 and nums[-1 - cnt] == 0:
                print('---')
                cnt = 1
            return len(nums) - cnt

        s, e = 0, len(nums) - 1
        while True:
            mid = s + ((e - s) // 2)

            if nums[mid] > 0 and nums[mid - 1] <= 0:
                cnt = 0
                while mid - cnt - 1 >= 0 and nums[mid - 1 - cnt] == 0:
                    cnt += 1
                return max(len(nums) - mid - 1, mid - cnt + 1)

            elif nums[mid] < 0 and nums[mid + 1] >= 0:
                cnt = 0
                while mid + 1 + cnt < len(nums) and nums[mid + 1 + cnt] == 0:
                    cnt += 1
                return max(len(nums) - mid - 1 - cnt, mid + 1)

            elif nums[mid] == 0:
                lcnt = mid
                while lcnt >= 0 and nums[lcnt] == 0:
                    lcnt -= 1
                rcnt = mid
                while rcnt < len(nums) and nums[rcnt] == 0:
                    rcnt += 1

                return max(lcnt + 1, len(nums) - rcnt)

            else:
                if nums[mid] < 0:
                    s = mid
                else:
                    e = mid


cases = [
    ([-2, -1, -1, 1, 2, 3], 3),
    ([-3, -2, -1, 0, 0, 1, 2], 3),
    ([5, 20, 66, 1314], 4),
    ([], 0),
    ([1], 1),
    ([-1], 1),
    ([-1, 1], 1),
    ([-1, 0], 1),
    ([0, 1], 1),
    ([0], 0),
    ([0, 0, 0], 0),
    ([-1, -2, -3], 3),
]

sol = Solution()
for inp, exp in cases:
    assert (
        got := sol.maximumCount(inp)
    ) == exp, f"Failed case ({inp}) - expecting ({exp}), got ({got})."
