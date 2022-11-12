package main

import "fmt"

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	stack := []*Node{root, nil}
	for len(stack) != 0 {
		currentNode := stack[0]
		stack = stack[1:]
		if currentNode == nil {
			if len(stack) == 0 {
				break
			}
			stack = append(stack, nil)
			continue
		}
		if currentNode.Left != nil {
			stack = append(stack, currentNode.Left)
		}
		if currentNode.Right != nil {
			stack = append(stack, currentNode.Right)
		}
		currentNode.Next = stack[0]
	}
	return root
}

func main() {
	fmt.Println("Right pointer added")
}
