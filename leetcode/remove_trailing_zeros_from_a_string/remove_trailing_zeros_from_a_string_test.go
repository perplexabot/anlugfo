package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var testCases = []struct{
        num string
        exp string
    }{
        {num: "51230100", exp: "512301"},
        {num: "123", exp: "123"},
        {num: "000", exp: "0"},
    }

    for _, testCase := range testCases {
        got := removeTrailingZeros(testCase.num)
        if got != testCase.exp {
            t.Errorf("removeTrailingZeros(%s) failed - got (%s), expecting (%s)", testCase.num, got, testCase.exp)
        }
    }

}
