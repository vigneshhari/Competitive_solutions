package main

import (
	"fmt"
)

func search(nums []int, target int) int {
	lIndex := 0
	rIndex := len(nums) - 1
	for lIndex < rIndex {
		currentIndex := ((lIndex + rIndex) / 2)
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
	return -1
}

func main() {
	var a = []int{-1, 0, 3, 5, 9, 12}
	fmt.Println(search(a, 9))
}
