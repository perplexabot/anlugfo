/*
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that
    can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

Example 1:
    Input: s = "010"
    Output: "001"
    Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

Example 2:
    Input: s = "0101"
    Output: "1001"
    Explanation: One of the '1's must be in the last position. The maximum number that can be made with
        the remaining digits is "100". So the answer is "1001".

Constraints:
    - 1 <= s.length <= 100
    - s consists only of '0' and '1'.
    - s contains at least one '1'.

A:
    empty string
        not possible
    string len == 1
        return 1
    string len != 1
        if more than one 1, one at the end and one at the beginning, else return 1
    string has a lot of ones
        all ones at the beginning except the remaining one, that goes at the end

D:
    Input: s = "0101"
    total size: 4
    total ones: 2
        keep appending ones, until one left
        append zeros until size equal less than one from og
        append remaining one
        return
*/

package main

import (
    "strings"
    "fmt"
)

func maximumOddBinaryNumber(s string) string {
    var total int = len(s)
    var ones int = strings.Count(s, "1")
    var zeros int = strings.Count(s, "0")

    var fin []rune
    if ones == total || zeros == total || total == 1 {
        return s
    } else if ones == 1 {
        var news strings.Builder
        w := strings.Repeat("0", zeros)
        news.WriteString(w)
        news.WriteString("1")
        return news.String()
    } else {
        // add sig bit ones
        for range ones - 1 {
            fin = append(fin, '1')
        }

        // add zeros
        for range zeros {
            fin = append(fin, '0')
        }

        // add odd 1
        fin = append(fin, '1')

    }

    return string(fin)
}

func main() {
    fmt.Println(maximumOddBinaryNumber("0110"))
}
