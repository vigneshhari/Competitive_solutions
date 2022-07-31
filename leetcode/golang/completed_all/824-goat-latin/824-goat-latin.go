package main

import "fmt"

func checkVowel(c int) bool {
	vowels := []int{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	for _, a := range vowels {
		if a == c {
			return true
		}
	}
	return false
}

func convertWord(word string, counter int) string {
	if checkVowel(int(word[0])) {
		word += "ma"
	} else {
		temp := string(word[0])
		word = word[1:] + temp + "ma"
	}
	for i := 0; i < counter; i++ {
		word += "a"
	}
	fmt.Println(word)
	return word
}

func toGoatLatin(sentence string) string {
	temp := ""
	counter := 1
	result := ""
	for _, c := range sentence {
		if c != ' ' {
			temp += string(c)
		} else {
			result += convertWord(temp, counter) + " "
			temp = ""
			counter++
		}
	}
	result += convertWord(temp, counter)
	return result
}

func main() {
	fmt.Println(toGoatLatin("The quick brown fox jumped over the lazy dog"))
}
