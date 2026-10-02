"""
A password is said to be strong if it satisfies all the following criteria:

    - It has at least 8 characters.
    - It contains at least one lowercase letter.
    - It contains at least one uppercase letter.
    - It contains at least one digit.
    - It contains at least one special character. The special characters are the characters in the
        following string: "!@#$%^&*()-+".
    - It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this
        condition, but "aba" does not).

Given a string password, return true if it is a strong password. Otherwise, return False.

Example 1:
    Input: password = "IloveLe3tcode!"
    Output: true
    Explanation: The password meets all the requirements. Therefore, we return true.

Example 2:
    Input: password = "Me+You--IsMyDream"
    Output: False
    Explanation: The password does not contain a digit and also contains 2 of the same character in
        adjacent positions. Therefore, we return False.

Example 3:
    Input: password = "1aB!"
    Output: False
    Explanation: The password does not meet the length requirement. Therefore, we return False.

Constraints:
    - 1 <= password.length <= 100
    - password consists of letters, digits, and special characters: "!@#$%^&*()-+".

A:
    all chars in a string are defined as characters?
        yes

D:
    Input: password = "IloveLe3tcode!"
        length ok
        lower case exists
        upper case exists
        digit exists
        special char peresent
        no adjacent rule break
        return true

P:

    charCnt = 0
    lower = False
    upper = False
    digit = False
    special = False
    prev = None
    for char in password:
        charCnt += 1

        if char == prev:
            return False
        prev = char

        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True
        elif char.isspecial():
            special = True
    return charCnt > 8 and lower and upper and digit and special


O:
    one pass, no extra ds (time and space of O(n) and O(1) respectively)

T:
    ("IloveLe3tcode!", true),
    ("Me+You--IsMyDream", False),
    ("1aB!", False),
    ("", False),
    ("A", False),
    ("Ab", False),
    ("Ab!", False),
    ("Ab!1", False),
    ("IloveLle3tcode!", true),
    ("IloveLLe3tcode!", False),
    ("aBc123!", False),
    ("aBc123!a", true),
    ("aBc123!aa", False),
    ("aBc123!aa", False),
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        charCnt = 0
        lower = False
        upper = False
        digit = False
        special = False
        prev = None
        specials = "!@#$%^&*()-+"
        for char in password:
            charCnt += 1

            if char == prev:
                return False
            prev = char

            if char.islower():
                lower = True
            elif char.isupper():
                upper = True
            elif char.isdigit():
                digit = True
            elif char in specials:
                special = True

        return lower and upper and digit and special and charCnt >= 8


cases = [
    ("IloveLe3tcode!", True),
    ("Me+You--IsMyDream", False),
    ("1aB!", False),
    ("", False),
    ("A", False),
    ("Ab", False),
    ("Ab!", False),
    ("Ab!1", False),
    ("IloveLle3tcode!", True),
    ("IloveLLe3tcode!", False),
    ("aBc123!", False),
    ("aBc123!a", True),
    ("aBc123!aa", False),
    ("aBc123!aa", False),
]

sol = Solution()
for password, expected in cases:
    assert (
        got := sol.strongPasswordCheckerII(password)
    ) == expected, f"Woops, failed case ({password}) - expecting ({expected}), got ({got})."
