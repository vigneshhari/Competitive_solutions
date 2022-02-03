package main

import "fmt"

func findFinalValue(nums []int, original int) int {
	var numMap = make(map[int]bool)
	for _, value := range nums {
		numMap[value] = true
	}
	for true {
		if numMap[original] {
			original *= 2
		} else {
			break
		}
	}
	return original
}

func main() {

	fmt.Println(findFinalValue([]int{5, 3, 6, 1, 12}, 3))
}
