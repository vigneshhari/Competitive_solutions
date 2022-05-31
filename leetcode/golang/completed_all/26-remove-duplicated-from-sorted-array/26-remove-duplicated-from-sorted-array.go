package main

import "fmt"

func removeDuplicates(nums []int) int {
	writePointer := 1
	for i := 1; i < len(nums); i++ {
		if nums[i-1] != nums[i] {
			nums[writePointer] = nums[i]
			writePointer++
		}
	}
	return writePointer
}

func main() {
	var a = []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)
}
