"""
Given an integer n, return a string with n characters such that each character in such
    string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples
    valid strings, return any of them.

Example 1:
    Input: n = 4
    Output: "pppz"
    Explanation: "pppz" is a valid string since the character 'p' occurs three times and the
        character 'z' occurs once. Note that there are many other valid strings such as
        "ohhh" and "love".

Example 2:
    Input: n = 2
    Output: "xy"
    Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note
        that there are many other valid strings such as "ag" and "ur".

Example 3:
    Input: n = 7
    Output: "holasss"

Constraints:
    - 1 <= n <= 500

A:
    n = 0
        not possible
    n = 1
        return a char
    n = 2
        return 2 chars
    n is negative
        not possible

D:
    Input: n = 7
    n is odd: so odd + even = odd + odd + odd
    n i even: so odd + odd

    if n is even:
        split in half, if two new are odd, done
        if even, add 1 and sub 1 from halfs and intro 2 new chars

    if n is odd:
        return same char n times
"""

from collections import Counter


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return 'a' * n
        else:
            if (n / 2) % 2:
                return 'a' * (n // 2) + 'b' * (n // 2)
            else:
                return 'a' * ((n // 2) - 1) + 'b' * ((n // 2) + 1)


def check(potential_ans):
    c = Counter(potential_ans)
    return all([x % 2 for x in c.values()])


sol = Solution()

cases = [4, 2, 7, 1, 10]

for n in cases:
    c = check(ans := sol.generateTheString(n))
    print(f"Generated {ans} for {n}")
    assert c is True, f"Failed case ({n}) - generated ({ans})."
