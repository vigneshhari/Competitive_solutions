package main

import "fmt"

func containsDuplicate(nums []int) bool {
	items := make(map[int]bool)
	for _, j := range nums {
		_, err := items[j]
		if err {
			return true
		}
		items[j] = true
	}
	return false
}

func twoSum(nums []int, target int) []int {
	items := make(map[int]int)
	for i, j := range nums {
		pos, ok := items[target-j]
		if ok && pos != i {
			return []int{i, pos}
		}
		items[j] = i
	}
	return []int{-1, -1}
}

func main() {

	fmt.Println(twoSum([]int{3, 3}, 6))

}
