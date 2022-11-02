package main

import (
	"fmt"
	"math"
)

type ListNode struct {
	Val  int
	Next *ListNode
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

func middleNode(head *ListNode) *ListNode {
	length := linkedListLength(head)
	middlenode := int(math.Ceil(float64(length / 2)))
	for i := 0; i < middlenode; i++ {
		head = head.Next
	}
	return head
}

func main() {
	newList1 := createLinkedList([]int{1, 2})
	result := middleNode(newList1)
	fmt.Print("Result is : ")
	if result != nil {
		fmt.Println(result.Val)
	}
}
