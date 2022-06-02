package main

import "fmt"

func isPerfectSquare(num int) bool {
	lIndex := 1
	rIndex := (num / 2) + 1
	currentIndex := 0
	for lIndex <= rIndex {
		currentIndex = lIndex + ((rIndex - lIndex) / 2)
		currentValue := currentIndex * currentIndex
		if currentValue == num {
			return true
		}
		if currentValue > num {
			rIndex = currentIndex - 1
		} else {
			lIndex = currentIndex + 1
		}
	}
	return false
}

func main() {
	fmt.Println(isPerfectSquare(256))
}
