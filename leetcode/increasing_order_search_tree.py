"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in
    the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:
    Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
    Input: root = [5,1,7]
    Output: [1,null,5,null,7]

Constraints:
    - The number of nodes in the given tree will be in the range [1, 100].
    - 0 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

A:
    empty tree
        return None
    equal values nodes, which is first?
        doesn't matter

D:
    traverse tree collecting nodes
    sort nodes
    reattach nodes
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        from collections import deque

        if not root:
            return None

        nodes = []

        def bfs(root):
            Q = deque([root])
            while Q:
                curr = Q.popleft()
                if curr.left:
                    Q.append(curr.left)
                if curr.right:
                    Q.append(curr.right)
                nodes.append(curr)

        bfs(root)
        nodes.sort(key=lambda x: x.val)

        for i in range(0, len(nodes)):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1] if i + 1 < len(nodes) else None

        return nodes[0]


t0 = TreeNode(
    5,
    TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)),
    TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))),
)

t1 = TreeNode(
    5,
    TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)),
    TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))),
)

sol = Solution()

for test in [t0, t1]:
    curr = sol.increasingBST(test)
    while curr:
        print(f"id={curr} val={curr.val}, left={curr.left}, right={curr.right}")
        curr = curr.right
    print('--')
