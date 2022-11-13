package main

import "fmt"

func isDigit(i byte) bool {
	return i == 48 || i == 49 || i == 50 || i == 51 || i == 52 || i == 53 || i == 54 || i == 55 || i == 56 || i == 57
}

func recursiveSolver(s, curString string, pos int, res *[]string) {
	if len(s) == pos {
		*res = append(*res, curString)
		return
	}
	if isDigit(s[pos]) {
		recursiveSolver(s, curString+string(s[pos]), pos+1, res)
		return
	}
	if s[pos] >= 'a' && s[pos] <= 'z' {
		recursiveSolver(s, curString+string(s[pos]-32), pos+1, res)
		recursiveSolver(s, curString+string(s[pos]), pos+1, res)
	} else {
		recursiveSolver(s, curString+string(s[pos]+32), pos+1, res)
		recursiveSolver(s, curString+string(s[pos]), pos+1, res)
	}

}

func letterCasePermutation(s string) []string {
	var results []string
	recursiveSolver(s, "", 0, &results)
	return results
}

func main() {
	fmt.Println("Permutations are ", letterCasePermutation("3z4"))
}
