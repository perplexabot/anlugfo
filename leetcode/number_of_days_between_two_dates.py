"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
    Input: date1 = "2019-06-29", date2 = "2019-06-30"
    Output: 1

Example 2:
    Input: date1 = "2020-01-15", date2 = "2019-12-31"
    Output: 15

Constraints:
    - The given dates are valid dates between the years 1971 and 2100.

A:
    date 1 always after date 2?
        no, need to find bigger
    date 1 == to date 2
        possible
    leap years?
        divisible by 4 but not by 100

D:
    "2020-01-15", "2019-12-31"
    year diff > 1? no, so find months left
    month diff > 1?, no so find days left
    days diff = 15

P:
    D = d0 - d1 in years
    if full years exist in between d0 and d1 such that D >= 1:
        smaller year's days to complete year
            +
        bigger year's days to reach day
            +
        number of full years * (365 or 366)
    if D < 1:
        if on different years:
            smaller year's days to complete year
                +
            bigger year's days to reach day
        if on same year:
            days in year - smaller years days to complete - bigger years days to reach day
O:
    could use datettime

T:
    "2019-06-29", "2019-06-30", 1
    "2019-06-30", "2019-06-29", 1
    "2020-01-15", "2019-12-31", 15
    "2019-12-31", "2020-01-15", 15
    "2021-01-01", "2022-01-02", 365
    "2020-01-01", "2022-05-12", 862
    "1970-01-23", "2026-01-01", 20432
"""

class Solution:
    def isleap(self, year: int) -> bool:
        y = int(year)
        if (y % 400 == 0):
            return True
        if (y % 100 == 0):
            return False
        if (y % 4 == 0):
            return True

    def daysInMonth(self, m, leap):
        monthDays = {
                1: 31 ,
                2: 28 ,
                3: 31 ,
                4: 30 ,
                5: 31 ,
                6: 30 ,
                7: 31 ,
                8: 31 ,
                9: 30 ,
                10: 31 ,
                11: 30 ,
                12: 31 ,
        }
        return 1 + monthDays[m] if leap and m == 2 else monthDays[m]

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 == date2:
            return 0
        
        # get bigger date
        y1,m1,d1 = [int(x) for x in date1.split('-')]
        y2,m2,d2 = [int(x) for x in date2.split('-')]
        dateHelper = {
            date1: {'day': d1, 'month': m1, 'year': y1},
            date2: {'day': d2, 'month': m2, 'year': y2},
        }

        if y1 > y2:
            biggerDate = date1
            smallerDate = date2
        elif y1 < y2:
            biggerDate = date2
            smallerDate = date1
        else:
            if m1 > m2:
                biggerDate = date1
                smallerDate = date2
            elif m1 < m2:
                biggerDate = date2
                smallerDate = date1
            else:
                if d1 > d2:
                    biggerDate = date1
                    smallerDate = date2
                else:
                    biggerDate = date2
                    smallerDate = date1

        total = 0

        if abs(y1-y2) >= 1:
            # years in between
            for y in range(dateHelper[smallerDate]['year'] + 1, dateHelper[biggerDate]['year']):
                total += 366 if self.isleap(y) else 365

            # smaller date to end of year
            total += self.daysInMonth(dateHelper[smallerDate]['month'], self.isleap(dateHelper[smallerDate]['year'])) - dateHelper[smallerDate]['day'] - 1
            for m in range(dateHelper[smallerDate]['month'] + 1, 13):
                total += self.daysInMonth(m,self.isleap(dateHelper[smallerDate]['year']))

            # days to reach bigger date from start of year
            total += dateHelper[biggerDate]['day'] + 1
            for m in range(1, dateHelper[biggerDate]['month']):
                total += self.daysInMonth(m,self.isleap(dateHelper[biggerDate]['year']))
            return total
        else:
            # total days in year
            leap = self.isleap(y1)
            total = sum(self.daysInMonth(m,leap) for m in range(1,13))

            # remove smaller date to end of year
            total -= self.daysInMonth(dateHelper[smallerDate]['month'], self.isleap(dateHelper[smallerDate]['year'])) - dateHelper[smallerDate]['day'] - 1
            for m in range(dateHelper[smallerDate]['month'] + 1, 13):
                total -= self.daysInMonth(m,self.isleap(dateHelper[smallerDate]['year']))

            # remove days to reach bigger date from start of year
            total -= self.daysInMonth(dateHelper[biggerDate]['month'], self.isleap(dateHelper[biggerDate]['year'])) - 1
            for m in range(1, dateHelper[biggerDate]['month']):
                total -= self.daysInMonth(m,self.isleap(dateHelper[biggerDate]['year']))

        return total

cases = [
    ("2019-06-29", "2019-06-30", 1),
    ("2019-06-30", "2019-06-29", 1),
    ("2020-01-15", "2019-12-31", 15),
    ("2019-12-31", "2020-01-15", 15),
    ("2021-01-01", "2022-01-02", 366),
    ("2020-01-01", "2022-05-12", 862),
    ("1970-01-23", "2026-01-01", 20432),
]

sol = Solution()

for (d0, d1, expected) in cases:
    print(f"doing {d0} and {d1}")
    assert (got:=sol.daysBetweenDates(d0, d1)) == expected, f"Failed case ({d0}, {d1}) - expecting ({expected}), got ({got})."
