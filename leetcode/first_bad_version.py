"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the
    latest version of your product fails the quality check. Since each version is developed based on
        the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes
    all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a
    function to find the first bad version. You should minimize the number of calls to the API.



Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

Example 2:
    Input: n = 1, bad = 1
    Output: 1

Constraints:
    1 <= bad <= n <= 2**31 - 1

A:
    all bad versions:
        return 0

    no bad versions:
        always one exists

    list of size 0:
        assume never the case

    list of size 1:
        return 0

    list of size 2:
        solve

A:
    ?

D:
    n = 5, bad = 4

     0 1 2 3 4
    [1,2,3,4,5]

    start = 0
    end = n - 1 = 4
    mid = start + ((end - start) // 2) = 2
    isbad(mid) = false

    start = mid = 2
    end = end = 4
    mid = start((end - start) // 2) = 2 + 1 = 3
    isbad(mid) = true
    isbad(mid - 1) = false
    return 4

    n = 10, bad = 8

     0 1 2 3 4 5 6 7 8 9
    [1,2,3,4,5,6,7,8,9,10]

    start = 0, end = n - 1 = 9, mid = start + ((end - start)//2) = 0 + ((9 - 0)//2) = 0 + (4) = 4
    isbad(mid) = false, move right
    start = mid, end = end, mid = 

P:
    start = 0, end = n -1, mid = (end-start)//2
    while True:
        if isBad(mid):
            if not isBad(mid-1):
                return mid -1
            end = mid
            start = start
        else:
            start = mid
            end = end
        mid = start + ((end - start) // 2)

"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def isBadVersion(n: int) -> bool:
    if n == 1:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1

        start = 0
        end = n - 1
        mid = (end - start) // 2
        while True:
            if isBadVersion(mid + 1):
                if not isBadVersion(mid):
                    return mid + 1
                end = mid
            else:
                start = mid + 1
            mid = start + ((end - start) // 2)


sol = Solution()
assert (got := sol.firstBadVersion(1)) == 1, "Failed case"
