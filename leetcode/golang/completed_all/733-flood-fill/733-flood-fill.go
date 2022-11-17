package main

func recursiveSolver(grid [][]int, i, j, old int) {
	if grid[i][j] != old {
		return
	}
	if grid[i][j] == old {
		grid[i][j] = -1
		if i != 0 {
			recursiveSolver(grid, i-1, j, old)
		}
		if j != 0 {
			recursiveSolver(grid, i, j-1, old)
		}
		if i != len(grid)-1 {
			recursiveSolver(grid, i+1, j, old)
		}
		if j != len(grid[0])-1 {
			recursiveSolver(grid, i, j+1, old)
		}
	}
}

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	recursiveSolver(image, sr, sc, image[sr][sc])
	for i := 0; i < len(image); i++ {
		for j := 0; j < len(image[0]); j++ {
			if image[i][j] == -1 {
				image[i][j] = color
			}
		}
	}
	return image
}

func main() {

}
