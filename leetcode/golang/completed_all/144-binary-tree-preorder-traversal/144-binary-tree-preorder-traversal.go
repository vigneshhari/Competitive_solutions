package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, results *[]int) {
	if node == nil {
		return
	}
	*results = append(*results, node.Val)
	recursiveSolver(node.Left, results)
	recursiveSolver(node.Right, results)
}

func preorderTraversal(root *TreeNode) []int {
	var results []int
	if root == nil {
		return results
	}
	recursiveSolver(root, &results)
	return results
}

func main() {
	fmt.Println("Hello World")
}
