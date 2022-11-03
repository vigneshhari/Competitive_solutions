package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	var temp []byte
	pos := 0
	flag := false
	for {
		if len(strs[0]) == pos {
			return string(temp[:])
		}
		currentLetter := strs[0][pos]
		for i := 1; i < len(strs); i++ {
			if len(strs[i]) == pos || strs[i][pos] != currentLetter {
				flag = true
				break
			}
		}
		if flag {
			return string(temp[:])
		}
		temp = append(temp, currentLetter)
		pos++
	}
}

func main() {
	fmt.Println("Longest Prefix is : ", longestCommonPrefix([]string{"flower", "flow", "floight", ""}))
}
