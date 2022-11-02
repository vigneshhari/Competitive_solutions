package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func (this *ListNode) Print() {
	currentNode := this
	for true {
		fmt.Print(currentNode.Val, " | ")
		currentNode = currentNode.Next
		if currentNode == nil {
			break
		}
	}
	fmt.Println()
}

func addAtTail(this *ListNode, val int) *ListNode {
	lastNode := this
	if lastNode != nil {
		for lastNode.Next != nil {
			lastNode = lastNode.Next
		}
	}
	newObj := ListNode{}
	newObj.Val = val
	newObj.Next = nil
	if lastNode == nil {
		return &newObj
	} else {
		lastNode.Next = &newObj
	}
	return this

}
func createLinkedList(list []int) *ListNode {
	var newListNode *ListNode = nil
	for _, j := range list {
		newListNode = addAtTail(newListNode, j)
	}
	return newListNode
}

func linkedListLength(head *ListNode) int {
	length := 0
	for head != nil {
		length++
		head = head.Next
	}
	return length
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	newHead := &ListNode{Val: -1, Next: head}
	fastPointer := newHead
	slowPointer := newHead
	for i := 0; i < n; i++ {
		fastPointer = fastPointer.Next
	}
	for fastPointer.Next != nil {
		fastPointer, slowPointer = fastPointer.Next, slowPointer.Next
	}
	slowPointer.Next = slowPointer.Next.Next
	newHead = newHead.Next
	return newHead
}

func removeNthFromEndTwoPass(head *ListNode, n int) *ListNode {
	newHead := &ListNode{Val: -1, Next: head}
	loopHead := newHead
	length := linkedListLength(loopHead)
	selectedNode := length - n - 1
	for i := 0; i < selectedNode; i++ {
		loopHead = loopHead.Next
	}
	loopHead.Next = loopHead.Next.Next
	newHead = newHead.Next
	return newHead
}

func main() {
	newList1 := createLinkedList([]int{1})
	result := removeNthFromEnd(newList1, 1)
	fmt.Print("Result is : ")
	if result != nil {
		result.Print()
	}
}
