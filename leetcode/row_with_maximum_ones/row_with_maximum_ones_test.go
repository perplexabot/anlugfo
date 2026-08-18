package main

import (
    "testing"
    "reflect"
)

func TestFunc(t *testing.T) {
    var TestCases = []struct {
        mat [][]int
        exp []int
    }{
        {mat: [][]int{{0,1},{1,0}}, exp: []int{0,1}},
        {mat: [][]int{{0,0,0},{0,1,1}}, exp: []int{1,2}},
        {mat: [][]int{{0,0},{1,1},{0,0}}, exp: []int{1,2}},
        {mat: [][]int{{1,2},{1,1}}, exp: []int{1,2}},
        {mat: [][]int{{1},{1},{1}}, exp: []int{0,1}},
        {mat: [][]int{{0},{1},{2}}, exp: []int{1,1}},
        {mat: [][]int{{1},{1,1,1},{1}}, exp: []int{1,3}},
        {mat: [][]int{{1},{1,1,1},{1,1,1,1,1}}, exp: []int{2,5}},
    }

    for _, testCase := range TestCases {
        got := rowAndMaximumOnes(testCase.mat)
        if (!reflect.DeepEqual(got, testCase.exp)) {
            t.Errorf("rowAndMaximumOnes(%v) failed - expecting (%v), got (%v)", testCase.mat, testCase.exp, got)
        }
    }
}
