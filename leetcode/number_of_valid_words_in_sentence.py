"""
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'),
    punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken
        down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:
    - It only contains lowercase letters, hyphens, and/or punctuation (no digits).
    - There is at most one hyphen '-'. If present, it must be surrounded by lowercase
        characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
    - There is at most one punctuation mark. If present, it must be at the end of the
        token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).

Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
Given a string sentence, return the number of valid words in sentence.

Example 1:
    Input: sentence = "cat and  dog"
    Output: 3
    Explanation: The valid words in the sentence are "cat", "and", and "dog".

Example 2:
    Input: sentence = "!this  1-s b8d!"
    Output: 0
    Explanation: There are no valid words in the sentence.
    "!this" is invalid because it starts with a punctuation mark.
    "1-s" and "b8d" are invalid because they contain digits.

Example 3:
    Input: sentence = "alice and  bob are playing stone-game10"
    Output: 5
    Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
    "stone-game10" is invalid because it contains digits.

Constraints:
    1 <= sentence.length <= 1000
    sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
    There will be at least 1 token.

A:
    sentence only has white space -> return 0
    token is just a punctuation -> return 0

D:
    valids = 0
    for word in sentence:
        if only lower case letters in word:
            if hyphens have letters on both sides:
                if punctuation at end:
                    valids += 1
    return valids
"""


class Solution:
    def countValidWords(self, sentence: str) -> int:
        from string import ascii_uppercase, ascii_lowercase, digits

        puncs = set(["!", ",", "."])
        valids = 0
        for word in sentence.split():

            if word.count('-') > 1:
                continue

            if set(word).intersection(digits):
                continue

            if word.count('!') + word.count(',') + word.count('.') > 1:
                continue

            if "!" in word or "." in word or "," in word:
                if word[-1] not in puncs:
                    continue

            good = True
            for ind, e in enumerate(word):
                if e in ascii_uppercase:
                    good = False
                    break

                if e == "-":
                    if ind == 0 or ind == len(word) - 1:
                        good = False
                        break
                    if word[ind - 1] not in ascii_lowercase or word[ind + 1] not in ascii_lowercase:
                        good = False
                        break

            if not good:
                continue

            valids += 1
        return valids


cases = [
    ("cat and  dog", 3),
    ("!this  1-s b8d!", 0),
    ("alice and  bob are playing stone-game10", 5),
    ("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.", 6),
    ("a-b-c", 0),
    (". ! 7hk  al6 l! aon49esj35la k3 7u2tkh  7i9y5  !jyylhppd et v- h!ogsouv 5", 4),
]

sol = Solution()
for sentence, exp in cases:
    assert (
        got := sol.countValidWords(sentence)
    ) == exp, f"Failed case ({sentence}) - expecting ({exp}), got ({got})."
