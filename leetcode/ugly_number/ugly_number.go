/*
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:
    Input: n = 6
    Output: true
    Explanation: 6 = 2 × 3

Example 2:
    Input: n = 1
    Output: true
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
    Input: n = 14
    Output: false
    Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:
    - -231 <= n <= 231 - 1
*/

package main

import (
    "math"
)


func getPrimes(n int) []int{
    primes:= make([]bool, n+1)
    for i:= range primes {
        primes[i] = true
    }
    primes[0] = false
    primes[1] = false

    for i:= 2; float64(i) <= math.Sqrt(float64(n)); i++ {
        if primes[i] {
            for j:=math.Pow(float64(i),2); j <= float64(n);j = j + float64(i) {
                primes[int(j)] = false
            }
        }
    }

    var final []int
    for num, isPrime:= range primes {
        if isPrime {
            final = append(final, num)
        }
    }
    return final
}

func isUgly(n int) bool {
    if n <= 0 {
        return false
    } else {
        primes := getPrimes(n)
        for _, primeNumber:= range primes {
            if primeNumber != 2 && primeNumber != 3 && primeNumber != 5 && n % primeNumber == 0 {
                return false
            }
        }
        return true
    }
}
