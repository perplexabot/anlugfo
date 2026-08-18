"""
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
    representing the color of the ith block. The characters 'W' and 'B' denote the colors
    white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k
    consecutive black blocks.

Example 1:
    Input: blocks = "WBBWWBBWBW", k = 7
    Output: 3
    Explanation:
    One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
    so that blocks = "BBBBBBBWBW".
    It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3
        operations.
    Therefore, we return 3.

Example 2:
    Input: blocks = "WBWBBBW", k = 2
    Output: 0
    Explanation:
    No changes need to be made, since 2 consecutive black blocks already exist.
    Therefore, we return 0.

Constraints:
    - n == blocks.length
    - 1 <= n <= 100
    - blocks[i] is either 'W' or 'B'.
    - 1 <= k <= n

A:
    blocks size == 0:
        not possible
    k > block size:
        not possible
    blocks size == 1:
        return 0 if k == 0 else check
    k == 0:
        not possible
    k == 1:
        if B present return 0 else 1
    k == 2:
        if B present return 0 if B next to it else 1
        if B not present return 2
    worst case is k flips

D:
    Input: blocks = "WBWBBBW", k = 2
    len(blocks) = 7

    WBWBBBW
    ..      1
     ..     1
      ..    1
       ..   0 return 0

"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        return (
            k - blocks.count('B')
            if k == len(blocks)
            else min([k - blocks[i : i + k].count('B') for i in range(len(blocks) - k + 1)])
        )


cases = [
    ("WBBWWBBWBW", 7, 3),
    ("WBWBBBW", 2, 0),
    ("W", 1, 1),
    ("BB", 1, 0),
    ("BB", 2, 0),
    ("WB", 1, 0),
    ("BW", 1, 0),
    ("BW", 2, 1),
    ("WB", 2, 1),
    ("WW", 1, 1),
    ("WW", 2, 2),
]

sol = Solution()
for block, k, exp in cases:
    assert (
        got := sol.minimumRecolors(block, k)
    ) == exp, f"Failed case ({block}, {k}) - expecting ({exp}), got ({got})."
