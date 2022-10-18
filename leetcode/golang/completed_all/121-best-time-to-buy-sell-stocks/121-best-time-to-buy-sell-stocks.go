package main

import "fmt"

func maxProfit(nums []int) int {
	globalMaxima := 0
	localMaxima := nums[0]
	for _, j := range nums[1:] {
		check := j - localMaxima
		if check < 0 {
			localMaxima = j
			continue
		}
		if check > globalMaxima {
			globalMaxima = check
		}

	}
	return globalMaxima
}

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
}
