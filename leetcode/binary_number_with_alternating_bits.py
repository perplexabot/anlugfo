"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will
    always have different values.

Example 1:
    Input: n = 5
    Output: true
    Explanation: The binary representation of 5 is: 101

Example 2:
    Input: n = 7
    Output: false
    Explanation: The binary representation of 7 is: 111.

Example 3:
    Input: n = 11
    Output: false
    Explanation: The binary representation of 11 is: 1011.

Constraints:
    - 1 <= n <= 2**31 - 1

A:
    cannot be negative or 0
    is 00110011 alternating?
        no
    is 0 or 1 alternating
        yes
    does an input of 05 count as 5?
        yes (no such input)

D:
    5 = 0b101
      xor 101
          or
      xor 010
          ---
          000

P:
    if n < 10:
        always alternating
    else:
        a,b = generate alternating numbers
        return n in set(a,b)


O:
    get number of digits (D) using math (vs strcnt)
    creating a alternating bit string
    time complexity = time creating/finding alternating
        O(n/2)
    space complexity = O(1)

T:
    1 true
    0 true
    2 true
    3 false
    5 true
    7 false
    11 false
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n < 3:
            return True
        b = 1
        while b < n:
            b <<= 1
            if b & 3 == 0:
                b += 1
        a = b >> 2
        return a == n or b == n


cases = [
    (0, True),
    (1, True),
    (2, True),
    (3, False),
    (5, True),
    (7, False),
    (11, False),
    (841395, False),
    (170, True),
    (85, True),
]

sol = Solution()
for n, expected in cases:
    print(f"Testing {n}")
    assert (
        got := sol.hasAlternatingBits(n)
    ) == expected, f"Failed case ({n}) - expecting ({expected}), got ({got})."
