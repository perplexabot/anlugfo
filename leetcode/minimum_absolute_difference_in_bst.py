"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the
    values of any two different nodes in the tree.

Example 1:
    Input: root = [4,2,6,1,3]
    Output: 1

Example 2:
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

Constraints:
    - The number of nodes in the tree is in the range [2, 104].
    - 0 <= Node.val <= 10**5

Note: This question is the same as 783:
    https://leetcode.com/problems/minimum-distance-between-bst-nodes/

A:
    empty tree:
        not possible
    tree with oe node:
        not possible

D:
    in order traversal
    go through list looking at consequtive diffs, keep track of min
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        elems = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            elems.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)

        min_diff = float('inf')
        for i in range(1, len(elems)):
            min_diff = min(abs(elems[i] - elems[i - 1]), min_diff)

        return min_diff


tree0 = TreeNode(5, TreeNode(4), TreeNode(7))

sol = Solution()
print(sol.getMinimumDifference(tree0))
