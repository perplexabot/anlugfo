"""
In the town of Digitville, there was a list of numbers called nums containing integers from 0 to
    n - 1. Each number was supposed to appear exactly once in the list, however, two
    mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two
    containing the two numbers (in any order), so peace can return to Digitville.

Example 1:
    Input: nums = [0,1,1,0]
    Output: [0,1]
    Explanation:
        The numbers 0 and 1 each appear twice in the array.

Example 2:
    Input: nums = [0,3,2,1,3,2]
    Output: [2,3]
    Explanation:
        The numbers 2 and 3 each appear twice in the array.

Example 3:
    Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]
    Output: [4,5]
    Explanation:
        The numbers 4 and 5 each appear twice in the array.

Constraints:
    - 2 <= n <= 100
    - nums.length == n + 2
    - 0 <= nums[i] < n
    - The input is generated such that nums contains exactly two repeated elements.

A:
    list len < 4?
        no
    always two sneaks?
        yes
    negatives, zeros?
        who cares
    can the sneaks be the same number?
        no?

D:
    Input: nums       = [7,1,5,4,3,4,6,0,9,5,8,2]
    sort              = [0,1,2,3,4,4,5,5,6,7,8,9]
    find consecutives =          x   x

P:
    sneaks = []
    nums.sort()
    prev = nums[0]
    for i in nums[1:]:
      if i == prev:
        sneaks.append(i)
      prev = i

O:
    time complexity
    ( sort )   ( iterate )
    O(nlogn) +    O(n) = O(nlogn) = O(nlogn)

    space complexity is O(1)

    can reduce time complexity to O(n) by increasing space complexity to O(N) (from collections import Counter)

T:
    [0,1,1,0], [0,1]
    [0,3,2,1,3,2], [2,3]
    [7,1,5,4,3,4,6,0,9,5,8,2], [4,5]
    [1,2,1,2,3,4], [1,2]
    [1,2,3,4,1,2], [1,2]
"""


class Solution(object):
    def getSneakyNumbers(self, nums):
        sneaks = []
        nums.sort()
        prev = nums[0]
        for i in nums[1:]:
            if i == prev:
                sneaks.append(i)
            prev = i
        return sneaks


cases = [
    ([0, 1, 1, 0], [0, 1]),
    ([0, 3, 2, 1, 3, 2], [2, 3]),
    ([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2], [4, 5]),
    ([1, 2, 1, 2, 3, 4], [1, 2]),
    ([1, 2, 3, 4, 1, 2], [1, 2]),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.getSneakyNumbers(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
