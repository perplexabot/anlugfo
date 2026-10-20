"""
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn,
    that player makes a move consisting of:
        - Choosing any integer x with 0 < x < n and n % x == 0.
        - Replacing the number n on the chalkboard with n - x.

Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:
    Input: n = 2
    Output: true
    Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:
    Input: n = 3
    Output: false
    Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

Constraints:
    - 1 <= n <= 1000

A:
    initial n has no x (n=1)?
        return False (alice not able to make a play)
    n can be float?
        assuming no
    is taking the largest factor the optimal move?


D:
    n = 10
    alice:
        chooses largest x (5) such that n % x == 0
    n = 5
    bob:
        chooses largest x (1) such that n % x == 0
    n = 4
    alice:
        chooses largest x (2) such that n % x == 0
    n = 2
    bob:
        chooses largest x (1) such that n % x == 0
    n = 1
        alice loses
    return true

P:
    for current n:
        find largest factor < n:
        if none exist, current person loses break
        n -= x

O:


T:
    2, true
    3, false
    10, false
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

sol = Solution()

cases = [
    (2, True),
    (3, False),
    (10, True),
    (1, False),
    (6, True),
    (4, True),
]

for n, expected in cases:
    assert (
        got := sol.divisorGame(n)
    ) == expected, f"Failed case ({n}) - expecting ({expected}), got ({got})."
