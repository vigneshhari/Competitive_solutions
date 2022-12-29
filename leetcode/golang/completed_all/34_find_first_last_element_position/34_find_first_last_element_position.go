package main

import "fmt"

func search(nums []int, target int, rev bool) int {
	lIndex := 0
	rIndex := len(nums) - 1
	currentIndex := 0
	for lIndex < rIndex {
		currentIndex = (lIndex + rIndex) / 2
		currentValue := nums[currentIndex]
		if currentValue == target {
			if rev {
				rIndex = currentIndex - 1
			} else {
				lIndex = currentIndex + 1
			}
		} else if currentValue > target {
			rIndex = currentIndex - 1
		} else {
			lIndex = currentIndex + 1
		}
	}
	return currentIndex
}

func searchRange(nums []int, target int) []int {
	leftpos := search(nums, target, true)
	rightpos := search(nums, target, false)
	fmt.Println(leftpos, rightpos)
	return []int{-1, -1}
}

func main() {
	searchRange([]int{5, 7, 7, 8, 8, 10}, 8)
}
