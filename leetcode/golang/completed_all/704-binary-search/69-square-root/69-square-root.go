package main

import "fmt"

func mySqrt(x int) int {
	lIndex := 1
	rIndex := (x / 2) + 1
	currentIndex := 0
	for lIndex <= rIndex {
		currentIndex = lIndex + ((rIndex - lIndex) / 2)
		currentValue := currentIndex * currentIndex
		if currentValue == x {
			return currentIndex
		}
		if currentValue > x {
			rIndex = currentIndex - 1
		} else {
			lIndex = currentIndex + 1
		}
	}
	return lIndex - 1
}

func main() {
	fmt.Println(mySqrt(8))
}
