"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a
    product of two positive integers both smaller than it.)
Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
    Input: n = 5
    Output: 12
    Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the
        prime number 5 is at index 1.

Example 2:
    Input: n = 100
    Output: 682289015

Constraints:
    1 <= n <= 100

A:
    n = 0 -> not possible
    n = 1 -> 0
    n = 2 -> [2,1] ok, but [1,2] not

D:
    get number of primes in n = p
    permutations = n! * (n - p)!
"""


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        from math import factorial

        def getPrimes(x):
            primes = [True for _ in range(x + 1)]

            i = 2
            while i * i <= x:
                if primes[i]:
                    for j in range(i * i, x + 1, i):
                        primes[j] = False
                i += 1
            return primes

        primes_bool = getPrimes(n)
        prime_count = sum(primes_bool[2:])

        return (factorial(prime_count) * factorial(n - prime_count)) % (10**9 + 7)


sol = Solution()

cases = [
    (5, 12),
    (100, 682289015),
    (1, 1),
]

for (n, exp) in cases:
    assert (
        got := sol.numPrimeArrangements(n)
    ) == exp, f"Failed case ({n}) - expecting ({exp}), got ({got})."
