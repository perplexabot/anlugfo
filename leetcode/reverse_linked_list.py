"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints:
    - The number of nodes in the list is the range [0, 5000].
    - -5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively.
    Could you implement both?

A:
    empty list (None)
        just return
    list of size one
        just return
    values can be none int?
        who cares
    reverse the

D:
    Input: head =   [1,2,3,4,5]
    prev = Null

    1.next = prev
    prev = 1

    2.next = prev
    prev = 2

    ...

    2.next = None, return

P:
    while curr:
        curr.next = prev
        prev = curr
        curr = curr.next

O:
    - one pass revert pointers O(n) for time O(1) for space
    - revert values (not pointers) O(n) for time O(n) for space

T:
    ([1,2,3,4,5], [5,4,3,2,1]),
    ([1,2], [2,1]),
    ([], []),
"""


def createLL(nums: list) -> ListNode:
    prev = None
    head = None
    for num in nums:
        curr = ListNode(num)
        if prev:
            prev.next = curr
        else:
            head = curr
        prev = curr
    return head


def LLtoList(nums: ListNode) -> list:
    lst = []
    curr = nums
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst


def printLL(head: ListNode):
    curr = head
    print(f"---", end="")
    while curr:
        print(f"{curr.val}", end=" ")
        curr = curr.next
    print()


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseListRec(self, head: ListNode | None) -> ListNode | None:
        def reverser(node: ListNode, prev: ListNode):
            if node:
                nextToReverse = node.next
                node.next = prev
                return reverser(nextToReverse, node)
            else:
                return prev

        return reverser(head, None)


cases = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], []),
]

sol = Solution()

for n, expected in cases:
    nums = createLL(n)
    h = sol.reverseList(nums)
    ans = LLtoList(h)

    assert ans == expected, f"Failed case ({n}) - expecting ({expected}), got ({ans})."
