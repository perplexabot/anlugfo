"""
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and
    death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is
    counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that
    the person is not counted in the year that they die.

Return the earliest year with the maximum population.

Example 1:
    Input: logs = [[1993,1999],[2000,2010]]
    Output: 1993
    Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

Example 2:
    Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
    Output: 1960
    Explanation:
    The maximum population is 2, and it had happened in years 1960 and 1970.
    The earlier year between them is 1960.

Constraints:
    1 <= logs.length <= 100
    1950 <= birthi < deathi <= 2050

A:
    empty subarray -> assume not possible
    empty array -> not possible
    death year before born year, not possible
    death year at born year -> not possible

A: ?

D:
    years = {}
    logs = [[1950,1961],[1960,1971],[1970,1981]]
        [1950,1961] -> years[1950] += 1, years[1951] += 1 ... years[1960] += 1
        [1960,1971] -> years[1960] += 1, years[1961] += 1 ... years[1970] += 1
    return max(years)

"""

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        from collections import defaultdict

        year_histo = defaultdict(int)
        for log in logs:
            for year in range(*log):
                year_histo[year] += 1

        print(year_histo)
        return min([year for year in year_histo if year_histo[year] == max(year_histo.values())])


cases = [([[1993, 1999], [2000, 2010]], 1993), ([[1950, 1961], [1960, 1971], [1970, 1981]], 1960)]

sol = Solution()
for (logs, exp) in cases:
    assert (
        got := sol.maximumPopulation(logs)
    ) == exp, f"Failed case ({logs}) - expecting ({exp}), got ({got})."
