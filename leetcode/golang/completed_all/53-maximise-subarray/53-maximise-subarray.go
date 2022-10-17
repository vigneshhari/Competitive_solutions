package main

import "fmt"

func maxSubArray(nums []int) int {
	globalMaxima := nums[0]
	localMaxima := 0
	for _, j := range nums {
		localMaxima += j
		if localMaxima > globalMaxima {
			globalMaxima = localMaxima
		}
		if localMaxima < 0 {
			localMaxima = 0
		}
	}
	return globalMaxima
}

func main() {
	fmt.Println(maxSubArray([]int{5, 4, -1, 7, 8}))
}
