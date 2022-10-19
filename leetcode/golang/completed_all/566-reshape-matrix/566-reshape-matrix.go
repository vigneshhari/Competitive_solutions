package main

import "fmt"

func matrixReshape(mat [][]int, r int, c int) [][]int {
	if len(mat)*len(mat[0]) != r*c {
		return mat
	}
	currentLooper := 0
	var currentRow []int
	var result [][]int
	for _, j := range mat {
		for _, k := range j {
			currentRow = append(currentRow, k)
			currentLooper++
			if currentLooper == c {
				result = append(result, currentRow)
				currentRow = []int{}
				currentLooper = 0
			}
		}
	}
	return result
}

func main() {
	fmt.Println("Hello World!", matrixReshape([][]int{[]int{1, 2}, []int{3, 4}}, 4, 1))
}
