"""
You are given an integer array arr. Sort the integers in the array in ascending order by the number
    of 1's in their binary representation and in case of two or more integers have the same number
    of 1's you have to sort them in ascending order.

Return the array after sorting it.

Example 1:
    Input: arr = [0,1,2,3,4,5,6,7,8]
    Output: [0,1,2,4,8,3,5,6,7]
    Explantion: [0] is the only integer with 0 bits.
    [1,2,4,8] all have 1 bit.
    [3,5,6] have 2 bits.
    [7] has 3 bits.
    The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Example 2:
    Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
    Output: [1,2,4,8,16,32,64,128,256,512,1024]
    Explantion: All integers have 1 bit in the binary representation, you should just sort them in
        ascending order.

Constraints:
    - 1 <= arr.length <= 500
    - 0 <= arr[i] <= 10**4

A:
    empty arr:
        return []
    same number in arr:
        cool

D:
    for num in arr:
        b = f"{num:b}"
        d[b.count('1')].append(b)

    final = []
    for key in sorted(d.keys()):
        final.extend(int(x, 2) for x in sorted(d[key]))
"""

from typing import List
from collections import defaultdict


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for num in arr:
            b = f"{num:014b}"
            d[b.count('1')].append(b)

        final = []
        for key in sorted(d.keys()):
            final.extend(int(x, 2) for x in sorted(d[key]))
        return final


cases = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]),
    ([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]),
    ([0], [0]),
    ([0, 1], [0, 1]),
]

sol = Solution()
for arr, exp in cases:
    assert (
        got := sol.sortByBits(arr)
    ) == exp, f"Failed case ({arr}) - expecting ({exp}), got ({got})"
