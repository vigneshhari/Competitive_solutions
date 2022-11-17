package main

func recursiveSolver(grid [][]int, i, j, old, newColor int) {
	if grid[i][j] != old || grid[i][j] == newColor {
		return
	}
	if grid[i][j] == old {
		grid[i][j] = newColor
		if i != 0 {
			recursiveSolver(grid, i-1, j, old, newColor)
		}
		if j != 0 {
			recursiveSolver(grid, i, j-1, old, newColor)
		}
		if i != len(grid)-1 {
			recursiveSolver(grid, i+1, j, old, newColor)
		}
		if j != len(grid[0])-1 {
			recursiveSolver(grid, i, j+1, old, newColor)
		}
	}
}

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	recursiveSolver(image, sr, sc, image[sr][sc], color)
	return image
}

func main() {

}
