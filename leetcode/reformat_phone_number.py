"""
You are given a phone number as a string number. number consists of digits, spaces ' ', and/or
    dashes '-'.

You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and
    dashes. Then, group the digits from left to right into blocks of length 3 until there are 4
    or fewer digits. The final digits are then grouped as follows:
    - 2 digits: A single block of length 2.
    - 3 digits: A single block of length 3.
    - 4 digits: Two blocks of length 2 each.

The blocks are then joined by dashes. Notice that the reformatting process should never produce
    any blocks of length 1 and produce at most two blocks of length 2.

Return the phone number after formatting.

Example 1:
    Input: number = "1-23-45 6"
    Output: "123-456"
    Explanation: The digits are "123456".
    Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
    Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd
        block is "456".
    Joining the blocks gives "123-456".

Example 2:
    Input: number = "123 4-567"
    Output: "123-45-67"
    Explanation: The digits are "1234567".
    Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
    Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks
        are "45" and "67".
    Joining the blocks gives "123-45-67".

Example 3:
    Input: number = "123 4-5678"
    Output: "123-456-78"
    Explanation: The digits are "12345678".
    Step 1: The 1st block is "123".
    Step 2: The 2nd block is "456".
    Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block
        is "78".
    Joining the blocks gives "123-456-78".

A:
    size of string without space and dash is less or = 6?
       just group in blocks of three 
    size of string without space and dash is less than 3?
       size 2 then return block of 2
    less than 3?
        not possible
    longer than 7?
        oh ya up to 100

D:
    12
        12
    123
        123
    1234
        12 34
    12345
        123 12
    123456
        123 456
    1234567
        123 45 67
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        n = number.replace('-', '').replace(' ', '')
        left = len(n)
        i = 0
        chunks = []
        while left > 4:
            chunks.append(n[i : i + 3])
            i += 3
            left -= 3

        if left == 2:
            end = [n[-2:]]
        elif left == 3:
            end = [n[-3:]]
        else:
            end = [n[-4:-2], n[-2:]]

        return '-'.join(chunks + end)


sol = Solution()

cases = [
    ("1-23-45 6", "123-456"),
    ("123 4-567", "123-45-67"),
    ("123 4-5678", "123-456-78"),
    ("12", "12"),
    ("123", "123"),
    ("1234", "12-34"),
    ("12345", "123-45"),
    ("123456", "123-456"),
    ("1234567", "123-45-67"),
]

for number, exp in cases:
    assert (
        got := sol.reformatNumber(number)
    ) == exp, f"Failed case ({number}) - expecting ({exp}), got ({got})."
