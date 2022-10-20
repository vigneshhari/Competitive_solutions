package main

import (
	"fmt"
)

func searchMatrix(matrix [][]int, target int) bool {

	lIndex, rIndex := 0, len(matrix)*len(matrix[0])

	for lIndex < rIndex {
		currentIndex := ((lIndex + rIndex) / 2)

		i, j := currentIndex/len(matrix[0]), currentIndex%len(matrix[0])
		currentValue := matrix[i][j]
		if currentValue == target {
			return true
		}
		if currentValue > target {
			rIndex = currentIndex
		} else {
			lIndex = currentIndex + 1
		}
	}
	return false
}

func main() {
	var a = [][]int{{-1, 0, 3, 5, 9, 12}}
	fmt.Println(searchMatrix(a, 9))
}
