package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
	mapper := make(map[int32]int)
	for _, j := range magazine {
		mapper[j] += 1
	}
	for _, j := range ransomNote {
		val, ok := mapper[j]
		if ok {
			if val == 0 {
				return false
			}
			mapper[j] = val - 1
		} else {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("Can generate ransom :", canConstruct("aac", "aab"))
}
