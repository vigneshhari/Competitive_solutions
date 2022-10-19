package main

import "fmt"

func generate(numRows int) [][]int {

	var i, j int
	result := [][]int{{1}}
	for i = 2; i <= numRows; i++ {
		currentLine := []int{1}
		for j = 1; j < i-1; j++ {
			currentLine = append(currentLine, result[i-2][j-1]+result[i-2][j])
		}
		currentLine = append(currentLine, 1)
		result = append(result, currentLine)
	}

	return result
}

func main() {
	fmt.Println("Hello World", generate(30))
}
