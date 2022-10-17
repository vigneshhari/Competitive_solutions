package main

import "fmt"

func getPhoneCharecters(number byte) []string {
	m := map[byte][]string{
		'2': []string{"a", "b", "c"},
		'3': []string{"d", "e", "f"},
		'4': []string{"g", "h", "i"},
		'5': []string{"j", "k", "l"},
		'6': []string{"m", "n", "o"},
		'7': []string{"p", "q", "r", "s"},
		'8': []string{"t", "u", "v"},
		'9': []string{"w", "x", "y", "z"},
	}
	return m[number]
}

func recursiveSolver(pendingDigits string, currentCombinations []string) []string {
	if pendingDigits == "" {
		return currentCombinations
	}

	var finalResults []string
	for _, j := range getPhoneCharecters(pendingDigits[0]) {
		var newCombinations []string
		for _, k := range currentCombinations {
			newCombinations = append(newCombinations, k+j)
		}
		finalResults = append(finalResults, recursiveSolver(pendingDigits[1:], newCombinations)...)
	}
	return finalResults
}

func letterCombinations(digits string) []string {
	if digits == "" {
		return []string{}
	}
	return recursiveSolver(digits[1:], getPhoneCharecters(digits[0]))
}

func main() {
	fmt.Println(letterCombinations(""))
}
