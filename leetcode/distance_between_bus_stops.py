"""
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all
    pairs of neighboring stops where distance[i] is the distance between the stops number i
    and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

Example 1:
    Input: distance = [1,2,3,4], start = 0, destination = 1
    Output: 1
    Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
    Input: distance = [1,2,3,4], start = 0, destination = 2
    Output: 3
    Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Example 3:
    Input: distance = [1,2,3,4], start = 0, destination = 3
    Output: 4
    Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

Constraints:
    1 <= n <= 10^4
    distance.length == n
    0 <= start, destination < n
    0 <= distance[i] <= 10^4

A:
    len(distance) == 1, means two stops only -> return distance value
    start == dest -> return 0
    start < dest -> assuming not always

D:
                       0 1 2 3
                      [4,3,2,1]
    Input: distance = [1,2,3,4], start = 0, destination = 1
        forward dist = sum(distance[start:destination]) = 1
        backward dist = sum(distance[0:start]) + sum(distance[destination:end]) = sum([]) + sum([2,3,4]) = 0 + 9 = 9
        return min(forward,backward)

    Input: distance = [1,2,3,4], start = 0, destination = 3
        forward dist = sum(distance[start:destination]) = sum([1,2,3,4]) = 10
        backward dist = sum(distance[0:start]) + sum(distance[destination:end]) = sum([]) + sum([4]) = 4
        return min(forward,backward)
"""

from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = min(start, destination)
        d = max(start, destination)
        return min(sum(distance[s:d]), sum(distance[:s]) + sum(distance[d:]))


cases = [
    ([1, 2, 3, 4], 0, 1, 1),
    ([1, 2, 3, 4], 0, 2, 3),
    ([1, 2, 3, 4], 0, 3, 4),
]

sol = Solution()
for (dist, s, d, exp) in cases:
    assert (
        got := sol.distanceBetweenBusStops(dist, s, d)
    ) == exp, f"Failed case ({dist}, {s}, {d}) - expecting ({exp}), got ({got})."
