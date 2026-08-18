"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
    Input: root = [1,2]
    Output: 1

Constraints:
    - The number of nodes in the tree is in the range [1, 104].
    - -100 <= Node.val <= 100
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.test = 0

        def dfs(node):
            if not node:
                return 0

            a0 = dfs(node.left)
            a1 = dfs(node.right)
            self.test = max(self.test, a0 + a1)
            return 1 + max(a0, a1)

        dfs(root)

        return self.test

        # def dfs(node):
        #    if not node.left and not node.right:
        #        return 0
        #    elif not node.left:
        #        return 1 + dfs(node.right)
        #    elif not node.right:
        #        return 1 + dfs(node.left)
        #    else:
        #        return 1 + max(dfs(node.left), dfs(node.right))

        # return dfs(root)


T0 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
T1 = TreeNode(1, TreeNode(2))
T2 = TreeNode(1)

cases = [(T0, 3), (T1, 1), (T2, 0)]

sol = Solution()
for root, exp in cases:
    assert (
        got := sol.diameterOfBinaryTree(root)
    ) == exp, f"Failed case ({root}) - expecting ({exp}), got ({got})"
