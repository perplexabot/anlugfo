/*
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.

Return an array containing the index of the row, and the number of ones in it.

Example 1:
    Input: mat = [[0,1],[1,0]]
    Output: [0,1]
    Explanation: Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of 
        ones (1). So, the answer is [0,1]. 

Example 2:
    Input: mat = [[0,0,0],[0,1,1]]
    Output: [1,2]
    Explanation: The row indexed 1 has the maximum count of ones (2). So we return its index, 1, and the count. So, the answer 
        is [1,2].

Example 3:
    Input: mat = [[0,0],[1,1],[0,0]]
    Output: [1,2]
    Explanation: The row indexed 1 has the maximum count of ones (2). So the answer is [1,2].

Constraints:
    - m == mat.length 
    - n == mat[i].length 
    - 1 <= m, n <= 100 
    - mat[i][j] is either 0 or 1.

A:
    empty matrix [], [[]]
        not possible
    non symmetric matrix
        possible
    n x 1 matrix
        return first row with 1
    1 x n matrix
        return number of 1s in row
*/

package main

import (
    "fmt"
)

func rowAndMaximumOnes(mat [][]int) []int {
    ones_max := 0
    indx_max := 0
    for rowi, row := range mat {
        ones := 0
        for _, elem := range row {
            if elem == 1 {
                ones ++
            }
        }

        if ones > ones_max {
            ones_max = ones
            indx_max = rowi
        }
    }
    return []int{indx_max,ones_max}
}

func main() {
    got := rowAndMaximumOnes([][]int{{1,2},{1,1}})
    fmt.Printf("got: %v\n", got)
}
