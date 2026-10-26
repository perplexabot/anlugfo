"""
You are given a 2D integer array drones, where drones[i] = [xi, yi, rangei] represents the
    x-coordinate, y-coordinate, and travel range of the ith drone.

You are also given an integer array target = [tx, ty], representing the coordinates of the target.

A drone drones[i] can reach the target if the manhattan-distance between its coordinates and the
    target coordinates is less than or equal to its rangei.

Return the index of the reachable drone with the minimum Manhattan distance to the target. If there
    is a tie, return the smallest index. If no drone can reach the target, return -1.

Example 1:
    Input: drones = [[0,0,8],[2,2,9]], target = [3,4]
    Output: 1
    Explanation:
        The distance between drones[0] and target is |0 - 3| + |0 - 4| = 7, which is within its
            range of 8.
        The distance between drones[1] and target is |2 - 3| + |2 - 4| = 3, which is within its
            range of 9.
        Since drones[1] is the nearest drone, the answer is 1.

Example 2:
    Input: drones = [[2,1,5],[4,4,5],[6,6,8]], target = [5,5]
    Output: 1
    Explanation:
        The distance between drones[0] and target is |2 - 5| + |1 - 5| = 7, which is greater than
            its range of 5.
        The distance between drones[1] and target is |4 - 5| + |4 - 5| = 2, which is within its
            range of 5.
        The distance between drones[2] and target is |6 - 5| + |6 - 5| = 2, which is within its
            range of 8.
        Both drones[1] and drones[2] are the nearest drones. Since we should return the smallest
            index, the answer is 1.

Example 3:
    Input: drones = [[4,4,5]], target = [8,6]
    Output: -1
    Explanation:
        The distance between drones[0] and target is |4 - 8| + |4 - 6| = 6, which is greater than
            its range of 5.
        No drone can reach the target, so the answer is -1.

Constraints:
    - 1 <= drones.length <= 100
    - drones[i] = [xi, yi, rangei]
    - target = [tx, ty]
    - -25 <= xi, yi, tx, ty <= 25
    - 1 <= rangei <= 100

A:
    no drones
        not possible
    1 drone
        same as any positive integer
    no target
        not possible
    target outside of all ranges
        possible
    target and a drone coord match
        return smallest index between direct matches
    drones with 0 range?
        no
    drones with < 0 range
        no

D:
    Input: drones = [[2,1,5],[4,4,5],[6,6,8]], target = [5,5]

    mind = 999999
    d0 abs(2-5) + abs(1-5) = 7, mindis=7, minind=0
    d1 abs(4-5) + abs(4-5) = 2, mindis=2, minind=1
    d2 abs(6-5) + abs(6-5) = 2, mindis=2, minind=1

P
    minind, mindis = -1, largenumber
    for i in range(len(drones)):
        d = abs(drones[i].x - t.x) + abs(drones[i].y - t.y)
        if d <= drones[i].range and d < minidis:
            minidis = d
            minind = i

O
    P is O(n) in time O(1) in space.

T:
    [[0,0,8],[2,2,9]], [3,4], 1
    [[2,1,5],[4,4,5],[6,6,8]], [5,5], 1
    [[4,4,5]], [8,6], -1
    [[1,0,0.5]], [0,0], -1
    [[0,1,0.5]], [0,0], -1
    [[0,0,0.5]], [0,0], 0
"""


class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        minind, mindis = -1, float('inf')
        for i in range(len(drones)):
            d = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
            if d <= drones[i][2] and d < mindis:
                mindis = d
                minind = i
        return minind


cases = [
    (([[0, 0, 8], [2, 2, 9]], [3, 4]), 1),
    (([[2, 1, 5], [4, 4, 5], [6, 6, 8]], [5, 5]), 1),
    (([[4, 4, 5]], [8, 6]), -1),
    (([[1, 0, 0.5]], [0, 0]), -1),
    (([[0, 1, 0.5]], [0, 0]), -1),
    (([[0, 0, 0.5]], [0, 0]), 0),
]

sol = Solution()

for case, expected in cases:
    assert (
        got := sol.nearestDrone(*case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
