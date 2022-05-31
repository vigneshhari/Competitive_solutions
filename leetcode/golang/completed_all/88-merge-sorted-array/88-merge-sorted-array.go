package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	pointer := m + n - 1
	m = m - 1
	n = n - 1
	for n >= 0 {
		if m >= 0 && nums1[m] > nums2[n] {
			nums1[pointer] = nums1[m]
			m--
		} else {
			nums1[pointer] = nums2[n]
			n--
		}
		pointer--
	}
}

func main() {

	var a = []int{0}
	var b = []int{1}
	merge(a, 0, b, len(b))
	fmt.Println(a)
}
