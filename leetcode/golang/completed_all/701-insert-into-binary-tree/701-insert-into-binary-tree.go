package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, target int) *TreeNode {
	if node == nil {
		return &TreeNode{Val: target}
	}
	if target < node.Val {
		node.Left = recursiveSolver(node.Left, target)
	} else if target > node.Val {
		node.Right = recursiveSolver(node.Right, target)
	}
	return node
}

func insertIntoBST(root *TreeNode, val int) *TreeNode {
	return recursiveSolver(root, val)
}

func main() {
	fmt.Println("Hello World")
}
