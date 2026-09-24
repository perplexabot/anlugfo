"""
You are given a positive integer n, that is initially placed on a board. Every day, for 10**9 days,
    you perform the following procedure:
    - For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
    - Then, place those numbers on the board.

Return the number of distinct integers present on the board after 10**9 days have elapsed.

Note:
    - Once a number is placed on the board, it will remain on it until the end.
    - % stands for the modulo operation. For example, 14 % 3 is 2.

Example 1:
    Input: n = 5
    Output: 4
    Explanation: Initially, 5 is present on the board.
    The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1.
    After that day, 3 will be added to the board because 4 % 3 == 1.
    At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5.

Example 2:
    Input: n = 3
    Output: 2
    Explanation:
    Since 3 % 2 == 1, 2 will be added to the board.
    After a billion days, the only two distinct numbers on the board are 2 and 3.

Constraints:
    - 1 <= n <= 100

A:
    n < 0
        not possible
    n = 0
        not possible
    n = 1
        return 1
    do we really have to run for 10**9 iterations?
        probably not

A:
    ?

D:
    n = 5
    new = [5]
    old = []

    5
        5 % 1 = 0
        5 % 2 = 1
        5 % 3 = 2
        5 % 4 = 1
        5 % 5 = 0
        new = [2, 4]
        old = [5]

    2
        2 % 1 = 0
        2 % 2 = 0
        2 % 3 = 2
        2 % 4 = 2
        2 % 5 = 2
        new = [4]
        old = [5,2]

    4
        4 % 1 = 0
        4 % 2 = 0
        4 % 3 = 1
        4 % 4 = 0
        4 % 5 = 4
        new = [3]
        old = [5,2,4]

    3
        3 % 1 = 0
        3 % 2 = 1
        3 % 3 = 0
        3 % 4 = 3
        3 % 5 = 3
        new = [0]
        old = [5,2,4,3]

    size of old = 4

P:
    new = set([n])
    old = set([])
    while new:
        e = new.pop()
        old.add(e)
        for i in range(1,n+1):
            if (i % e == 1):
                if i not in old:
                    new.add(i)
    return len(new)

O:
    return n - 1 is another way to do this...

T:
    (1,1)
    (2,1)
    (5,4)
    (3,2)

"""


class Solution:
    def distinctIntegers(self, n: int) -> int:
        new = set([n])
        old = set([])

        while new:
            old.add(e := new.pop())
            for i in range(1, n + 1):
                if e % i == 1:
                    if i not in old:
                        new.add(i)
        return len(old)


cases = [
    (2, 1),
    (5, 4),
    (3, 2),
    (1, 1),
]

sol = Solution()

for n, exp in cases:
    assert (
        got := sol.distinctIntegers(n)
    ) == exp, f"Whoopsie, failed case ({n}) - expecting ({exp}), got ({got})."
