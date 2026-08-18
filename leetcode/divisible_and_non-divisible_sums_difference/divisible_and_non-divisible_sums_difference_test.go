package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        n int
        m int
        exp int
    }{
        {n: 5, m: 6, exp: 15},
        {n: 10, m: 3, exp: 19},
        {n: 1, m: 1, exp: -1},
    }

    for _, testCase := range TestCases {
        got := differenceOfSums(testCase.n, testCase.m)
        if (got != testCase.exp) {
            t.Errorf("differenceOfSums(%d, %d) failed - expecting (%d), got (%d).", testCase.n, testCase.m, testCase.exp, got)
        }
    }
}
