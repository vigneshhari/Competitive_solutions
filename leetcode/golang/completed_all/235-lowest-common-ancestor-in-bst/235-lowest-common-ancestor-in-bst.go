package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursiveSolver(node *TreeNode, target int, currentStack []*TreeNode) []*TreeNode {
	if node == nil {
		return nil
	}
	if target < node.Val {
		return recursiveSolver(node.Left, target, append(currentStack, node))
	} else if target > node.Val {
		return recursiveSolver(node.Right, target, append(currentStack, node))
	}
	return append(currentStack, node)
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	stackP := recursiveSolver(root, p.Val, []*TreeNode{})
	stackQ := recursiveSolver(root, q.Val, []*TreeNode{})
	for i := 0; i < len(stackP); i++ {
		if i >= (len(stackQ)) || stackP[i] != stackQ[i] {
			return stackP[i-1]
		}
	}
	return stackQ[len(stackP)-1]
}

func main() {
	fmt.Println("Hello World")
}
