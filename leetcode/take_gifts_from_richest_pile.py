"""
You are given an integer array gifts denoting the number of gifts in various piles. Every second,
    you do the following:
    - Choose the pile with the maximum number of gifts.
    - If there is more than one pile with the maximum number of gifts, choose any.
    - Leave behind the floor of the square root of the number of gifts in the pile. Take the rest
        of the gifts.

Return the number of gifts remaining after k seconds.

Example 1:
    Input: gifts = [25,64,9,4,100], k = 4
    Output: 29
    Explanation:
    The gifts are taken in the following way:
    - In the first second, the last pile is chosen and 10 gifts are left behind.
    - Then the second pile is chosen and 8 gifts are left behind.
    - After that the first pile is chosen and 5 gifts are left behind.
    - Finally, the last pile is chosen again and 3 gifts are left behind.
    The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.

Example 2:
    Input: gifts = [1,1,1,1], k = 4
    Output: 4
    Explanation:
    In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile.
    That is, you can't take any pile with you.
    So, the total gifts remaining are 4.

Constraints:
    1 <= gifts.length <= 10^3
    1 <= gifts[i] <= 10^9
    1 <= k <= 10^3

A:
    can list have none positive ints? no
    can k be none positive? no
    what if k>len(gifts)? doesn't matter
    can floor(squareroot(gifts[i])) will always return a positive

D:
    Input: gifts = [25,64,9,4,100], k = 4
    k = 1
        max(gifts) = 100, replace with floor(sq(100)) = 10, [25,64,9,4,10]
    k = 2
        max(gifts) = 64, replace with floor(sq(64)) = 8, [25,8,9,4,10]
    k = 3
        max(gifts) = 25, replace with floor(sq(25)) = 5, [5,8,9,4,10]
    k = 4
        max(gifts) = 10, replace with floor(sq(10)) = 3, [5,8,9,4,3]
    return sum([5,8,9,4,3]) = 29

below sol:
    O(k * n)
"""

from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            max_ind, max_val = max(enumerate(gifts), key=lambda x: x[1])
            fl_sq = max_val ** (1 / 2) // 1
            gifts[max_ind] = fl_sq
        return int(sum(gifts))


cases = [([25, 64, 9, 4, 100], 4, 29), ([1, 1, 1, 1], 4, 4), ([1], 10, 1)]

sol = Solution()
for gifts, k, exp in cases:
    assert (
        got := sol.pickGifts(gifts, k)
    ) == exp, f"Failed case ({case}), expecting ({exp}), got ({got})."
