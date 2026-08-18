package main
import (
    "testing"
    "reflect"
)

func TestShuffle(t *testing.T) {
    var cases = []struct {
        nums []int
        n int
        expected []int
    }{
        {nums: []int{2,5,1,3,4,7}, n: 3, expected: []int{2,3,5,4,1,7}},
        {nums: []int{1,2,3,4,4,3,2,1}, n: 4, expected: []int{1,4,2,3,3,2,4,1}},
        {nums: []int{1,1,2,2}, n: 2, expected: []int{1,2,1,2}},
    }

    for _, testCase := range cases {
        got := shuffle(testCase.nums,testCase.n)
        if !reflect.DeepEqual(got, testCase.expected) {
            t.Errorf("shuffle(%v, %d) failed - expecting (%v), got (%v)", testCase.nums, testCase.n, testCase.expected, got)
        }
    }
}
