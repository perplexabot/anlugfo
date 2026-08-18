"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
    Input: root = [1,2,3,null,5]
    Output: ["1->2->5","1->3"]

Example 2:
    Input: root = [1]
    Output: ["1"]

Constraints:
    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100

A:
    root is none -> return root
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        from collections import deque

        paths = []

        def dfs(curr, path):
            path.append(str(curr.val))
            if curr.left:
                dfs(curr.left, list(path))
            if curr.right:
                dfs(curr.right, list(path))
            if not curr.left and not curr.right:
                paths.append(path)

        if root:
            dfs(root, [])

        return ['->'.join(x) for x in paths]


cases = [
    (TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3)), ["1->2->5", "1->3"]),
    (TreeNode(1), ["1"]),
]

sol = Solution()
for ind, (root, exp) in enumerate(cases):
    assert (
        got := sol.binaryTreePaths(root)
    ) == exp, f"Failed case ({ind}) - expecting ({exp}), got ({got})."
