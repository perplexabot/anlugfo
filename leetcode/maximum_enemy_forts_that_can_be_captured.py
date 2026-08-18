"""
You are given a 0-indexed integer array forts of length n representing the positions of several forts.
    forts[i] can be -1, 0, or 1 where:
        - -1 represents there is no fort at the ith position.
        - 0 indicates there is an enemy fort at the ith position.
        - 1 indicates the fort at the ith the position is under your command.

Now you have decided to move your army from one of your forts at position i to an empty position j
    such that:
        - 0 <= i, j <= n - 1
        - The army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j),
            forts[k] == 0.

While moving the army, all the enemy forts that come in the way are captured.

Return the maximum number of enemy forts that can be captured. In case it is impossible to move your
    army, or you do not have any fort under your command, return 0.



Example 1:
    Input: forts = [1,0,0,-1,0,0,0,0,1]
    Output: 4
    Explanation:
    - Moving the army from position 0 to position 3 captures 2 enemy forts, at 1 and 2.
    - Moving the army from position 8 to position 3 captures 4 enemy forts.
    Since 4 is the maximum number of enemy forts that can be captured, we return 4.

Example 2:
    Input: forts = [0,0,1,-1]
    Output: 0
    Explanation: Since no enemy fort can be captured, 0 is returned.

Constraints:
    1 <= forts.length <= 1000
    -1 <= forts[i] <= 1

A:
    forts doesn't contain any 1s -> return 0
    forts doesn't contain any -1s -> return 0
    forts is of size <= 1 -> return 0

D:
    base_a = index of first 1 or -1
    base_b = base_a + 1

    max_cap = float('-inf')
    caps = 0
    while base_b < len(forts):
        if forts[base_b] + forts[base_a] == 0:
            max_cap = max(max_cap, caps)
            caps = 0
            base_a = base_b
            base_b = base_a + 1
        else:
            caps += 1
            base_b += 1
    return max_cap
"""

from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        if len(forts) < 2:
            return 0

        if 1 not in forts:
            return 0

        base_a = 0
        while base_a < len(forts):
            if forts[base_a] == 1 or forts[base_a] == -1:
                break
            base_a += 1
        base_b = base_a + 1

        max_cap = 0
        caps = 0
        while base_b < len(forts):
            if forts[base_a] + forts[base_b] == 0:
                max_cap = max(max_cap, caps)
                caps = 0
                base_a = base_b
                base_b = base_a + 1
            elif forts[base_b] == forts[base_a]:
                base_a = base_b
                base_b = base_a + 1
                caps = 0
            else:
                caps += 1
                base_b += 1

        return max_cap


cases = [
    ([1, 0, 0, -1, 0, 0, 0, 0, 1], 4),
    ([0, 0, 1, -1], 0),
    ([1, -1], 0),
    ([1], 0),
    ([-1], 0),
    ([0], 0),
    ([1, 0, -1], 1),
    ([1, 0, 0, -1], 2),
    ([-1, 0, 0, 1], 2),
    ([-1, 0, 1, 0, -1], 1),
    ([-1, 0, 0, 1, 0, 0, 0, -1], 3),
    ([1, 0, 0, -1, 0, 0, -1, 0, 0, 1], 2),
    ([0, -1, -1, 0, -1], 0),
    ([0, 0, 1, 0, 1, 1], 0),
    ([0, 0, 1, -1], 0),
]

sol = Solution()
for (forts, exp) in cases:
    assert (
        got := sol.captureForts(forts)
    ) == exp, f"Failed case ({forts}) - expecting ({exp}), got ({got})."
