"""
You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets
    more than limit candies.

Example 1:
    Input: n = 5, limit = 2
    Output: 3
    Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2
        candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

Example 2:
    Input: n = 3, limit = 3
    Output: 10
    Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3
        candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0),
        (2, 0, 1), (2, 1, 0) and (3, 0, 0).

Constraints:
    - 1 <= n <= 50
    - 1 <= limit <= 50

A:
    limit == 0
        return 1
    limit == n
        just do all
    n < limit
        just do all
    n == 0
        return 1
    n == 1
        return 3

D:
    n = 3, limit = 3
    first = 0
        second = 3, third = 0 (0,3,0)
        second = 2, third = 1 (0,2,1)
        second = 1, third = 2 (0,1,2)
        second = 0, third = 3 (0,0,3)
    first = 1
        second = 0, third = 2 (1,0,2)
        second = 1, third = 1 (1,1,1)
        second = 2, third = 0 (1,2,0)
    first = 2
        second = 0, third = 1 (2,0,1)
        second = 1, third = 0 (2,1,0)
    first = 3
        second = 0, third = 0 (3,0,0)

    n = 5, limit = 2
    first = 0
        second = 5, third = 0
        second = 4, third = 1
        second = 3, third = 2
        second = 2, third = 3
        second = 1, third = 4
        second = 0, third = 5

P:
    total = 0
    l = min(n, limit)
    for first in l:
        remain = l - first
        total += remain + 1
    return total

"""


class Solution:
    # sum should be n
    # none of the elements should be greater than limit
    def distributeCandies(self, n: int, limit: int) -> int:
        if limit == 0 or n == 0:
            return 1

        things = set()
        for first in range(n + 1):
            for second in range(n + 1):
                for third in range(n + 1):
                    if sum([first, second, third]) == n and all(
                        x <= limit for x in [first, second, third]
                    ):
                        things.add((first, second, third))
        return len(things)


cases = [
    (5, 2, 3),
    (3, 3, 10),
    (3, 5, 10),
    (0, 10, 1),
    (1, 10, 3),
    (10, 0, 1),
    (1, 1, 3),
    (1, 0, 1),
]

sol = Solution()
for n, limit, exp in cases:
    assert (
        got := sol.distributeCandies(n, limit)
    ) == exp, f"Failed case ({n}, {limit}) - got ({got}), expecting ({exp})."
