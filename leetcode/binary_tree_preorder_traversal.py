"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,2,3]

Example 2:
    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    Output: [1,2,4,5,6,7,3,8,9]

Example 3:
    Input: root = []
    Output: []

Example 4:
    Input: root = [1]
    Output: [1]

Constraints:
    - The number of nodes in the tree is in the range [0, 100].
    - -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
    likely using a stack

A:
    root = NULL
        possible
    root has no children
        possible, return head value

D:
    1
  2   3
4  7

P:
    ret = []
    dfs(node):
        ret.append(node.value);
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)

O:
    none recursive version doesnt make use of memory stack

    stack = [node.head]
    while (stack):
        curr = stack.pop()
        ret.append(curr)
        if curr.left:
            ret.append(curr.left)
        if curr.right:
            ret.append(curr.right)

T:
    TreeNode(1, right=TreeNode(2, TreeNode(3))),
    TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
        TreeNode(3, right=TreeNode(8, right=TreeNode(9))))
    TreeNode(1)
    TreeNode(1, TreeNode(2), TreeNode(3))
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        d = deque()
        d.append(root)
        ret = []
        while d:
            curr = d.pop()
            ret.append(curr.val)
            if curr.right:
                d.append(curr.right)
            if curr.left:
                d.append(curr.left)
        return ret


cases = [
    (TreeNode(1, right=TreeNode(2, TreeNode(3))), [1, 2, 3]),
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
            TreeNode(3, right=TreeNode(8, right=TreeNode(9))),
        ),
        [1, 2, 4, 5, 6, 7, 3, 8, 9],
    ),
    (TreeNode(1), [1]),
    (TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3]),
    (None, []),
]

sol = Solution()
for ind, (case, expected) in enumerate(cases):
    assert (
        got := sol.preorderTraversal(case)
    ) == expected, f"Failed case ({ind}) - expecting ({expected}), got ({got})."
