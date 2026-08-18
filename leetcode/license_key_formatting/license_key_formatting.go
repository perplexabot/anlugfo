/*
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string
    is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which
    could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted
    between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example 1:
    Input: s = "5F3Z-2e-9-w", k = 4
    Output: "5F3Z-2E9W"
    Explanation: The string s has been split into two parts, each part has 4 characters.
    Note that the two extra dashes are not needed and can be removed.

Example 2:
    Input: s = "2-5g-3-J", k = 2
    Output: "2-5G-3J"
    Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could
        be shorter as mentioned above.

Constraints:
    - 1 <= s.length <= 105
    - s consists of English letters, digits, and dashes '-'.
    - 1 <= k <= 104

A:
    k >= len(s)
        return s with no dashes
    k == 1
        return with dashes between all
    k == 0
        return without dash
    just hyphens in s
        no possible

AA:
    leading hyphens
        possible
    useless hyphens
        possible

D:
    Input: s = "5F3Z-2e-9-w", k = 4
    0| out = [], cnt = 0
    1| out = ["w"], cnt = 1
    2| skip -
    3| out = ["w", "9"], cnt = 2
    4| out = ["w", "9", "e"], cnt = 3
    5| out = ["w", "9", "e", "2"], cnt = 4, append '-', cnt = 0
    6| out = ["w", "9", "e", "2", "-", "Z"], cnt = 1
    ...
    reverse out and join, return
*/

package main

import (
    "fmt"
    "slices"
    "unicode"
)

func licenseKeyFormatting(s string, k int) string {
    var rev []rune = []rune(s)
    slices.Reverse(rev)

    alphanumericCnt := func () int {
        cnt := 0
        for _, ch := range s {
            if unicode.IsLetter(ch) || unicode.IsNumber(ch) {
                cnt ++
            }
        }
        return cnt
    }()

    var ret []rune
    var cnt int
    var siz int
    for _, ch := range rev {
        if ch != '-' {
            ret = append(ret, unicode.ToUpper(ch))
            siz ++
            cnt ++

            if cnt == k && siz < alphanumericCnt {
                ret = append(ret, '-')
                cnt = 0
            }
        }
    }
    slices.Reverse(ret)
    return string(ret)
}

func main() {
    ans := licenseKeyFormatting("a-a-a-a-z", 2)
    fmt.Printf("%s\n", ans)
}
