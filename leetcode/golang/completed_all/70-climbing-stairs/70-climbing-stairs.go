package main

import "fmt"

func climbStairs(n int) int {
	a, b := 1, 1
	for ; n >= 2; n-- {
		a, b = b, a+b
	}
	return b
}

func main() {
	fmt.Println("The number of ways to reach is ", climbStairs(1))
}
