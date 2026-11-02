"""
You are given a 2D array events which represents a sequence of events where a child pushes a series
    of buttons on a keyboard.

Each events[i] = [indexi, timei] indicates that the button at index indexi was pressed at time
    timei.
        - The array is sorted in increasing order of time.
        - The time taken to press a button is the difference in time between consecutive button
            presses. The time for the first button is simply the time at which it was pressed.

Return the index of the button that took the longest time to push. If multiple buttons have the same
    longest time, return the button with the smallest index.

Example 1:
    Input: events = [[1,2],[2,5],[3,9],[1,15]]
    Output: 1
    Explanation:
        Button with index 1 is pressed at time 2.
        Button with index 2 is pressed at time 5, so it took 5 - 2 = 3 units of time.
        Button with index 3 is pressed at time 9, so it took 9 - 5 = 4 units of time.
        Button with index 1 is pressed again at time 15, so it took 15 - 9 = 6 units of time.

Example 2:
    Input: events = [[10,5],[1,7]]
    Output: 10
    Explanation:
        Button with index 10 is pressed at time 5.
        Button with index 1 is pressed at time 7, so it took 7 - 5 = 2 units of time.

Constraints:
    - 1 <= events.length <= 1000
    - events[i] == [indexi, timei]
    - 1 <= indexi, timei <= 10**5
    - The input is generated such that events is sorted in increasing order of timei.

A:
    empty events:
        not possible
    event invalid (length not 2)
        not possible
    t2 < t1?
        not possible
    one item?
        return item index
    even with 0 time?
        no, all events are for button presses
A:
    really really bad question description! turns out:
        we don't need to keep track of total press time for index i
        just keep track of the max press time for a index i
        then provide the index with the largest presstime
        yuk

D:
    Input: events = [[1,2],[2,5],[3,9],[1,15]]

    startT = 0
    0
        1: 2
    1
        2: 3
    2
        3: 4
    3
        1: 2 + 6 = 8
    return 1


       0       1         2        3        4        5
    ([[4, 5], [19, 10], [3, 11], [3, 12], [6, 15], [1, 20]], 1),
    startT = 0
    0 -> 4  :               = 5
    1 -> 19 : (10 - 5)      = 5
    2 -> 3  : (11 - 10)     = 1
    3 -> 3  : 1 + (12 - 11) = 2
    4 -> 6  : (15 - 12)     = 3
    5 -> 1  : (20 - 15)     = 5

    return 4, 19 or 1? return 1 since lowest


       0       1        2       3        4       5         6         7        8
    ([[7, 1], [19, 3], [9, 4], [12, 5], [2, 8], [15, 10], [18, 12], [7, 14], [19, 16]], 2),
    startT = 0
    0 -> 7  :               = 1
    1 -> 19 : (3 - 1)       = 2
    2 -> 9  : (4 - 3)       = 1
    3 -> 12 : (5 - 4)       = 1
    4 -> 2  : (8 - 5)       = 3
    5 -> 15 : (10 - 8)      = 2
    6 -> 18 : (12 - 10)     = 2
    7 -> 7  : 1 + (14 - 12) = 3
    8 -> 19 : 2 + (16 - 14) = 4


P
    iterate items keeping track of times
    iterate times to extract max index and time
    return

O:
    time: O(n), iterate items about twice
    spac: O(i), number of unique button indices i


"""

from collections import defaultdict
from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        if len(events) == 1:
            return events[0][0]

        d = defaultdict(int)
        prevT = 0
        for e in events:
            d[e[0]] = max(d[e[0]], e[1] - prevT)
            prevT = e[1]

        maxi = float('inf')
        maxv = 0
        for k, v in d.items():
            if v == maxv:
                if k < maxi:
                    maxi = k
                    maxv = v
            elif v > maxv:
                maxi = k
                maxv = v

        return maxi


sol = Solution()

cases = [
    ([[1, 2], [2, 5], [3, 9], [1, 15]], 1),
    ([[10, 5], [1, 7]], 10),
    ([[1, 10]], 1),
    ([[10, 10]], 10),
    ([[10, 1], [11, 11]], 11),
    ([[4, 5], [19, 10], [3, 11], [3, 12], [6, 15], [1, 20]], 1),
    ([[7, 1], [19, 3], [9, 4], [12, 5], [2, 8], [15, 10], [18, 12], [7, 14], [19, 16]], 2),
]

for case, expected in cases:
    assert (
        got := sol.buttonWithLongestTime(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
