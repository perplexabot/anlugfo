package main

import (
    "testing"
)

func TestFunc(t *testing.T) {
    var cases = []struct {
        amount int
        exp int
    }{
        {amount: 9, exp: 90},
        {amount: 10, exp: 90},
        {amount: 0, exp: 100},
        {amount: 20, exp: 80},
        {amount: 1, exp: 100},
        {amount: 6, exp: 90},
        {amount: 5, exp: 90},
        {amount: 15, exp: 80},
        {amount: 16, exp: 80},
        {amount: 14, exp: 90},
        {amount: 100, exp: 0},
    }

    for _, testCase := range cases {
        got := accountBalanceAfterPurchase(testCase.amount)
        if got != testCase.exp {
            t.Errorf("accountBalanceAfterPurchase(%d) failed - got (%d), expecting (%d)", testCase.amount, got, testCase.exp)
        }
    }
}
