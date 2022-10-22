package main

import "fmt"

func isAnagram(s string, t string) bool {
	mapper := make(map[int32]int)
	for _, j := range s {
		mapper[j] += 1
	}
	totalCharacters := len(mapper)
	for _, j := range t {
		val, ok := mapper[j]
		if ok {
			if val == 0 {
				return false
			}
			if val == 1 {
				totalCharacters--
			}
			mapper[j] = val - 1
		} else {
			return false
		}
	}
	return totalCharacters == 0
}

func main() {
	fmt.Println("Can generate anagram :", isAnagram("cats", "tac"))
}
