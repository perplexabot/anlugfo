package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        num int
        exp int
    }{
        {num: 11891, exp: 99009},
        {num: 90, exp: 99},
        {num: 1, exp: 9},
        {num: 99, exp: 99},
    }

    for _, testCase := range TestCases {
        got := minMaxDifference(testCase.num)
        if (got != testCase.exp) {
            t.Errorf("minMaxDifference(%d) failed - expecting (%d), got (%d)", testCase.num, testCase.exp, got)
        }
    }
}
