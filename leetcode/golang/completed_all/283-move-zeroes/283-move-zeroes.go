package main

import "fmt"

func moveZeroes(nums []int) {
	zeroPointer := 0
	currentPointer := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {

		}
	}

}

func main() {
	nums := []int{0, 1, 0, 3, 12}
	moveZeroes(nums)
	fmt.Println("Hello World", nums)
}
