"""
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from
    either 0 to 1 or 1 to 0.

    - For example, for x = 7, the binary representation is 111 and we may choose any bit
        (including any leading zeros not shown) and flip it. We can flip the first bit
        from the right to get 110, flip the second bit from the right to get 101, flip the fifth
        bit from the right (a leading zero) to get 10111, etc.

Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

Example 1:
    Input: start = 10, goal = 7
    Output: 3
    Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively.
        We can convert 10 to 7 in 3 steps:
        - Flip the first bit from the right: 1010 -> 1011.
        - Flip the third bit from the right: 1011 -> 1111.
        - Flip the fourth bit from the right: 1111 -> 0111.
        It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

Example 2:
    Input: start = 3, goal = 4
    Output: 3
    Explanation: The binary representation of 3 and 4 are 011 and 100 respectively.
    We can convert 3 to 4 in 3 steps:
        - Flip the first bit from the right: 011 -> 010.
        - Flip the second bit from the right: 010 -> 000.
        - Flip the third bit from the right: 000 -> 100.
        It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.

Constraints:
    - 0 <= start, goal <= 109

A:
    start of goal is empty or non int
        no
    goal or start is negative?
        no
    they are already the same
        return 0
    all different
        who cares

D:
    Input: start = 10, goal = 7
    10 ^ 7 = 13 = 0b1101. 3 ones = 3 bit diffs

P:
    time comp: O(b), where b is the bit size of the larger input (goal, target)
    spac comp: O(1)

O:
    bit_count()

T:

    10, 7, 3
    3, 4, 3
    7, 1, 2
    1, 7, 2
    7, 2, 2
    7, 0, 3
    32, 1, 4
"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return f"{start ^ goal:0b}".count('1')


cases = [
    ((10, 7), 3),
    ((3, 4), 3),
    ((7, 1), 2),
    ((1, 7), 2),
    ((7, 2), 2),
    ((7, 0), 3),
    ((32, 1), 2),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.minBitFlips(*case)
    ) == expected, f"Failed case ({case}) - expecting ({expected}), got ({got})."
