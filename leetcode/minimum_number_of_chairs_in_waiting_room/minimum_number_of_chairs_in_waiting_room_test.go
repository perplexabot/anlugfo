package main 

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        s string
        exp int
    }{
        {s: "EEEEEEE", exp: 7},
        {s: "ELELEEL", exp: 2},
        {s: "ELEELEELLL", exp: 3},
    }

    for _, testCase := range TestCases {
        got := minimumChairs(testCase.s)
        if (got != testCase.exp) {
            t.Errorf("minimumChairs(%s) failed - expecting (%d), got (%d)", testCase.s, testCase.exp, got)
        }
    }
}
