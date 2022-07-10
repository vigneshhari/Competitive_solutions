package main

import "fmt"

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func hasGroupsSizeX(deck []int) bool {
	var dict = map[int]int{}
	for _, i := range deck {
		dict[i]++
	}
	maxSize := dict[deck[0]]
	for _, element := range dict {
		maxSize = gcd(maxSize, element)
	}
	return maxSize >= 2
}

func main() {
	fmt.Println(hasGroupsSizeX([]int{1, 1, 2, 2, 2, 2}))
}
