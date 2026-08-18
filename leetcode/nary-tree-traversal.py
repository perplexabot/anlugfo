"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children
    is separated by the null value (See examples)

Example 1:
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [5,6,3,2,4,1]

Example 2:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,
                    null,14]
    Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    0 <= Node.val <= 104
    The height of the n-ary tree is less than or equal to 1000.

A:
    root is None -> return []

"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    from collections import deque

    def postorder(self, root: 'Node') -> List[int]:
        vals = []

        def traverse(root):
            if root.children:
                for child in root.children:
                    traverse(child)
            vals.append(root.val)

        if not root:
            return []

        traverse(root)
        return vals


case0 = Node(1, [Node(3, [Node(5, None), Node(6, None)]), Node(2, None), Node(4, None)])
case1 = Node(
    1,
    [
        Node(2, None),
        Node(3, [Node(6, None), Node(7, [Node(11, [Node(14, None)])])]),
        Node(4, [Node(8, [Node(12, None)])]),
        Node(5, [Node(9, [Node(13, None)]), Node(10, None)]),
    ],
)

cases = [
    (case0, [5, 6, 3, 2, 4, 1]),
    (case1, [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]),
    (None, []),
]

sol = Solution()
for (tree, exp) in cases:
    assert (
        got := sol.postorder(tree)
    ) == exp, f"Failed case ({tree}) - expecting ({exp}), got ({got})."
