/*
You are given a 0-indexed array of string words and two integers left and right.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character
    where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

Example 1:
    Input: words = ["are","amy","u"], left = 0, right = 2
    Output: 2
    Explanation:
    - "are" is a vowel string because it starts with 'a' and ends with 'e'.
    - "amy" is not a vowel string because it does not end with a vowel.
    - "u" is a vowel string because it starts with 'u' and ends with 'u'.
    The number of vowel strings in the mentioned range is 2.

Example 2:
    Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
    Output: 3
    Explanation:
    - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
    - "mu" is not a vowel string because it does not start with a vowel.
    - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
    - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
    The number of vowel strings in the mentioned range is 3.

Constraints:
    - 1 <= words.length <= 1000
    - 1 <= words[i].length <= 10
    - words[i] consists of only lowercase English letters.
    - 0 <= left <= right < words.length

A:
    left or right out of range:
        not possible
    left == right
        one word to check
    words.length > 0
        always
*/

package main

import (
    "fmt"
)

func vowelStrings(words []string, left int, right int) int {
    var count int
    var m map[rune]rune = map[rune]rune{
        'a':'a',
        'e':'e',
        'i':'i',
        'o':'o',
        'u':'u',
        'A':'A',
        'E':'E',
        'I':'I',
        'O':'O',
        'U':'U',
    }

    for i := left; i <= right; i++ {
        r := []rune(words[i])
        if _, startOk := m[r[0]] ; startOk {
            if _, endOk := m[r[len(r)-1]] ; endOk {
                count++
            }

        }
    }

    return count
}

func main() {
    var thing []string = []string{"hello", "bye", "obo"}
    ans := vowelStrings(thing,0,2)
    fmt.Printf("%d\n", ans)
}
