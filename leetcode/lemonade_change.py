"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and
    order one at a time (in the order specified by bills). Each customer will only buy one lemonade
    and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer
    so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you
    can provide every customer with the correct change, or false otherwise.

Example 1:
    Input: bills = [5,5,5,10,20]
    Output: true
    Explanation:
    From the first 3 customers, we collect three $5 bills in order.
    From the fourth customer, we collect a $10 bill and give back a $5.
    From the fifth customer, we give a $10 bill and a $5 bill.
    Since all customers got correct change, we output true.

Example 2:
    Input: bills = [5,5,10,10,20]
    Output: false
    Explanation:
    From the first two customers in order, we collect two $5 bills.
    For the next two customers in order, we collect a $10 bill and give back a $5 bill.
    For the last customer, we can not give the change of $15 back because we only have two $10
        bills.
    Since not every customer received the correct change, the answer is false.

Constraints:
    - 1 <= bills.length <= 10**5
    - bills[i] is either 5, 10, or 20.

A:
    empty bills arr:
        return True
    arr of size 1:
        return True if 5

D:
    for b in bills:
        if b == 5:
            change.update([5])
        if b == 10:
            if change[5]:
                change.subtract([5])
                change.update([10])
            else:
                return False
        if b == 20:
            if change[5] and change[10]
                change.subtract([5,10])
                change.update([20])
            elif change[5] > 2:
                change.subtract([5,5])
                change.update([20])
            else:
                return False
    return True
"""

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        from collections import Counter

        change = Counter()
        for b in bills:
            if b == 5:
                change.update([5])
            if b == 10:
                if change[5] > 0:
                    change.subtract([5])
                    change.update([10])
                else:
                    return False
            if b == 20:
                if change[5] > 0 and change[10] > 0:
                    change.subtract([5, 10])
                    change.update([20])
                elif change[5] > 2:
                    change.subtract([5, 5, 5])
                    change.update([20])
                else:
                    return False
        return True


cases = [
    ([5, 5, 5, 10, 20], True),
    ([5, 5, 10, 10, 20], False),
    ([5], True),
    ([10], False),
    ([20], False),
    ([20, 10], False),
    ([5, 10], True),
    ([5, 20], False),
    ([5, 5], True),
    ([5, 5, 5, 20], True),
    ([5, 5, 20], False),
]

sol = Solution()
for case, exp in cases:
    assert (
        got := sol.lemonadeChange(case)
    ) == exp, f"Failed case ({case}) - expecting ({exp}), got ({got})."
