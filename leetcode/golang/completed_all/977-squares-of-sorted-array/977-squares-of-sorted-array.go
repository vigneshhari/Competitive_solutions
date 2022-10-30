package main

import "fmt"

func sortedSquares(nums []int) []int {
	var lis1, lis2, result []int
	for _, j := range nums {
		if j < 0 {
			lis1 = append(lis1, j*j)
		} else {
			lis2 = append(lis2, j*j)
		}
	}
	pointer1, pointer2 := len(lis1)-1, 0
	for pointer1 >= 0 && pointer2 < len(lis2) {
		if lis1[pointer1] < lis2[pointer2] {
			result = append(result, lis1[pointer1])
			pointer1--
		} else {
			result = append(result, lis2[pointer2])
			pointer2++
		}
	}
	for pointer1 >= 0 {
		result = append(result, lis1[pointer1])
		pointer1--
	}
	for pointer2 < len(lis2) {
		result = append(result, lis2[pointer2])
		pointer2++
	}
	return result
}

func main() {
	fmt.Println("New Sorted List is ", sortedSquares([]int{-4, -1, 0, 1, 2, 3, 4, 5, 6, 7}))
}
