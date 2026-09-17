"""
Given a fixed-length integer array arr, duplicate each occurrence of zero,
    shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
    Do the above modifications to the input array in place and do not return anything.

Example 1:
    Input: arr = [1,0,2,3,0,4,5,0]
    Output: [1,0,0,2,3,0,0,4]
    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
    Input: arr = [1,2,3]
    Output: [1,2,3]
    Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:
    - 1 <= arr.length <= 10**4
    - 0 <= arr[i] <= 9

AADPOCT

A:
    empty arr?
        return arr
    arr of just 0s?
        return arr
    in place vs new?
        either?
        apparently the question didn't mention inplace is a requirment - but it is!
        so this has to mod the arr in place
    non numbers in arr?
        who cares
A:
    none arr passed?
        not possible
    max size of arr?
        10**4
D:
                  0 1 2 3 4 5 6 7
    Input: arr = [1,0,2,3,0,4,5,0]

    n = []
    l = len(arr)
    i = {0..l}

    i = 0:
        arr[i] != 0, n.append(arr[i])
        n = [1]
        if len(n) >= l return using n[:l]
    i = 1:
        arr[i] == 0, n.extend([0,0])
        n = [1,0,0]
        if len(n) >= l return using n[:l]
    i = 2:
        arr[i] != 0, n.append(arr[i])
        n = [1,0,0,2]
        if len(n) >= l return using n[:l]
    i = 3:
        arr[i] != 0, n.extend([0,0])
        n = [1,0,0,2,3]
        if len(n) >= l return using n[:l]
    i = 4:
        arr[i] == 0, n.extend([0,0])
        n = [1,0,0,2,3,0,0]
        if len(n) >= l return using n[:l]
    i = 5:
        arr[i] != 0, n.extend([0,0])
        n = [1,0,0,2,3,0,0,4]
        if len(n) >= l return using n[:l], yes return

P:
    n = []
    l = len(arr)
    cnt = 0
    while cnt < l:
        if arr[cnt] != 0:
            n.append(arr[cnt])
        else:
            n.extend([0,0])

        if len(n) >= l:
            break

        cnt += 1

    for ind, i in enumerate(n):
        arr[ind] = i

O:
    time complexity: O(2n) = O(n)
    space complexity: O(2n) = O(n)

    Might be possible to not create an extra array - complexity will stay the same.
C:
T:
    []
    [0]
    [0,0,0,0,0]
    [1,2,3]
    [1,2,3,0]
    [0,1]
    [1,0,1]
    [1]
"""


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """Do not return anything, modify arr in-place instead."""

        n = []
        l = len(arr)
        cnt = 0

        while cnt < l:
            if arr[cnt]:
                n.append(arr[cnt])
            else:
                n.extend([0, 0])

            if len(n) >= l:
                break

            cnt += 1

        for i in range(l):
            arr[i] = n[i]


sol = Solution()

cases = [
    ([], []),
    ([0], [0]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 0], [1, 2, 3, 0]),
    ([0, 1], [0, 0]),
    ([1, 0, 1], [1, 0, 0]),
    ([1], [1]),
]

for test, expected in cases:
    assert (
        sol.duplicateZeros(test) or test
    ) == expected, f"Woops {test} failed - expecting {expected}, got {test}"
