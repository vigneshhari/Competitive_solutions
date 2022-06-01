package main

import (
	"fmt"
)

func searchInsert(nums []int, target int) int {
	lIndex := 0
	rIndex := len(nums) - 1
	currentIndex := 0
	for lIndex <= rIndex {
		currentIndex = lIndex + ((rIndex - lIndex) / 2)
		currentValue := nums[currentIndex]
		if currentValue == target {
			return currentIndex
		}
		if currentValue > target {
			rIndex = currentIndex - 1
		} else {
			lIndex = currentIndex + 1
		}
	}
	return lIndex
}

func main() {
	var a = []int{-1, 0, 3, 5, 9, 12}
	fmt.Println(searchInsert(a, 13))
}
