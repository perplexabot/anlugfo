"""
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is
    equal to the number of ones inside the substring. Notice that the empty substring is
    considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "01000111"
    Output: 6
    Explanation: The longest balanced substring is "000111", which has length 6.

Example 2:
    Input: s = "00111"
    Output: 4
    Explanation: The longest balanced substring is "0011", which has length 4.

Example 3:
    Input: s = "111"
    Output: 0
    Explanation: There is no balanced substring except the empty substring, so the answer is 0.

Constraints:
    1 <= s.length <= 50
    '0' <= s[i] <= '1'

A:
    len(s) < 2:
        return 0
    s has things other than 0 or 1

D:
    find interfaces, for each:
        count left and right until out of bounds or change
        new_max = max(curr, new_count)
"""


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        def get_indices(s):
            if not s:
                return []

            start = 0
            indices = []
            while start < len(s):
                ans = s.find('01', start, len(s))
                if ans != -1:
                    indices.append(ans)
                    start = ans + 1
                else:
                    return indices

        curr_max = 0
        for interface in get_indices(s):
            cnt = 2
            left = interface - 1
            right = interface + 2

            while left > -1 and right < len(s):
                if s[left] != "0" or s[right] != "1":
                    break
                cnt += 2
                left -= 1
                right += 1
            curr_max = max(curr_max, cnt)
        return curr_max


cases = [
    ("01000111", 6),
    ("00111", 4),
    ("111", 0),
    ("01", 2),
    ("10", 0),
    ("0", 0),
    ("1", 0),
    ("0101000111", 6),
    ("000101000", 2),
]

sol = Solution()
for s, exp in cases:
    assert (
        got := sol.findTheLongestBalancedSubstring(s)
    ) == exp, f"Failed case ({s}) - expecting ({exp}), got ({got})."
