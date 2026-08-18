"""
Given two strings first and second, consider occurrences in some text of the form "first second
    third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".

Example 1:
    Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
    Output: ["girl","student"]

Example 2:
    Input: text = "we will we will rock you", first = "we", second = "will"
    Output: ["we","rock"]

Constraints:
    - 1 <= text.length <= 1000
    - text consists of lowercase English letters and spaces.
    - All the words in text a separated by a single space.
    - 1 <= first.length, second.length <= 10
    - first and second consist of lowercase English letters.

A:
    no occurence of first, second
        return empty
    repeating occurence,
        normal
    sentence size less than 2 words
        return empty
    first and second are the same
        so what
"""

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        curr = 0
        ret = []
        words = text.split()
        while curr < len(words):
            if words[curr] == first and curr + 2 < len(words):
                if words[curr + 1] == second:
                    ret.append(words[curr + 2])
            curr += 1
        return ret


cases = [
    ("alice is a good girl she is a good student", "a", "good", ["girl", "student"]),
    ("we will we will rock you", "we", "will", ["we", "rock"]),
    ("we we we we", "we", "we", ["we", "we"]),
    ("we we we", "we", "we", ["we"]),
    ("", "a", "b", []),
    (
        "obo jvezipre obo jnvavldde jvezipre jvezipre jnvavldde jvezipre jvezipre jvezipre y jnvavldde jnvavldde obo jnvavldde jnvavldde obo jnvavldde jnvavldde jvezipre",
        "jnvavldde",
        "y",
        [],
    ),
    (
        "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa",
        "kcyxdfnoa",
        "jkypmsxd",
        ["kcyxdfnoa", "kcyxdfnoa", "kcyxdfnoa"],
    ),
]

sol = Solution()
for text, first, second, exp in cases:
    assert (
        got := sol.findOcurrences(text, first, second)
    ) == exp, f"Failed case ({text}, {first}, {second}) - expecting ({exp}), got ({got})."
