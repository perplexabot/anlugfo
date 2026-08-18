"""
You are given a positive integer num. You may swap any two digits of num that have the same parity
    (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

Example 1:
    Input: num = 1234
    Output: 3412
    Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
    Swap the digit 2 with the digit 4, this results in the number 3412.
    Note that there may be other sequences of swaps but it can be shown that 3412 is the largest
        possible number.
    Also note that we may not swap the digit 4 with the digit 1 since they are of different
        parities.

Example 2:
    Input: num = 65875
    Output: 87655
    Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
    Swap the first digit 5 with the digit 7, this results in the number 87655.
    Note that there may be other sequences of swaps but it can be shown that 87655 is the largest
        possible number.

Constraints:
    - 1 <= num <= 10**9

A:
    size of int is 1:
        return
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        from bisect import insort

        evens = []
        odds = []

        for i in str(num):
            if int(i) % 2 == 0:
                insort(evens, i)
            else:
                insort(odds, i)

        new = []
        for i in str(num):
            if int(i) % 2 == 0:
                new.append(evens.pop())
            else:
                new.append(odds.pop())
        return int(''.join(new))


cases = [(1234, 3412), (65875, 87655), (11, 11), (12, 12), (129, 921)]

sol = Solution()
for num, exp in cases:
    assert (
        got := sol.largestInteger(num)
    ) == exp, f"Failed case ({num}) - expecting ({exp}), got ({got})."
