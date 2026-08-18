"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of
    any two different nodes in the tree.

Example 1:
    Input: root = [4,2,6,1,3]
    Output: 1

Example 2:
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [2, 100].
    0 <= Node.val <= 10**5

Note:
    This question is the same as 530:
        https://leetcode.com/problems/minimum-absolute-difference-in-bst/

A:
    wtf does "between two nodes" mean?
        who knows
    no root (null tree)
        not possible
    single node
        not possible
    negative values
        not possible
A:
    ?
D:
    get nodes via bfs
    sort
    keep track of min while diffing every 2 adjacent elements
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from typing import Optional

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        def bfs(root):
            vals = []
            Q = deque([root])
            while Q:
                curr = Q.popleft()
                vals.append(curr.val)
                if curr.left:
                    Q.append(curr.left)
                if curr.right:
                    Q.append(curr.right)
            return vals

        mindiff = float('inf')
        vals_sorted = bfs(root)
        vals_sorted.sort()
        for i in range(1, len(vals_sorted)):
            mindiff = min(mindiff, vals_sorted[i] - vals_sorted[i - 1])
        return mindiff


cases = [
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6)), 1),
    (TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49))), 1),
    (TreeNode(1, TreeNode(1), TreeNode(48, TreeNode(12), TreeNode(49))), 0),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.minDiffInBST(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
