package main

import (
	"fmt"
)

func isValidSudoku(board [][]byte) bool {
	mapper := make(map[int]map[byte]bool)
	for i, j := range board {
		for j, l := range j {
			if l == '.' {
				continue
			}
			rowKey := i
			columnKey := 10 + j
			miniSquareKey := 20 + (10 * ((i) / 3)) + ((j) / 3)
			_, rowOk := mapper[rowKey]
			_, columnOk := mapper[columnKey]
			_, miniSquareKeyOk := mapper[miniSquareKey]
			if !rowOk {
				mapper[rowKey] = make(map[byte]bool)
			}
			if !columnOk {
				mapper[columnKey] = make(map[byte]bool)
			}
			if !miniSquareKeyOk {
				mapper[miniSquareKey] = make(map[byte]bool)
			}
			_, rowOk = mapper[rowKey][l]
			_, columnOk = mapper[columnKey][l]
			_, miniSquareKeyOk = mapper[miniSquareKey][l]
			if rowOk || columnOk || miniSquareKeyOk {
				return false
			}
			mapper[rowKey][l] = true
			mapper[columnKey][l] = true
			mapper[miniSquareKey][l] = true
		}
	}
	return true
}

func main() {
	fmt.Print("Valid Sudoku :", isValidSudoku([][]byte{{'5', '3', '.', '.', '7', '.', '.', '.', '.'}, {'6', '.', '.', '1', '9', '5', '.', '.', '.'}, {'.', '9', '8', '.', '.', '.', '.', '6', '.'}, {'8', '.', '.', '.', '6', '.', '.', '.', '3'}, {'4', '.', '.', '8', '.', '3', '.', '.', '1'}, {'7', '.', '.', '.', '2', '.', '.', '.', '6'}, {'.', '6', '.', '.', '.', '.', '2', '8', '.'}, {'.', '.', '.', '4', '1', '9', '.', '.', '5'}, {'.', '.', '.', '.', '8', '.', '.', '7', '9'}}))
}
