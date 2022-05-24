package main

import "fmt"

func isValid(s string) bool {
	var stack []byte
	for i := 0; i < len(s); i++ {
		if s[i] == '{' || s[i] == '(' || s[i] == '[' {
			stack = append(stack, s[i])
		} else {
			if len(stack) == 0 {
				return false
			}
			if stack[len(stack)-1] == '(' && s[i] != ')' {
				return false
			} else if stack[len(stack)-1] == '{' && s[i] != '}' {
				return false
			} else if stack[len(stack)-1] == '[' && s[i] != ']' {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}

func main() {
	fmt.Print(isValid("{(}"))
}
