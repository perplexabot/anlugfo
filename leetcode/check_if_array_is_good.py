"""
You are given an integer array nums. We consider an array good if it is a permutation of an
    array base[n].

base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which
    contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and
    base[3] = [1, 2, 3, 3].

Return true if the given array is good, otherwise return false.

Note: A permutation of integers represents an arrangement of these numbers.

Example 1:
    Input: nums = [2, 1, 3]
    Output: false
    Explanation: Since the maximum element of the array is 3, the only candidate n for which this
        array could be a permutation of base[n], is n = 3. However, base[3] has four elements but
        array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So
        the answer is false.

Example 2:
    Input: nums = [1, 3, 3, 2]
    Output: true
    Explanation: Since the maximum element of the array is 3, the only candidate n for which this
        array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation
        of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach
        base[3]). Therefore, the answer is true.

Example 3:
    Input: nums = [1, 1]
    Output: true
    Explanation: Since the maximum element of the array is 1, the only candidate n for which this
        array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation
        of base[1] = [1, 1]. Therefore, the answer is true.

Example 4:
    Input: nums = [3, 4, 4, 1, 2, 1]
    Output: false
    Explanation: Since the maximum element of the array is 4, the only candidate n for which this
        array could be a permutation of base[n], is n = 4. However, base[4] has five elements but
        array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So
        the answer is false.

Constraints:
    - 1 <= nums.length <= 100
    - 1 <= num[i] <= 200

A:
    what is n?
        could be any number, but for a case C, it depends on len(nums)
    what if nums is empty?
        not possible
    what if nums is of size 1
        not good
    is nums sorted
        noo
    ok to mod original ds?
        going to

D:
    Input: nums = [1, 3, 3, 2]
    l = len(nums) = 4, so should be compared against base[l-1] = base[3]
    is set(nums) == set(base[3]) AND nums.count(l-1) == 2,  return True

P:
    if len(nums) < 2:
        return False

    s = sorted(nums)
    prev = 0
    for curr in s[:-1]:
        if curr - prev != 1:
            return False
        prev = curr

    return s[-1] == s[-2]

O:
    using sort then processing
    sort       iterate
    O(nlogn) + O(n)     = O(n) [time]
    O(n)     + O(1)     = O(n) [space]

C:

T:

    ([2, 1, 3], false),
    ([1, 3, 3, 2], true),
    ([1, 1], true),
    ([3, 4, 4, 1, 2, 1], false),
    ([1], false),

"""

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        nums.sort()
        prev = 0
        for curr in nums[:-1]:
            if curr - prev != 1:
                return False
            prev = curr
        return nums[-1] == nums[-2]


cases = [
        ([2, 1, 3], False),
        ([1, 3, 3, 2], True),
        ([1, 1], True),
    ([3, 4, 4, 1, 2, 1], False),
        ([1], False),
]

sol = Solution()
for nums, expected in cases:
    assert (
        got := sol.isGood(nums)
    ) == expected, f"Failed case ({nums}) - expecting ({expected}), ({got})."
