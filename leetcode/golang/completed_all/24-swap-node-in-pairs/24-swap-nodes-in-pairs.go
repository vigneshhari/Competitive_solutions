package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	newHead := ListNode{Val: -1, Next: head}
	tempHead := &newHead
	for tempHead != nil && tempHead.Next != nil {
		firstNode := tempHead.Next
		secondNode := firstNode.Next
		if secondNode == nil {
			break
		}
		secondNode.Next, firstNode.Next = firstNode, secondNode.Next
		tempHead.Next = secondNode
		tempHead = firstNode
	}
	return newHead.Next
}

func main() {
	head := ListNode{Val: -1, Next: nil}
	temp := &head
	arr := []int{1, 2, 3, 4}
	for _, val := range arr {
		newNode := ListNode{Val: val, Next: nil}
		temp.Next = &newNode
		temp = &newNode
	}
	swapPairs(&head)
	printLL := &head
	for printLL != nil {
		fmt.Print(printLL.Val, " , ")
		printLL = printLL.Next
	}

}
