package main

import "fmt"

func isBadVersion(n int) bool {
	if n >= 1 {
		return true
	}
	return false
}

func firstBadVersion(n int) int {
	start := 1
	end := n
	middle := 0
	lastBadVersion := n
	for end >= start {
		fmt.Println(start, end, middle)
		middle = (start + end) / 2
		if isBadVersion(middle) {
			lastBadVersion = middle
			end = middle - 1
		} else {
			start = middle + 1
		}
	}
	return lastBadVersion
}

func main() {
	fmt.Println("Hello World", firstBadVersion(3))
}
