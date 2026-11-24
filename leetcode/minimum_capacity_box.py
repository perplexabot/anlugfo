"""
You are given an integer array capacity, where capacity[i] represents the capacity of the
    ith box, and an integer itemSize representing the size of an item.

The ith box can store the item if capacity[i] >= itemSize.

Return an integer denoting the index of the box with the minimum capacity that can store the item.
    If multiple such boxes exist, return the smallest index.

If no box can store the item, return -1.

Example 1:
    Input: capacity = [1,5,3,7], itemSize = 3
    Output: 2
    Explanation:
        The box at index 2 has a capacity of 3, which is the minimum capacity that can store the item. Thus, the answer is 2.

Example 2:
    Input: capacity = [3,5,4,3], itemSize = 2
    Output: 0
    Explanation:
        The minimum capacity that can store the item is 3, and it appears at indices 0 and 3. Thus, the answer is 0.

Example 3:
    Input: capacity = [4], itemSize = 5
    Output: -1
    Explanation:
        No box has enough capacity to store the item, so the answer is -1.

Constraints:
    - 1 <= capacity.length <= 100
    - 1 <= capacity[i] <= 100
    - 1 <= itemSize <= 100

A:
    len(cap) < 1?
        no
    capacity is negative?
        no
    capacity is zero
        no
    no capacity allows for item?
        possible
    can we use two consecutive caps to fill item?
        no
    negative item size or size of zero?
        no

D:
    Input: capacity = [3,5,4,3], itemSize = 2
    Output: 0

    i = 0, 1
    i = 1, 3
    i = 2, 2
    i = 3, 1
    return i = 0

P
    minc = float(inf)
    mini = -1

    for i in caps:
        if cap[i] - itemSize >= 0 and < minc:
            minc = cap[i] - itemSize
            mini = i
    return mini

O:
    time: O(n)
    spac: O(1)

T:
    [1,5,3,7], 3, 2
    [3,5,4,3], 2, 0
    [4], 5, -1
    [4], 4, 0
    [4], 3, 0
    [1,2,3], 3, 2
    [1,2,3], 2, 1
    [1,2,3], 1, 0
    [3,2,1], 3, 2
    [3,2,1], 2, 1
    [3,2,1], 1, 0
"""


class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minc = float('inf')
        mini = -1

        for index in range(len(capacity)):
            if (diff := capacity[index] - itemSize) >= 0 and diff < minc:
                minc = diff
                mini = index
        return mini


cases = [
    (([1, 5, 3, 7], 3), 2),
    (([3, 5, 4, 3], 2), 0),
    (([4], 5), -1),
    (([4], 4), 0),
    (([4], 3), 0),
    (([1, 2, 3], 3), 2),
    (([1, 2, 3], 2), 1),
    (([1, 2, 3], 1), 0),
    (([3, 2, 1], 3), 0),
    (([3, 2, 1], 2), 1),
    (([3, 2, 1], 1), 2),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.minimumIndex(*case)
    ) == expected, f"FaIlEd case ({case}), expecting ({expected}), got ({got})."
