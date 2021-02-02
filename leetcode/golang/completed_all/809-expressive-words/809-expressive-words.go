package main

import "fmt"

type Expressiveness struct {
	letter uint8 ;
	count int ;
	next *Expressiveness;
}

func makeExpressiveness(word string) *Expressiveness {
	if(len(word) == 0){return &Expressiveness{} }
	header := &Expressiveness{letter: word[0] , count: 1}
	expression := header
	for i := 1; i < len(word); i++ {
		if(expression.letter == word[i]){
			expression.count++
		}else{
			newExpression := &Expressiveness{letter: word[i] , count : 1}
			expression.next = newExpression
			expression = expression.next
		}
 	}
	return header
}

func checkExpressive(word string , expressiveHeader *Expressiveness) bool{
	word = word + "-"
	currentLetter := word[0]
	currentCount := 0
	for index , _ := range word {
		if(currentLetter == word[index] ){
			currentCount++;
		}else{
			if(expressiveHeader == nil){return false}
			if(expressiveHeader.letter != currentLetter){return false}
			if(currentCount > expressiveHeader.count){return false}
			if(currentCount != expressiveHeader.count && expressiveHeader.count < 3){return false}
			expressiveHeader = expressiveHeader.next
			currentCount = 1
			currentLetter = word[index]
		}
	}
	if(expressiveHeader == nil){return true}
	return false
}
func expressiveWords(S string, words []string) int {
	wordCount := 0
	expressiveHeader := makeExpressiveness(S)
	for _ , word := range words {
		if(checkExpressive(word , expressiveHeader)){wordCount++}
	}
	return wordCount
}

func main(){

	fmt.Println(expressiveWords("" , []string{"hello", "hi", "helo"}))
}
