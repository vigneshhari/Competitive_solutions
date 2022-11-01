package main

import "fmt"

func reverseString(s []byte) {
	for i := 0; i < len(s)/2; i++ {
		s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
	}
}

func main() {
	tmp := []byte{'h', 'e', 'l', 'l', 'o'}
	reverseString(tmp)
	fmt.Println("Reversed Byte array is", tmp)
}
