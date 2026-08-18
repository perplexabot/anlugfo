"""
You are given a string of length 5 called time, representing the current time on a digital clock in
    the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is
    "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a
    digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing
    every ? with a digit from 0 to 9.

Example 1:
    Input: time = "?5:00"
    Output: 2
    Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00".
        Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we
        have two choices.
Example 2:
    Input: time = "0?:0?"
    Output: 100
    Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
Example 3:
    Input: time = "??:??"
    Output: 1440
    Explanation: There are 24 possible choices for the hours, and 60 possible choices for the
        minutes. In total, we have 24 * 60 = 1440 choices.

Constraints:
    - time is a valid string of length 5 in the format "hh:mm".
    - "00" <= hh <= "23"
    - "00" <= mm <= "59"
    - Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9.

A:
    string not of size 5
        not possible
    more than one ?
        yes
    no ?
        yes
    format of time?
        24hr

D:
    H,M = time.split(':')
    Input: time = "0?:0?"
    H = 0?
    hways = 1
    H1 == ?
        hways *= 10 hit
    H0 == ?
        if H1 > 3:
            hways *= 2
        else:
            hways *= 3
    hways = 10

    M = 0?
    mways = 1
    M1 == ?
        mways *= 10 hit
    M0 == ?
        mways *= 6
    mways = 10

    return mways * hways
"""


class Solution:
    def countTime(self, time: str) -> int:
        h, m = time.split(':')
        hways, mways = 1, 1

        if h == "??":
            hways = 24
        else:
            if h[1] == '?':
                hways *= 10 if int(h[0]) < 2 else 4
            if h[0] == '?':
                hways *= 2 if int(h[1]) > 3 else 3

        if m[1] == '?':
            mways *= 10
        if m[0] == '?':
            mways *= 6

        return mways * hways


sol = Solution()

cases = [
    ("?5:00", 2),
    ("2?:??", 240),
    ("12:00", 1),
    ("0?:0?", 100),
    ("??:??", 1440),
]

for time, exp in cases:
    assert (
        got := sol.countTime(time)
    ) == exp, f"Failed case ({time}) - expecting ({exp}), got ({got})."
