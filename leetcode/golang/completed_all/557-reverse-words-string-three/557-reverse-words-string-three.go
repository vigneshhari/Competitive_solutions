package main

import "fmt"

func reverseString(s []byte, start, end int) {
	for i := 0; i < (end-start+1)/2; i++ {
		s[start+i], s[end-i] = s[end-i], s[start+i]
	}
}

func reverseWords(s string) string {
	byteArray := []byte(s)
	lastPosition := 0
	for i, j := range s {
		if j == int32(byte(' ')) {
			reverseString(byteArray, lastPosition, i-1)
			lastPosition = i + 1
		}
	}
	reverseString(byteArray, lastPosition, len(s)-1)
	return string(byteArray[:])
}

func main() {
	fmt.Println("Reversed String is : ", reverseWords("Let's take LeetCode contest"))
}
