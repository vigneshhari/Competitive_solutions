package main

import "fmt"

func orangesRotting(grid [][]int) int {
	var stack [][]int
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 2 {
				stack = append(stack, []int{i, j, 2})
			}
		}
	}
	maxValue := 0
	for len(stack) != 0 {
		currentNode := stack[0]
		i, j, currentTime := currentNode[0], currentNode[1], currentNode[2]
		currentTime++
		stack = stack[1:]
		if i != 0 {
			if grid[i-1][j] == 1 {
				grid[i-1][j] = currentTime
				stack = append(stack, []int{i - 1, j, currentTime})
			}
		}
		if j != 0 {
			if grid[i][j-1] == 1 {
				grid[i][j-1] = currentTime
				stack = append(stack, []int{i, j - 1, currentTime})

			}
		}
		if i < len(grid)-1 {
			if grid[i+1][j] == 1 {
				grid[i+1][j] = currentTime
				stack = append(stack, []int{i + 1, j, currentTime})

			}
		}
		if j < len(grid[0])-1 {
			if grid[i][j+1] == 1 {
				grid[i][j+1] = currentTime
				stack = append(stack, []int{i, j + 1, currentTime})

			}
		}
		if currentTime-2 > maxValue {
			maxValue = currentTime - 3
		}
	}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				return -1
			}
		}
	}
	return maxValue
}

func main() {
	fmt.Println("Minimum minutes to wait is : ", orangesRotting([][]int{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}))
}
