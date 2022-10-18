package main

import "fmt"

func intersect(nums1 []int, nums2 []int) []int {
	items := make(map[int]int)
	var repeating []int
	for _, j := range nums1 {
		_, ok := items[j]
		if ok {
			items[j]++
		} else {
			items[j] = 1
		}
	}
	for _, j := range nums2 {
		val, ok := items[j]
		if ok {
			if val <= 0 {
				continue
			}
			repeating = append(repeating, j)
			items[j]--
		}
	}
	return repeating
}

func main() {

	fmt.Println("Hello There", intersect([]int{4, 9, 5}, []int{9, 4, 9, 8, 4}))
}
