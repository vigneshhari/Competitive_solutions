package main

import "fmt"

func isValid(s string) bool {
	stack := make([]byte, len(s))
	pointer := -1
	for i := 0; i < len(s); i++ {
		if s[i] == '{' || s[i] == '(' || s[i] == '[' {
			pointer++
			stack[pointer] = s[i]
		} else {
			if pointer == -1 {
				return false
			}
			if stack[pointer] == '(' && s[i] != ')' {
				return false
			} else if stack[pointer] == '{' && s[i] != '}' {
				return false
			} else if stack[pointer] == '[' && s[i] != ']' {
				return false
			}
			pointer--
		}
	}
	return pointer == -1
}

func main() {
	fmt.Print(isValid("()"))
}
