package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct{
        nums []int
        exp int
    }{
        {nums: []int{3,2,1,4,5}, exp: 2},
        {nums: []int{3,2,6,1,4}, exp: 1},
        {nums: []int{1,2,1,2}, exp: 2},
        {nums: []int{1,2,1,2,2,1}, exp: 3},
        {nums: []int{1,1,1,1,1,1,1}, exp: 3},
    }

    for _, testCase := range TestCases {
        got := maxOperations(testCase.nums)
        if (got != testCase.exp) {
            t.Errorf("maxOperations(%v) failed - expecting (%d), got (%d)", testCase.nums, testCase.exp, got)
        }
    }
}
