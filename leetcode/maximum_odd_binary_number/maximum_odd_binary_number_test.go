package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct {
        s string
        exp string
    }{
        {s: "010", exp: "001"},
        {s: "0101", exp: "1001"},
        {s: "1", exp: "1"},
        {s: "0", exp: "0"},
        {s: "000", exp: "000"},
        {s: "100", exp: "001"},
        {s: "010", exp: "001"},
        {s: "001", exp: "001"},
        {s: "11", exp: "11"},
        {s: "10", exp: "01"},
        {s: "01", exp: "01"},
    }

    for _, testCase := range TestCases {
        got := maximumOddBinaryNumber(testCase.s)
        if (got != testCase.exp) {
            t.Errorf("maximumOddBinaryNumber(%s) failed - got (%s), expecting (%s)", testCase.s, got, testCase.exp)
        }
    }
}
