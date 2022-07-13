package main

func multiplyString(str rune, times int) string {
	finalString := ""
	for i := 0; i < times; i++ {
		finalString += string(str)
	}
	return finalString
}

func findSubstring(currentChar rune, counter map[rune]int, repeatLimit int) (string, bool) {
	var lexical_list = []rune{'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'}
	for _, letter := range lexical_list {
		if letter != currentChar && counter[letter] > 0 {
			repeatCount := counter[letter]
			if ((currentChar > letter) && counter[currentChar] != 0) && currentChar != '-' {
				repeatCount = 1
			} else {
				if counter[letter] > repeatLimit {
					repeatCount = repeatLimit
				}
			}
			counter[letter] -= repeatCount
			return multiplyString(letter, repeatCount), false
		}
	}
	return "", true
}

func repeatLimitedString(s string, repeatLimit int) string {
	var counter = map[rune]int{}
	for _, a := range s {
		counter[a] += 1
	}
	finalString := ""
	currentLetter := rune('-')
	for true {
		subString, stop := findSubstring(currentLetter, counter, repeatLimit)
		if stop {
			break
		}
		finalString += subString
		currentLetter = rune(subString[0])
	}
	return finalString
}

func main() {
	print(repeatLimitedString("robnsdvpuxbapuqgopqvxdrchivlifeepy", 2))
}
