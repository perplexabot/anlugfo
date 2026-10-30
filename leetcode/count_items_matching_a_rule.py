"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type,
    color, and name of the ith item. You are also given a rule represented by two strings,
    ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:
    - ruleKey == "type" and ruleValue == typei.
    - ruleKey == "color" and ruleValue == colori.
    - ruleKey == "name" and ruleValue == namei.

Return the number of items that match the given rule.

Example 1:
    Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],
        ["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
    Output: 1
    Explanation: There is only one item matching the given rule, which is
        ["computer","silver","lenovo"].

Example 2:
    Input: items = [["phone","blue","pixel"],["computer","silver","phone"],
        ["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
    Output: 2
    Explanation: There are only two items matching the given rule, which are
        ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the
        item ["computer","silver","phone"] does not match.

Constraints:
    - 1 <= items.length <= 104
    - 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
    - ruleKey is equal to either "type", "color", or "name".
    - All strings consist only of lowercase letters.

A:
    empty items
        return 0
    items but no rule
        return size of items?
        likely always rule
    no items no rules
        return 0
    more than one rule?
        no, always 1

D:
    Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],
        ["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"

        ruleKey = color which means index == 1
        item[0][1] == silver?, no
        item[1][1] == silver?, yes, cnt ++
        item[2][1] == silver?, no
        return cnt

P:
    cnt = 0
    typeToIndex = {"type": 0, "color": 1, "name": 2}
    for item in items:
        if item[typeToIndex[ruleKey]] == ruleValue:
            cnt ++
    return cnt

"""


class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        typeToIndex = {"type": 0, "color": 1, "name": 2}
        for item in items:
            if item[typeToIndex[ruleKey]] == ruleValue:
                cnt += 1
        return cnt


cases = [
    (
        (
            [
                ["phone", "blue", "pixel"],
                ["computer", "silver", "lenovo"],
                ["phone", "gold", "iphone"],
            ],
            "color",
            "silver",
        ),
        1,
    ),
    (
        (
            [
                ["phone", "blue", "pixel"],
                ["computer", "silver", "phone"],
                ["phone", "gold", "iphone"],
            ],
            "type",
            "phone",
        ),
        2,
    ),
    (([["thing", "opaque", "thingy"], ["another", "blue", "thingamabob"]], "type", "thing"), 1),
    (([["thing", "opaque", "thingy"], ["another", "blue", "thingamabob"]], "type", "thingy"), 0),
    (([["thing", "opaque", "thingy"], ["another", "blue", "thingamabob"]], "color", "wow"), 0),
]

sol = Solution()
for case, expected in cases:
    assert (
        got := sol.countMatches(*case)
    ) == expected, f"Failed case ({case})! - expecting ({expected}), got ({got})."
