"""
The Hamming distance between two integers is the number of positions at which the corresponding
    bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:
    Input: x = 1, y = 4
    Output: 2
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
    The above arrows point to positions where the corresponding bits are different.

Example 2:
    Input: x = 3, y = 1
    Output: 1

Constraints:
    - 0 <= x, y <= 2**31 - 1

A:
    none int
        not possible
    negative numbers
        not possible
    bits in one number more than the other
        possible, just count extra ones

D:

    x = 7, y = 34

    7  = 0 0 0 1 1 1
    34 = 1 0 0 0 1 0
         x     x   x

    return 3

P:
    dist = 0
    for i,j in zip_longest(f"{x:b}", f"{y:b}", fillvalue=0):
        if i != j
            dist += 1
    return dist

O:
    Possible to do this with xor?
        x = 7, y = 34, x ^ y = 37, 37b10 = 100101b2, count 1s in 100101b2

T
    1, 4, 2
    3, 1, 1
    7, 34, 3

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return f"{x ^ y:b}".count("1")


cases = [
    (1, 4, 2),
    (3, 1, 1),
    (7, 34, 3),
]

sol = Solution()
for x, y, exp in cases:
    assert (
        got := sol.hammingDistance(x, y)
    ) == exp, f"Woops! Failed case ({x}, {y}) - expecting ({exp}), got ({got})."
