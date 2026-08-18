"""
There are n people standing in a line labeled from 1 to n. The first person in the line is holding
    a pillow initially. Every second, the person holding the pillow passes it to the next person
    standing in the line. Once the pillow reaches the end of the line, the direction changes, and
    people continue passing the pillow in the opposite direction.

    - For example, once the pillow reaches the nth person they pass it to the n - 1th person, then
        to the n - 2th person and so on.

Given the two positive integers n and time, return the index of the person holding the pillow after
    time seconds.

Example 1:
    Input: n = 4, time = 5
    Output: 2
    Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
    After five seconds, the 2nd person is holding the pillow.

Example 2:
    Input: n = 3, time = 2
    Output: 3
    Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
    After two seconds, the 3rd person is holding the pillow.

Constraints:
    - 2 <= n <= 1000
    - 1 <= time <= 1000

A:
    time > n:
        modulo
    time < n:
        grab from array
    n == 0:
        not possible
    n == 1:
        not possible
    time = 0
        not possible

D:
    Input: n = 4, time = 5
    l = [1,2,3,4,3,2,1], time < 2n - 1
        return l[5] = 2

    Input: n = 3, time = 2
    l = [1,2,3,2,1], time < 2n - 1
        return l[2] = 3

    Input: n = 4, time = 11
    l = [1,2,3,4,3,2,1], time > 2n - 1
        return l[time % (2n-2)] 
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        m = list(range(1, n + 1)) + list(range(2, n))[::-1]
        return m[time % ((2 * n) - 2)]


cases = [(4, 5, 2), (3, 2, 3), (4, 11, 2)]

sol = Solution()
for n, time, exp in cases:
    assert (
        got := sol.passThePillow(n, time)
    ) == exp, f"Failed case ({n}, {time}) - expecting ({exp}), got ({got})"
