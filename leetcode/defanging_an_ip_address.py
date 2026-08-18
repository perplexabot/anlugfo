"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"

Example 2:
    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"

Constraints:
    - The given address is a valid IPv4 address.

A:
    non valid ip
        not possible
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


cases = [
    ("1.1.1.1", "1[.]1[.]1[.]1"),
    ("255.100.50.0", "255[.]100[.]50[.]0"),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.defangIPaddr(case)
    ) == exp, f'Failed case ({case}) - expecting ({exp}), got ({got}).'
