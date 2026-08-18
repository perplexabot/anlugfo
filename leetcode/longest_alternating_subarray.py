"""
You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:
    - m is greater than 1.
    - s1 = s0 + 1.
    - The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words,
        s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2]
        = (-1)m.

Return the maximum length of all alternating subarrays present in nums or -1 if no such
    subarray exists.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [2,3,4,3,4]
    Output: 4
    Explanation: The alternating subarrays are [3,4], [3,4,3], and [3,4,3,4]. The longest of these
        is [3,4,3,4], which is of length 4.

Example 2:
    Input: nums = [4,5,6]
    Output: 2
    Explanation: [4,5] and [5,6] are the only two alternating subarrays. They are both of length 2.

Constraints:
    - 2 <= nums.length <= 100
    - 1 <= nums[i] <= 10**4

A:
    len(nums) < 2: not possible
    is x,x considered alternating: no
A:
    ?
D:
                  4       5           5
    nums = [1,2,1,2,3,2,3,2,1,0,1,0,1,0]
"""

from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        max_cnt = -1
        for i in range(len(nums) - 1):
            pair = nums[i : i + 2]
            if pair[1] - pair[0] != 1:
                continue
            cnt = 2
            j = i + 2
            while j < len(nums) - 1 and pair == nums[j : j + 2]:
                j += 2
                cnt += 2
            cnt = cnt + 1 if j < len(nums) and pair[0] == nums[j] else cnt
            max_cnt = max(max_cnt, cnt)
        return max_cnt


cases = [
    ([2, 3, 4, 3, 4], 4),
    ([4, 5, 6], 2),
    ([1, 2, 1, 2, 3, 2, 3, 2, 1, 0, 1, 0, 1, 0], 5),
    ([21, 9, 5], -1),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.alternatingSubarray(case)
    ) == exp, f'Failed case ({case}) - expecting ({exp}), got ({got}).'
