"""
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a
    pointer. A character can only be typed if the pointer is pointing to that character. The pointer
    is initially pointing to the character 'a'.

Each second, you may perform one of the following operations:

    - Move the pointer one character counterclockwise or clockwise.
    - Type the character the pointer is currently on.

Given a string word, return the minimum number of seconds to type out the characters in word.

Example 1:
    Input: word = "abc"
    Output: 5
    Explanation:
    The characters are printed as follows:
    - Type the character 'a' in 1 second since the pointer is initially on 'a'.
    - Move the pointer clockwise to 'b' in 1 second.
    - Type the character 'b' in 1 second.
    - Move the pointer clockwise to 'c' in 1 second.
    - Type the character 'c' in 1 second.

Example 2:
    Input: word = "bza"
    Output: 7
    Explanation:
    The characters are printed as follows:
    - Move the pointer clockwise to 'b' in 1 second.
    - Type the character 'b' in 1 second.
    - Move the pointer counterclockwise to 'z' in 2 seconds.
    - Type the character 'z' in 1 second.
    - Move the pointer clockwise to 'a' in 1 second.
    - Type the character 'a' in 1 second.

Example 3:
    Input: word = "zjpc"
    Output: 34
    Explanation:
    The characters are printed as follows:
    - Move the pointer counterclockwise to 'z' in 1 second.
    - Type the character 'z' in 1 second.
    - Move the pointer clockwise to 'j' in 10 seconds.
    - Type the character 'j' in 1 second.
    - Move the pointer clockwise to 'p' in 6 seconds.
    - Type the character 'p' in 1 second.
    - Move the pointer counterclockwise to 'c' in 13 seconds.
    - Type the character 'c' in 1 second.

Constraints:
    1 <= word.length <= 100
    word consists of lowercase English letters.

A:
    empty word:
        return 0
    word with one letter:
        solve and return
    word only has lower case letters?
        yes

D:
    Input: word = "zjpc"
    pointer at a
        z:
            z -
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        from string import ascii_lowercase

        n = len(ascii_lowercase)
        weights = {x: i + 1 for i, x in enumerate(ascii_lowercase)}
        pointer = 'a'
        seconds = 0

        for letter in word:
            seconds += (
                min(
                    abs(weights[letter] - weights[pointer]),
                    n - abs(weights[letter] - weights[pointer]),
                )
                + 1
            )
            pointer = letter
        return seconds


sol = Solution()

cases = [("abc", 5), ("bza", 7), ("zjpc", 34), ("a", 1), ("z", 2), ("b", 2)]
for word, exp in cases:
    assert (
        got := sol.minTimeToType(word)
    ) == exp, f"Failed case ({word}) - expecting ({exp}), got ({got})."
