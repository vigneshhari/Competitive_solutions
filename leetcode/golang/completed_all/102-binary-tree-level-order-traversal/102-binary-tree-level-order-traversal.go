package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, results *[][]int, level int) {
	if node == nil {
		return
	}
	if len(*results) < level {
		*results = append(*results, []int{})
	}
	recursiveSolver(node.Left, results, level+1)
	(*results)[level] = append((*results)[level], node.Val)
	recursiveSolver(node.Right, results, level+1)
}

func levelOrder(root *TreeNode) [][]int {
	var results [][]int
	if root == nil {
		return results
	}
	recursiveSolver(root, &results, 0)
	return results
}

func main() {
	fmt.Println("Hello World")
}
