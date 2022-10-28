package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode) {
	if node == nil {
		return
	}
	node.Right, node.Left = node.Left, node.Right
	recursiveSolver(node.Left)
	recursiveSolver(node.Right)
}

func invertTree(root *TreeNode) *TreeNode {
	recursiveSolver(root)
	return root
}

func main() {
	fmt.Println("Hello World")
}
