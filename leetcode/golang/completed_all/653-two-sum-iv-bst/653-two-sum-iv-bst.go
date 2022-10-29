package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, target int, mapper map[int]bool) bool {
	if node == nil {
		return false
	}
	pos, ok := mapper[target-node.Val]
	if ok && pos {
		return true
	}
	mapper[node.Val] = true
	return recursiveSolver(node.Left, target, mapper) || recursiveSolver(node.Right, target, mapper)
}

func findTarget(root *TreeNode, k int) bool {
	mapper := make(map[int]bool)
	return recursiveSolver(root, k, mapper)
}

func main() {
	fmt.Println("Hello World")
}
