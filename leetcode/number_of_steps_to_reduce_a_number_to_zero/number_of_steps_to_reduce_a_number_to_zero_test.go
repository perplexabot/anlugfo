package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        num int
        exp int
    }{
        {num: 14, exp: 6},
        {num: 8, exp: 4},
        {num: 123, exp: 12},
        {num: 1, exp: 1},
        {num: 0, exp: 0},
        {num: 2, exp: 2},
    }

    for _, testCase := range TestCases {
        got := numberOfSteps(testCase.num)
        if got != testCase.exp {
            t.Errorf("numberOfSteps(%d) failed - expecting (%d), got (%d)", testCase.num, testCase.exp, got)
        }
    }
}
