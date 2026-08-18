package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        words []string
        left int
        right int
        exp int
    }{
        {words: []string{"are","amy","u"}, left: 0, right: 2, exp: 2},
        {words: []string{"hey","aeo","mu","ooo","artro"}, left: 1, right: 4, exp: 3},
        {words: []string{"a","e","i"}, left: 0, right: 0, exp: 1},
        {words: []string{"a","e","i"}, left: 0, right: 1, exp: 2},
        {words: []string{"a","e","i"}, left: 0, right: 2, exp: 3},
        {words: []string{"a","e","i"}, left: 1, right: 2, exp: 2},
        {words: []string{"a","e","i"}, left: 2, right: 2, exp: 1},
        {words: []string{"t","e","i"}, left: 0, right: 2, exp: 2},
        {words: []string{"a"}, left: 0, right: 0, exp: 1},
    }

    for _, testCase := range TestCases {
        got := vowelStrings(testCase.words, testCase.left, testCase.right)
        if (got != testCase.exp) {
            t.Errorf("vowelStrings(%v, %d, %d) failed - expecting (%d), got (%d)",
                testCase.words,
                testCase.left,
                testCase.right,
                testCase.exp,
                got,
            )
        }
    }
}
