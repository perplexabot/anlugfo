package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        n int
        exp bool
    }{
        {n: 6, exp: true},
        {n: 1, exp: true},
        {n: 14, exp: false},
        {n: -1, exp: false},
        {n: 100, exp: true},
        {n: 0, exp: false},
    }

    for _, testCase := range TestCases {
        got := isUgly(testCase.n)
        if got != testCase.exp {
            t.Errorf("isUgly(%d) failed - expecting (%t) got (%t).", testCase.n, testCase.exp, got)
        }
    }
}
