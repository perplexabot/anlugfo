package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct {
        nums1 []int
        nums2 []int
        k int
        exp int
    }{
        {nums1: []int{1,3,4}, nums2: []int{1,3,4}, k: 1, exp: 5},
        {nums1: []int{1,2,4,12}, nums2: []int{2,4}, k: 3, exp: 2},
        {nums1: []int{1}, nums2: []int{1}, k: 3, exp: 0},
        {nums1: []int{1}, nums2: []int{1}, k: 1, exp: 1},
        {nums1: []int{3}, nums2: []int{1}, k: 1, exp: 1},
        {nums1: []int{3}, nums2: []int{1}, k: 3, exp: 1},
        {nums1: []int{1}, nums2: []int{3}, k: 1, exp: 0},
    }

    for _, testCase := range TestCases {
        got := numberOfPairs(testCase.nums1, testCase.nums2, testCase.k)
        if got != testCase.exp {
            t.Errorf("numberOfPairs(%v, %v, %d) failed - expecting (%d), got (%d)", testCase.nums1, testCase.nums2, testCase.k, testCase.exp, got)
        }
    }
}
