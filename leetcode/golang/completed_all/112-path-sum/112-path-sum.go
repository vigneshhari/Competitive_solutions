package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, targetSum int, currentSum int) bool {
	if node == nil {
		return false
	}
	currentSum = currentSum + node.Val
	if node.Left == nil && node.Right == nil {
		return currentSum == targetSum
	}
	return recursiveSolver(node.Left, targetSum, currentSum) || recursiveSolver(node.Right, targetSum, currentSum)
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	return recursiveSolver(root, targetSum, 0)
}

func main() {
	fmt.Println("Hello World")
}
