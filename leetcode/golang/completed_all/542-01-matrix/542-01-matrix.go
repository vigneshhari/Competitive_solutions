package main

import (
	"fmt"
	"math"
)

func min(i, j int) int {
	if i > j {
		return j
	}
	return i
}

func checkMin(i, j int, mat [][]int, first bool) int {
	minVal := mat[i][j]
	if minVal == 0 {
		return 0
	}
	if i != 0 {
		minVal = min(minVal, mat[i-1][j])
	}
	if j != 0 {
		minVal = min(minVal, mat[i][j-1])
	}
	if i != len(mat)-1 {
		minVal = min(minVal, mat[i+1][j])
		if first && mat[i+1][j] == 0 {
			return 1
		}
	}
	if j != len(mat[0])-1 {
		minVal = min(minVal, mat[i][j+1])
		if first && mat[i][j+1] == 0 {
			return 1
		}
	}
	if minVal != mat[i][j] {
		return minVal + 1
	}
	return minVal
}

func updateMatrix(mat [][]int) [][]int {
	for i := 0; i < len(mat); i++ {
		for j := 0; j < len(mat[0]); j++ {
			if mat[i][j] == 1 {
				mat[i][j] = math.MaxInt32
			}
		}
	}
	for i := 0; i < len(mat); i++ {
		for j := 0; j < len(mat[0]); j++ {
			mat[i][j] = checkMin(i, j, mat, true)
		}
	}
	for i := len(mat) - 1; i >= 0; i-- {
		for j := len(mat[0]) - 1; j >= 0; j-- {
			mat[i][j] = checkMin(i, j, mat, false)
		}
	}

	return mat
}
func main() {
	val := [][]int{{0, 0, 0}, {0, 1, 0}, {1, 1, 1}}
	fmt.Println("The updated Matrix is ", updateMatrix(val))
}
