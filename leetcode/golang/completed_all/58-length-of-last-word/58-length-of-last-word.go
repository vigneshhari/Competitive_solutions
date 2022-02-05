package main

import "fmt"

func lengthOfLastWord(s string) int {
	spaces := true
	count := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == ' ' && !spaces {
			break
		}
		if s[i] == ' ' {
			continue
		}
		count++
		spaces = false
	}

	return count
}

func main() {

	fmt.Println(lengthOfLastWord("Hello Theree    "))

}
