"""
You are given an array of integers nums. Return the length of the longest
    subarray of nums which is either strictly increasing or strictly decreasing.



Example 1:
    Input: nums = [1,4,3,3,2]
        Output: 2
        Explanation:
            The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
            The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
            Hence, we return 2.

Example 2:
    Input: nums = [3,3,3,3]
    Output: 1
    Explanation:
        The strictly increasing subarrays of nums are [3], [3], [3], and [3].
        The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
        Hence, we return 1.

Example 3:
    Input: nums = [3,2,1]
    Output: 3
    Explanation:
        The strictly increasing subarrays of nums are [3], [2], and [1].
        The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
        Hence, we return 3.

Constraints:
    - 1 <= nums.length <= 50
    - 1 <= nums[i] <= 50

A:
    empty arr
        no
    size of 1
        return 1
    negatives and zeros?
        so what!
    longest subarray size of arr
        sorted arr
    no longest subarray
        not possible, size of 2 is always possible

D:
                   0 1 2 3 4
    Input: nums = [1,4,3,3,2]
    increasing:
        0,1
    decreasing:
        1,2 or 3,4

    return 2

P:
    if len(arr) < 3:
        return len(arr)

    longest_increasing = 0
    current_increasing = 0
    longest_decreasing = 0
    current_decreasing = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_increasing++
        else:
            longest_increasing = max(longest_increasing, current_increasing)
            current_increasing = 0

        if arr[i] < arr[i-1]:
            current_decreasing++
        else:
            longest_decreasing = max(longest_decreasing, current_decreasing)

    return max(longest_increasing,longest_decreasing)

O:
    time: O(n)
    spac: O(1)

T:
    ([1,4,3,3,2], 2),
    ([3,3,3,3], 1),
    ([3,2,1], 3),
    ([1], 1),
    ([1,2], 2),
    ([2,1], 2),
    ([100,1], 2),
    ([1,1], 1),
"""

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        longest_increasing = 1
        current_increasing = 1
        longest_decreasing = 1
        current_decreasing = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_increasing += 1
            else:
                longest_increasing = max(longest_increasing, current_increasing)
                current_increasing = 1

            if nums[i] < nums[i - 1]:
                current_decreasing += 1
            else:
                longest_decreasing = max(longest_decreasing, current_decreasing)
                current_decreasing = 1

        longest_increasing = max(longest_increasing, current_increasing)
        longest_decreasing = max(longest_decreasing, current_decreasing)
        return max(longest_decreasing, longest_increasing)


sol = Solution()

cases = [
    ([1, 4, 3, 3, 2], 2),
    ([3, 3, 3, 3], 1),
    ([3, 2, 1], 3),
    ([1], 1),
    ([1, 2], 2),
    ([2, 1], 2),
    ([100, 1], 2),
]

for case, expected in cases:
    assert (
        got := sol.longestMonotonicSubarray(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
