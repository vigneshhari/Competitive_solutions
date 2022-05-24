package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	temp := x
	reversed := 0
	position := 0
	for ; x > 0; x = x / 10 {
		reversed = (reversed * 10) + (x % 10)
		position += 1
	}
	if temp == reversed {
		return true
	}
	return false
}

func main() {
	fmt.Println(isPalindrome(121))
}
