"""
You are given a string sentence that consist of words separated by spaces. Each word consists of
    lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
    The rules of Goat Latin are as follows:

        - If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of
            the word.
            For example, the word "apple" becomes "applema".
        - If a word begins with a consonant (i.e., not a vowel), remove the first letter and append
            it to the end, then add "ma".
            For example, the word "goat" becomes "oatgma".
        - Add one letter 'a' to the end of each word per its word index in the sentence, starting
            with 1.
            For example, the first word gets "a" added to the end, the second word gets "aa" added
                to the end, and so on.

Return the final sentence representing the conversion from sentence to Goat Latin.

Example 1:
    Input: sentence = "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:
    Input: sentence = "The quick brown fox jumped over the lazy dog"
    Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa
        azylmaaaaaaaaa ogdmaaaaaaaaaa"

Constraints:
    1 <= sentence.length <= 150
    sentence consists of English letters and spaces.
    sentence has no leading or trailing spaces.
    All the words in sentence are separated by a single space.

A:
    empty sentense: return ""
    sentence with a single letter: no issue
    sentence with a lot of white space between words: no issue

D:
    gl = []
    for ind, word in words:
        if word[0] in vowel:
            w = word[0] + "ma"
        else:
            w = word[1:] + word[0] + "ma"
        gl.append(w + "a" * ind)
    return ' '.join(gl)

"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        gl = []
        for (ind, word) in enumerate(sentence.split()):
            w = (
                word + "ma"
                if word[0].lower() in {"a", "e", "i", "o", "u"}
                else word[1:] + word[0] + "ma"
            )
            gl.append(w + "a" * (ind + 1))

        return ' '.join(gl)


cases = [
    ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
    (
        "The quick brown fox jumped over the lazy dog",
        "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
    ),
    ("I", "Imaa"),
    ("B", "Bmaa"),
]

sol = Solution()
for (sentence, exp) in cases:
    assert (
        got := sol.toGoatLatin(sentence)
    ) == exp, f"Failed case ({sentence}) - \nexpecting ({exp})\ngot       ({got})."
