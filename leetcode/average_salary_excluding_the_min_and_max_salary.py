"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within
    10-5 of the actual answer will be accepted.



Example 1:
    Input: salary = [4000,3000,1000,2000]
    Output: 2500.00000
    Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
        Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:
    Input: salary = [1000,2000,3000]
    Output: 2000.00000
    Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
        Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

Constraints:
    - 3 <= salary.length <= 100
    - 1000 <= salary[i] <= 10**6
    - All the integers of salary are unique.

A:
    len of arr <= 2?
        not possible
    negatives
        nope
    def of ave post removal
        assuming typical ave

D:
    Input: salary = [4000,3000,1000,2000]
    sum = 0
    maxi = 0
    mini = 10**6
    sum += 4000, mini = maxi = 4000
    sum += 3000, mini = 3000
    sum += 1000, mini = 1000
    sum += 2000
    ave = (sum - maxi - mini) / (len(salary) - 2) = 2500

P:
    sum = 0
    mina = 10**6
    maxa = 0
    for s in salary:
        set mina if smallest
        set maxa if largest
        sum += s
    return (s - mina - maxa) / (len(s) -  2)

O:
    time complexity: O(n)
    spac complexity: O(1)

T:
    ([4000,3000,1000,2000],2500.00000),
    ([1000,2000,3000],2000.00000),
"""


class Solution:
    def average(self, salary: list[int]) -> float:
        m = 0
        mina = float('inf')
        maxa = 0
        for s in salary:
            maxa = s if s > maxa else maxa
            mina = s if s < mina else mina
            m += s
        return (m - mina - maxa) / (len(salary) - 2)


# OR
#    def averageOne(self, salary: list[int]) -> float:
#        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


cases = [
    ([4000, 3000, 1000, 2000], 2500.00000),
    ([1000, 2000, 3000], 2000.00000),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.average(case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
