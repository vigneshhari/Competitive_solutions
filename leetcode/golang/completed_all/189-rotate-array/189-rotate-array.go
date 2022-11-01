package main

import "fmt"

func rotate(nums []int, k int) {
	c := k % len(nums)
	count, startPos := 0, 0
	for ; count < len(nums); startPos++ {
		currentPos := startPos
		prev := nums[currentPos]
		for true {
			nextValue := (currentPos + c) % len(nums)
			nums[nextValue], prev = prev, nums[nextValue]
			currentPos = nextValue
			count += 1
			if currentPos == startPos {
				break
			}
		}
	}
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	rotate(nums, 3)
	fmt.Println("Rotated Array is : ", nums)
}
