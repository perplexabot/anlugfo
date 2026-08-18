/*
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

    Each substring is balanced.

Return the maximum number of balanced strings you can obtain.

Example 1:
    Input: s = "RLRRLLRLRL"
    Output: 4
    Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
    Input: s = "RLRRRLLRLL"
    Output: 2
    Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
    Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

Example 3:
    Input: s = "LLLLRRRR"
    Output: 1
    Explanation: s can be split into "LLLLRRRR".

Constraints:
    - 2 <= s.length <= 1000
    - s[i] is either 'L' or 'R'.
    - s is a balanced string.

A:
    can s be not balanced?
        no
    can s be empty?
        yes, just return empty
    anything other than LR?
        no

A:
    can we be greedy?
        yes because of the properties of a balanced string - if we remove a pair, s is still balanced

D:
    lcnt = 0
    rcnt = 0
    ans = 0
    for char in s:
        if char == L:
            lcnt ++
        else
            rcnt ++

        if lcnt == rcnt:
            ans ++
            lcnt = 0
            rcnt = 0

*/

package main

import (
    "fmt"
)

func balancedStringSplit(s string) int {
    var ans int
    var lcnt int
    var rcnt int

    for _, char := range s {
        if string(char) == "L" {
            lcnt ++
        } else {
            rcnt ++
        }

        if lcnt == rcnt {
            ans ++
            lcnt = 0
            rcnt = 0
        }
    }

    return ans
}

func main() {
    fmt.Println(balancedStringSplit("LRLLRR"))
}
