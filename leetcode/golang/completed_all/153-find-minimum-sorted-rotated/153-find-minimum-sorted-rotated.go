package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
func findMin(nums []int) int {
	lIndex := 0
	rIndex := len(nums) - 1
	if len(nums) == 1 {
		return nums[0]
	}
	if len(nums) == 2 {
		if nums[0] < nums[1] {
			return nums[0]
		}
		return nums[1]
	}
	for lIndex < rIndex {
		lValue := nums[lIndex]
		currentIndex := (lIndex + rIndex) / 2
		currentValue := nums[currentIndex]
		if nums[max(currentIndex-1, 0)] > currentValue {
			return currentValue
		} else if nums[min(currentIndex+1, len(nums)-1)] < currentValue {
			return nums[min(currentIndex+1, len(nums)-1)]
		}
		if currentValue < lValue {
			rIndex = currentIndex - 1
		} else {
			lIndex = currentIndex + 1
		}
	}
	return nums[0]
}

func main() {
	var a = []int{5, 1, 2, 3, 4}
	fmt.Println(findMin(a))
}
