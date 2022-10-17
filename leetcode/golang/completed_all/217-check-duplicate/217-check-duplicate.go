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

func main() {

	fmt.Println(containsDuplicate([]int{1, 2, 3, 4, 4}))

}
