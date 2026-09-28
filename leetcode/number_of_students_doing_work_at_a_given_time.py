"""
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time
    endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the
    number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

Example 1:
    Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
    Output: 1
    Explanation: We have 3 students where:
    The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
    The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
    The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.

Example 2:
    Input: startTime = [4], endTime = [4], queryTime = 4
    Output: 1
    Explanation: The only student was doing their homework at the queryTime.

Constraints:
    - startTime.length == endTime.length
    - 1 <= startTime.length <= 100
    - 1 <= startTime[i] <= endTime[i] <= 1000
    - 1 <= queryTime <= 1000

A:
    empty start or/and endtime
        not possible
    end time before start time?
        not possible
    start time == end time
        possible: 2 -> 2:59 for example, so start = end = querytime counts as 1
    none ints:
        not possible
    query time > than last endtime
        return 0
    query time < than earliest starttime
        return 0
    are starttime and endtime sorted?
        who cares
    startime not equal in length as endtime?
        not possible

D:
    Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4

    total = 0
    i = 0
        1 to 3, q not within
    i = 1
        2 to 3, q not within
    i = 2
        3 to 7, q is within, total += 1
    return total (1)

P:
    total = 0
    for zip(starttime, endtime):
        if starttime <= querytime  <=endtime
            total += 1
    return total

O:
    use generator to reduce space complexity (going to just use zip quickyl instead of devising zipping generator function)

T:
    ([1,2,3], [3,2,7], 4, 1),
    ([4], [4], 4, 1),
    ([], [], 3, 0),
    ([1], [1], 1, 1),
    ([1], [1], 2, 0),
    ([1], [1], 0, 0),
    ([1], [2], 3, 0),
    ([1], [2], 1, 1),
    ([1], [2], 2, 1),
"""


class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        return sum(1 for s, e in zip(startTime, endTime) if s <= queryTime <= e)


sol = Solution()

cases = [
    ([1, 2, 3], [3, 2, 7], 4, 1),
    ([4], [4], 4, 1),
    ([], [], 3, 0),
    ([1], [1], 1, 1),
    ([1], [1], 2, 0),
    ([1], [1], 0, 0),
    ([1], [2], 3, 0),
    ([1], [2], 1, 1),
    ([1], [2], 2, 1),
]

for startTimes, endTimes, queryTime, expected in cases:
    assert (
        got := sol.busyStudent(startTimes, endTimes, queryTime)
    ) == expected, f"Woops! Failed case ({startTimes}, {endTimes}, {queryTime}) - expecting ({expected}), got ({got})."
