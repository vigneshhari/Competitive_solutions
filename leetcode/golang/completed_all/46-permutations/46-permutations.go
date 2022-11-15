package main

import "fmt"

func recursiveSolver(options, currentPath []int, results *[][]int) {
	if len(options) == 1 {
		*results = append(*results, append(currentPath, options[0]))
		return
	}
	for i, j := range options {
		clone := append([]int{}, options...)
		recursiveSolver(append(clone[:i], clone[i+1:]...), append(currentPath, j), results)
	}
}

func permute(nums []int) [][]int {
	var results [][]int
	recursiveSolver(nums, []int{}, &results)
	return results
}

func main() {
	fmt.Println("Permutations are :", permute([]int{1, 2, 3, 4}))
}
