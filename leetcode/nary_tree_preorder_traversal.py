"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children
    is separated by the null value (See examples)

Example 1:
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,3,5,6,2,4]

Example 2:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,
        null,12,null,13,null,null,14]
    Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    0 <= Node.val <= 104
    The height of the n-ary tree is less than or equal to 1000.


A:
    root is none -> return []

D:
    out = []
    Q = [root]
    while Q:
        curr = Q.pop()
        out.pushleft(curr.children)
    return out
"""

from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        from collections import deque

        out = []
        Q = deque([root])
        while Q:
            curr = Q.popleft()
            if curr:
                out.append(curr.val)
                if curr.children:
                    Q.extendleft(curr.children[::-1])
        return out


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


case0 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
case1 = Node(
    1,
    [
        Node(2),
        Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
        Node(4, [Node(8, [Node(12)])]),
        Node(5, [Node(9, [Node(13)]), Node(10)]),
    ],
)

cases = [
    (case0, [1, 3, 5, 6, 2, 4]),
    (case1, [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]),
    ([], []),
]

sol = Solution()
for (case, exp) in cases:
    assert (
        got := sol.preorder(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
