"""
You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the diagonals of
    nums. In case, no prime is present on any of the diagonals, return 0.

Note that:
    - An integer is prime if it is greater than 1 and has no positive integer divisors other
        than 1 and itself.
    - An integer val is on one of the diagonals of nums if there exists an integer i for
        which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.

In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].

Example 1:
    Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
    Output: 11
    Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one
        of the diagonals. Since 11 is the largest prime, we return 11.

Example 2:
    Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
    Output: 17
    Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the
        diagonals. 17 is the largest prime, so we return 17.


Constraints:
    - 1 <= nums.length <= 300
    - nums.length == numsi.length
    - 1 <= nums[i][j] <= 4*10^6

A:
    empty matrix:
        return 0
    non sym matrix:
        assuming not possible
    matrix of size one
        return value

D:
    grab diagonals 
    grab max prime

P:
    get diagonals
        d0 = [A[i][i] for i in range(A[0])]
        d1 = [A[i][len(A[0]) - i - 1] for i in range(0, len(A[0]))]

    grab max of both diags

    use max to get all primes

    get intersection of diags and primes

    return max
"""

from typing import List


class Solution:
    def sieve(self, m: int) -> List[int]:
        n = m + 1
        A = [True for _ in range(n)]

        for i in range(2, int(n ** (1 / 2)) + 1):
            if A[i]:
                j = i**2
                cnt = 0
                while j < n:
                    A[j] = False
                    cnt += 1
                    j = (i**2) + (cnt * i)

        return set([i for i in range(len(A)) if A[i]]) - {0,1}

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        if not nums or not nums[0]:
            return 0

        ds = set(
            [nums[i][i] for i in range(len(nums[0]))]
            + [nums[i][len(nums[0]) - i - 1] for i in range(0, len(nums[0]))]
        )

        primes = self.sieve(max(ds))
        return max(primes.intersection(ds), default=0)


sol = Solution()

cases = [
    ([[1, 2, 3], [5, 6, 7], [9, 10, 11]], 11),
    ([[1, 2, 3], [5, 17, 7], [9, 11, 10]], 17),
    ([[1]], 0),
    ([[]], 0),
]

for case, exp in cases:
    assert (
        got := sol.diagonalPrime(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
