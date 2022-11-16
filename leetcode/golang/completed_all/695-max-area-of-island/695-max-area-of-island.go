package main

func recursiveSolver(grid [][]int, i, j int) int {
	if grid[i][j] == 0 {
		return 0
	}
	grid[i][j] = 0
	results := 1
	if i != 0 {
		results += recursiveSolver(grid, i-1, j)
	}
	if j != 0 {
		results += recursiveSolver(grid, i, j-1)
	}
	if i != len(grid)-1 {
		results += recursiveSolver(grid, i+1, j)
	}
	if j != len(grid[0])-1 {
		results += recursiveSolver(grid, i, j+1)
	}
	return results
}

func maxAreaOfIsland(grid [][]int) int {
	maxVal := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			max := recursiveSolver(grid, i, j)
			if max > maxVal {
				maxVal = max
			}
		}
	}
	return maxVal
}

func main() {

}
