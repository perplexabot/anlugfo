"""
Given an array arr, replace every element in that array with the greatest element among the
    elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:
    Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]
    Explanation:
    - index 0 --> the greatest element to the right of index 0 is index 1 (18).
    - index 1 --> the greatest element to the right of index 1 is index 4 (6).
    - index 2 --> the greatest element to the right of index 2 is index 4 (6).
    - index 3 --> the greatest element to the right of index 3 is index 4 (6).
    - index 4 --> the greatest element to the right of index 4 is index 5 (1).
    - index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
    Input: arr = [400]
    Output: [-1]
    Explanation: There are no elements to the right of index 0.

Constraints:
    - 1 <= arr.length <= 104
    - 1 <= arr[i] <= 105

A:
    array of size < 2?
        yes
    none positive ints
        no

D:
                   0  1 2 3 4 5
    Input: arr = [17,18,5,4,6,1]

    ind=5, -1, max=1
    ind=4, 1, max=6
    ind=3, 6, max=6
    ind=2, 6, max=6
    ind=1, 6, max=18
    ind=0, 18, max=18

    return [18, 6, 6, 6, 1, -1]
"""

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            curr = arr[i]
            arr[i] = m
            m = max(m, curr)
        return arr


sol = Solution()

cases = [
    ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
    ([400], [-1]),
]

for case, exp in cases:
    assert (
        got := sol.replaceElements(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
