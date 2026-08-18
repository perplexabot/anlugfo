package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        arr []int
        exp bool
    }{
        {arr: []int{2,6,4,1}, exp: false},
        {arr: []int{1,2,34,3,4,5,7,23,12}, exp: true},
        {arr: []int{1}, exp: false},
        {arr: []int{1,2}, exp: false},
        {arr: []int{1,1}, exp: false},
        {arr: []int{1,2,1}, exp: false},
        {arr: []int{1,1,1}, exp: true},
        {arr: []int{1,3,9}, exp: true},
        {arr: []int{1,32,9}, exp: false},
    }

    for _, testCase := range TestCases {
        got := threeConsecutiveOdds(testCase.arr)
        if (got != testCase.exp) {
            t.Errorf("threeConsecutiveOdds(%v) failed - expecting (%t), got (%t).", testCase.arr, testCase.exp, got)
        }
    }
}
