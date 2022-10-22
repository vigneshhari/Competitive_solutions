package main

import "fmt"

func firstUniqChar(s string) int {
	mapper := make(map[int32]int)
	for _, j := range s {
		mapper[j] += 1
	}
	for i, j := range s {
		val, ok := mapper[j]
		if ok {
			if val == 1 {
				return i
			}
		}
	}
	return -1
}

func main() {
	fmt.Println("First unique character is", firstUniqChar("aabb"))
}
