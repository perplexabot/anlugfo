package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct {
        s string
        exp int
    }{
        {s: "RLRRLLRLRL", exp: 4},
        {s: "RLRRRLLRLL", exp: 2},
        {s: "LLLLRRRR", exp: 1},
        {s: "LR", exp: 1},
        {s: "LRLR", exp: 2},
        {s: "", exp: 0},
        {s: "LRLLRR", exp: 2},
    }

    for _, testCase := range TestCases {
        got := balancedStringSplit(testCase.s)
        if (got != testCase.exp) {
            t.Errorf("balancedStringSplit(%s) failed - expecting (%d), got (%d)", testCase.s, testCase.exp, got)
        }
    }
}
