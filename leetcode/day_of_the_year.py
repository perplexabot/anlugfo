"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day
    number of the year.

Example 1:
    Input: date = "2019-01-09"
    Output: 9
    Explanation: Given date is the 9th day of the year in 2019.

Example 2:
    Input: date = "2019-02-10"
    Output: 41

Constraints:
    - date.length == 10
    - date[4] == date[7] == '-', and all other date[i]'s are digits
    - date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.

A:
    does year matter?
        no
    first day of year
        return 1
    last day of year
        return 365

A:
    ?

D:
    m = get month
    d = get day

    for i in range(1,m):
        ans += month_to_days[i]
    return ans += d
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        from datetime import datetime

        dobj = datetime.strptime(date, "%Y-%m-%d")
        return int(dobj.strftime("%j"))


cases = [
    ("2019-01-09", 9),
    ("2019-02-10", 41),
    ("2019-01-01", 1),
    ("2019-12-31", 365),
    ("2004-03-01", 61),
    ("2012-01-02", 2),
    ("1900-05-02", 122),
]

sol = Solution()
for date, exp in cases:
    assert (
        got := sol.dayOfYear(date)
    ) == exp, f"Failed case ({date}) - expecing ({exp}), got ({got})."
