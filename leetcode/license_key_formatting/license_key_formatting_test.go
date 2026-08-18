package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        s string
        k int
        exp string
    }{
        {s: "2-5g-3-J", k: 2, exp: "2-5G-3J"},
        {s: "5F3Z-2e-9-w", k: 4, exp: "5F3Z-2E9W"},
        {s: "a-a-a-a-z", k: 2, exp: "A-AA-AZ"},
        {s: "a", k: 3, exp: "A"},
        {s: "aaaaaaaa", k: 1, exp: "A-A-A-A-A-A-A-A"},
        {s: "--a-a-a-a--", k:2, exp: "AA-AA"},
    }

    for _, testCase := range TestCases {
        got := licenseKeyFormatting(testCase.s, testCase.k)
        if (got != testCase.exp) {
            t.Errorf("licenseKeyFormatting(%v, %d) failed - expecting (%s), got (%s)", testCase.s, testCase.k, testCase.exp, got)
        }
    }
}
