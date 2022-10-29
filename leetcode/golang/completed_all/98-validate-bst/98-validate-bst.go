package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, min, max int) bool {
	if node == nil {
		return true
	}
	if node.Val >= max || node.Val <= min {
		return false
	}
	return recursiveSolver(node.Left, min, node.Val) && recursiveSolver(node.Right, node.Val, max)
}

func isValidBST(root *TreeNode) bool {
	return recursiveSolver(root.Left, math.MinInt64, root.Val) && recursiveSolver(root.Right, root.Val, math.MaxInt64)
}

func main() {
	fmt.Println("Hello World")
}
