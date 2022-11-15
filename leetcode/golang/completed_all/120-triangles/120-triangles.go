package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minimumTotal(triangle [][]int) int {
	if len(triangle) == 1 {
		return triangle[0][0]
	}
	for i := len(triangle) - 2; i >= 1; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			fmt.Println(i, j)
			triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
		}
	}
	return min(triangle[1][0], triangle[1][1]) + triangle[0][0]
}

func main() {
	fmt.Println("Shortest path is", minimumTotal([][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}))
}
