"""
You are given a string time in the form of hh:mm, where some of the digits in the string are 
    hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

Example 1:
    Input: time = "2?:?0"
    Output: "23:50"
    Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending 
        with the digit '0' is 50.

Example 2:
    Input: time = "0?:3?"
    Output: "09:39"

Example 3:
    Input: time = "1?:22"
    Output: "19:22"

Constraints:
    time is in the format hh:mm.
    It is guaranteed that you can produce a valid time from the given string.

A:
    more than one question mark -> possible
    colon always there -> yes
    00:00 < 23:59

D:
    01234
    ??:??

    0 -> range(0,2) 
    1 -> range(0,9) if 0 is < 2 else range(0,3)
    2 -> :
    3 -> range(0,5)
    4 -> range(0,9)

    01234
    0?:3?
    1 -> max(range(0,9)) -> 9
    4 -> max(range(0,5)) -> 5
    09:39


    01234
    2?:?0
    1 -> max(range(0,3)) -> 3
    3 -> max(range(0,5)) -> 5
    23:50

    01234
    1?:22
    1 -> max(range(0,9)) -> 9
    19:22

    if time[:2] == '??' -> new.append('23')
    if time[:2] == '?d' -> new.append('2d') if d < 4 else new.append('1d')
    if time[:2] == "d?' -> new.append('d9') if d < 2 else new.append('d3')
    new.append(':')
    if time[3] == '?' -> new.append('5') else mew.append(time[3])
    if time[4] == '?' -> new.append('9') else new.append(time[4])

"""


class Solution:
    def maximumTime(self, time: str) -> str:
        new = []
        if time[:2] == '??':
            new.append('23')
        elif time[:2].startswith('?'):
            if int(time[1]) < 4:
                new.append('2' + time[1])
            else:
                new.append('1' + time[1])
        elif time[:2].endswith('?'):
            if int(time[0]) < 2:
                new.append(time[0] + '9')
            else:
                new.append(time[0] + '3')
        else:
            new.append(time[:2])

        new.append(':')

        if time[3] == '?':
            new.append('5')
        else:
            new.append(time[3])

        if time[4] == '?':
            new.append('9')
        else:
            new.append(time[4])
        return ''.join(new)


cases = [
    ("2?:?0", "23:50"),
    ("0?:3?", "09:39"),
    ("1?:22", "19:22"),
    ("??:??", "23:59"),
    ("2?:??", "23:59"),
    ("??:?9", "23:59"),
    ("?4:03", "14:03"),
    ("00:01", "00:01"),
]

sol = Solution()
for (time, exp) in cases:
    assert (
        got := sol.maximumTime(time)
    ) == exp, f"Failed case ({time}) - expecting ({exp}), got ({got})."
