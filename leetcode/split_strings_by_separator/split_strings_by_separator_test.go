package main

import (
    "testing"
    "reflect"
)

func TestFunc(t *testing.T) {
    var cases = []struct{
        words []string
        seper byte
        exp []string
    }{
        {words: []string{"one.two.three","four.five","six"}, seper: '.', exp: []string{"one","two","three","four","five","six"}},
        {words: []string{"1,2"}, seper: ',', exp: []string{"1", "2"}},
        {words: []string{"1,2"}, seper: '.', exp: []string{"1,2"}},
        {words: []string{"$easy$","$problem$"}, seper: '$', exp: []string{"easy","problem"}},
        {words: []string{"|||"}, seper: '|', exp: nil},
    }

    for _, testCase := range cases {
        got := splitWordsBySeparator(testCase.words, testCase.seper)
        if !reflect.DeepEqual(testCase.exp, got) {
            t.Errorf("splitWordsBySeparator(%v, %b) failed - expecting (%v), got (%v)", testCase.words, testCase.seper, testCase.exp, got)
        }
    }
}
