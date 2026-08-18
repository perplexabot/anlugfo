"""
There are numBottles water bottles that are initially full of water. You can exchange numExchange
    empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you
    can drink.

Example 1:
    Input: numBottles = 9, numExchange = 3
    Output: 13
    Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
    Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2:
    Input: numBottles = 15, numExchange = 4
    Output: 19
    Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
    Number of water bottles you can drink: 15 + 3 + 1 = 19.

Constraints:
    - 1 <= numBottles <= 100
    - 2 <= numExchange <= 100

A:
    numBottles == 0
        return 0

    numExchange > numBottles
        return numBottles

    numBottles == numExchange
        return numBottles + 1

    numExchange = 0
        not possible

    numEchange = 1
        not possible

D:
    Input: numBottles = 9, numExchange = 3,  drank = 0
        drink 9         empty 9     refresh (3full, 0empty)
        drink 9+3       empty 3     refresh (1full, 0empty)
        drink 9+3+1     empty 1     refresh (0full, 0empty)

    Input: numBottles = 15, numExchange = 4, drank = 0
                                            (empty // numExchange, empty -= full * numExchange)
        drink 15        empty 15    refresh (3full, 15-(3*4) empty = 3empty)
        drink 15+3      empty 6     refresh (1full, 6 - (4)  empty = 2empty)
        drink 15+3+1    empty 3     refresh (0full, 3 - (0)  empty = 3empty)

P:
    empty = 0
    drank = 0
    full = numBottles
    while full:
        # drink the fucking thing
        drank = full
        empty += full
        full = 0

        # exchange the fuckers
        full = empty // numExchange
        empty -= (full * numExchange)

"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        drank = 0
        fulls = numBottles

        while fulls:
            drank += fulls
            empty += fulls
            fulls = 0

            fulls = empty // numExchange
            empty -= fulls * numExchange
        return drank + fulls


sol = Solution()

cases = [
    (9, 3, 13),
    (15, 4, 19),
    (1, 2, 1),
    (2, 2, 3),
    (0, 3, 0),
    (3, 2, 5),
]

for numBottles, numExchange, exp in cases:
    assert (
        got := sol.numWaterBottles(numBottles, numExchange)
    ) == exp, f"Failed case ({numBottles}, {numExchange}) - expecting ({exp}), got ({got})."
