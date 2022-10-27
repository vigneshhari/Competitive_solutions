package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(left *TreeNode, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	} else if left == nil || right == nil {
		return false
	}
	return left.Val == right.Val && recursiveSolver(left.Right, right.Left) && recursiveSolver(left.Left, right.Right)
}

func isSymmetric(root *TreeNode) bool {
	return recursiveSolver(root, root)
}

func main() {
	fmt.Println("Hello World")
}
