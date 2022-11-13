package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root1 == nil {
		return root2
	} else {
		if root2 != nil {
			root1.Val = root1.Val + root2.Val
			if root1.Left == nil && root2.Left != nil {
				root1.Left = root2.Left
			} else {
				mergeTrees(root1.Left, root2.Left)
			}
			if root1.Right == nil && root2.Right != nil {
				root1.Right = root2.Right
			} else {
				mergeTrees(root1.Right, root2.Right)
			}
		}
	}
	return root1
}

func main() {
	fmt.Println("Hello World")
}
