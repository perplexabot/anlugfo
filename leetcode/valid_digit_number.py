"""You are given an integer n and a digit x.

A number is considered valid if:
    - It contains at least one occurrence of digit x, and
    - It does not start with digit x.

Return true if n is valid, otherwise return false.

Example 1:
    Input: n = 101, x = 0
    Output: true
    Explanation:
        The number contains digit 0 at index 1. It does not start with 0, so it satisfies both
            conditions. Thus, the answer is true.

Example 2:
    Input: n = 232, x = 2
    Output: false
    Explanation:
        The number starts with 2, which violates the condition. Thus, the answer is false.

Example 3:
    Input: n = 5, x = 1
    Output: false
    Explanation:
        The number does not contain digit 1. Thus, the answer is false.

Constraints:
    - 0 <= n <= 10**5
    - 0 <= x <= 9

AADPOCT

A:
    can n be none int?
        no
    can x be none int?
        whocares
    can n start with 0 (e.g 05353)
        no
    can x be 0
        yes, in which case don't need to check til most sig digit
    can x be negative
        no

A:

D:
    Input: n = 232, x = 2

    t = 232
    good = False

    last = None
    t % 10 = 2, 2 =? x -> yes, good = True, last = True
    t //= 10 = 23

    last = None
    t % 10 = 3, 2 =? x -> no, last = False
    t //= 10 = 2

    last = None
    t % 10 = 2, 2 =? 2 -> yes, good = True, last = True

    return not last and good

P:
    good = False
    while n:
        i = n % 10

        last = False
        if i == x:
            good = True
            last = True

        n //= 10

    return good and not last

O:

T:
    (0,1, True),
    (0,0, True),
    (11,1, False),
    (12,1, False),
    (12,2, True),
    (11112, 2, True),
    (11112, 1, False),
    (12222, 1, False),
    (12222, 2, True),
    (12221, 1, False),
    (12221, 2, True),
    (101, 0 ,true),
    (232, 2 ,false),
    (5, 1 ,false),
"""


class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        valid = False
        while n:
            i = n % 10

            last = False
            if i == x:
                valid = True
                last = True

            n //= 10
        return valid and not last


cases = [
    (0, 1, False),
    (0, 0, False),
    (11, 1, False),
    (12, 1, False),
    (12, 2, True),
    (11112, 2, True),
    (11112, 1, False),
    (12222, 1, False),
    (12222, 2, True),
    (12221, 1, False),
    (12221, 2, True),
    (101, 0, True),
    (232, 2, False),
    (5, 1, False),
]

sol = Solution()
for n, x, exp in cases:
    assert (
        got := sol.validDigit(n, x)
    ) == exp, f"Woops, failed ({n}, {x}) - expecting ({exp}), got ({got})."
