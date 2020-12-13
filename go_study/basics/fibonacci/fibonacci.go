package main

import "fmt"

func fibonacci() func() int {
	current := 0
	last := 0
	return func() int {
		if current == 0 {
			current = 1
			return last
		}
		temp := last + current
		last = current
		current = temp
		return last
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
