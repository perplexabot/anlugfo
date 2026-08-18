"""
A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.

You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in the
    testing sequence, and a sorted list releaseTimes, where releaseTimes[i] was the time the
    ith key was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, and
    every subsequent key was pressed at the exact time the previous key was released.

The tester wants to know the key of the keypress that had the longest duration. The ith keypress
    had a duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of
    releaseTimes[0].

Note that the same key could have been pressed multiple times during the test, and these multiple
    presses of the same key may not have had the same duration.

Return the key of the keypress that had the longest duration. If there are multiple such
    keypresses, return the lexicographically largest key of the keypresses.



Example 1:
    Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
    Output: "c"
    Explanation: The keypresses were as follows:
    Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
    Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and released at time 29).
    Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character and released at time 49).
    Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and released at time 50).
    The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
    'c' is lexicographically larger than 'b', so the answer is 'c'.

Example 2:
    Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
    Output: "a"
    Explanation: The keypresses were as follows:
    Keypress for 's' had a duration of 12.
    Keypress for 'p' had a duration of 23 - 12 = 11.
    Keypress for 'u' had a duration of 36 - 23 = 13.
    Keypress for 'd' had a duration of 46 - 36 = 10.
    Keypress for 'a' had a duration of 62 - 46 = 16.
    The longest of these was the keypress for 'a' with duration 16.

Constraints:
    releaseTimes.length == n
    keysPressed.length == n
    2 <= n <= 1000
    1 <= releaseTimes[i] <= 10**9
    releaseTimes[i] < releaseTimes[i+1]
    keysPressed contains only lowercase English letters.

A:
    releaseTimes empty -> return None
    keysPressed empty -> return None
    len(releaseTimes) = 1 -> return keysPressed[0]
    possible for releaseTimes[i] < releaseTimes[i-1] ?

D:
                    0  1  2  3  4
    releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
    ind = 0
        time = 12, max = 12, pots = {s}
    ind = 1
        time = 23-12 = 11, max = 12, pots = {s}
    ind = 2
        time = 36-23 = 13, max = 13, pots = {u}
    ind = 3
        time = 46-36 = 10, max = 13, pots = {u}
    ind = 4
        time = 62-46 = 16, max = 16, pots = {a}
    return a
"""

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        if len(releaseTimes) == 1:
            return keysPressed[0]

        max_hold = releaseTimes[0]
        pot_keys = set([keysPressed[0]])

        index = 1
        while index < len(releaseTimes):
            hold_time = releaseTimes[index] - releaseTimes[index - 1]
            if hold_time > max_hold:
                max_hold = hold_time
                pot_keys = set([keysPressed[index]])
            elif hold_time == max_hold:
                pot_keys.add(keysPressed[index])
            index += 1
        return max(pot_keys)


cases = [
    ([9, 29, 49, 50], "cbcd", "c"),
    ([12, 23, 36, 46, 62], "spuda", "a"),
    ([9, 29, 49, 50], "cbcd", "c"),
]

sol = Solution()
for (releaseTimes, keys, exp) in cases:
    assert (
        got := sol.slowestKey(releaseTimes, keys)
    ) == exp, f"Failed case ({releaseTimes}, {keys}) - expecting ({exp}), got ({got})."
