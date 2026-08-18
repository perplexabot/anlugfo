/*
Given a positive integer num represented as a string, return the integer num without
    trailing zeros as a string.

Example 1:
    Input: num = "51230100"
    Output: "512301"
    Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return
        integer "512301".

Example 2:
    Input: num = "123"
    Output: "123"
    Explanation: Integer "123" has no trailing zeros, we return integer "123".

Constraints:
    - 1 <= num.length <= 1000
    - num consists of only digits.
    - num doesn't have any leading zeros.

A:
    anything other than digits?
        no
    can num be 0?
        ?
*/

package main

import (
    "fmt"
)

func removeTrailingZeros(num string) string {
    if num == "" {
        return num
    }

    var r []rune = []rune(num)

    if string(r[0]) == "0" {
        return "0"
    }

    var last int 
    for i:= len(r) - 1; i >= 0; i-- {
        if string(r[i]) != "0" {
            last = i
            break
        }
    }
    return string(r[:last+1])
}

func main() {
    ans:=removeTrailingZeros("2340")
    fmt.Printf("|%s|\n",ans)
}
