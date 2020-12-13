package main

import "fmt"

func add(x, y int) (sum, difference int) {
	sum = x + y
	difference = x - y
	return
}

func main() {
	sum, difference := add(42, 13)
	fmt.Println(sum, difference)
	return
}
