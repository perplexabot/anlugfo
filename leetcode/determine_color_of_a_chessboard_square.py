"""
You are given coordinates, a string that represents the coordinates of a square of the chessboard.
    Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have
    the letter first, and the number second.

Example 1:
    Input: coordinates = "a1"
    Output: false
    Explanation: From the chessboard above, the square with coordinates "a1" is black, so
        return false.

Example 2:
    Input: coordinates = "h3"
    Output: true
    Explanation: From the chessboard above, the square with coordinates "h3" is white, so
        return true.

Example 3:
    Input: coordinates = "c7"
    Output: false

Constraints:
    - coordinates.length == 2
    - 'a' <= coordinates[0] <= 'h'
    - '1' <= coordinates[1] <= '8'


A:
    board always same size
        yes
    coords always valid?
        yes

D:
    h3:
        a = b
        b = w
        c = b
        d = w
        e = b
        f = w
        g = b
        h = w

        1 = w
        2 = b
        3 = w

        or

        h = 8, 7 steps is odd so color flip
        1 = 1, 2 steps is even so color stays

P:
    start_number = 0
    start_color = black
    for letter in a->h
        
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        ans = False

        conv = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        let = coordinates[0]
        num = coordinates[1]

        # moving from 'a'
        let_dist = conv[let] - 1
        if let_dist % 2:
            ans = not ans

        # moving from '1'
        num_dist = int(num) - 1
        if num_dist % 2:
            ans = not ans

        return ans


sol = Solution()

cases = [
    ("a1", False),
    ("h3", True),
    ("c7", False),
]

for coor, exp in cases:
    assert (
        got := sol.squareIsWhite(coor)
    ) == exp, f"Failed case ({coor}) - expecting ({exp}), got ({got})."
