package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func lengthOfLongestSubstring(s string) int {
	wordStart := 0
	maxLength := 0
	mapper := make(map[int32]int)
	for i, j := range s {
		val, ok := mapper[j]
		if ok && val >= wordStart {
			wordStart = val + 1
		}
		mapper[j] = i
		maxLength = max(maxLength, i-wordStart+1)
	}
	return maxLength
}

func main() {
	fmt.Println("The length of the max substring is : ", lengthOfLongestSubstring("abcabcbb"))
}
