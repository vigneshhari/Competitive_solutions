package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, level int) int {
	if node == nil {
		return level - 1
	}
	val1 := recursiveSolver(node.Left, level+1)
	val2 := recursiveSolver(node.Right, level+1)
	if val1 > val2 {
		return val1
	}
	return val2
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	level := recursiveSolver(root, 1)
	return level
}

func main() {
	fmt.Println("Hello World")
}
