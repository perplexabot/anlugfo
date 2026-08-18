"""
We have two special characters:
    - The first character can be represented by one bit 0.
    - The second character can be represented by two bits (10 or 11).

Given a binary array bits that ends with 0, return true if the last character must
    be a one-bit character.

Example 1:
    Input: bits = [1,0,0]
    Output: true
    Explanation: The only way to decode it is two-bit character and one-bit character.
    So the last character is one-bit character.

Example 2:
    Input: bits = [1,1,1,0]
    Output: false
    Explanation: The only way to decode it is two-bit character and two-bit character.
    So the last character is not one-bit character.

Constraints:
    1 <= bits.length <= 1000
    bits[i] is either 0 or 1.

A:
    arr of size 0 -> return false
    arr of size 1 -> return true
    arr of size 2 -> return true if 00 else false

D:
                   0 1 2 3
    Input: bits = [1,1,1,0]
        3 -> always good
        2 -> is a one so use index 1 also (11)
        0 -> not possible -> return false

                   0 1 2
    Input: bits = [1,0,0]
        2 -> always good
        1 -> either 1 char
            0 -> not possible -> return false
             or two chars with index 0 -> return true
"""

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            i += 1 if not bits[i] else 2
        return i == len(bits) - 1


cases = [([1, 0, 0], True), ([1, 1, 1, 0], False), ([0, 0], True)]

sol = Solution()
for bits, exp in cases:
    assert (
        got := sol.isOneBitCharacter(bits)
    ) == exp, f"Failed case ({bits}) - expecting ({exp}), got ({got})."
