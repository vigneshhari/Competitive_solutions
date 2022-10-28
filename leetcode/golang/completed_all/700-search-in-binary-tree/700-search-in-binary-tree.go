package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, target int) *TreeNode {
	if node == nil {
		return nil
	}
	if target < node.Val {
		return recursiveSolver(node.Left, target)
	} else if target > node.Val {
		return recursiveSolver(node.Right, target)
	}
	return node
}

func searchBST(root *TreeNode, val int) *TreeNode {
	return recursiveSolver(root, val)
}

func main() {
	fmt.Println("Hello World")
}
