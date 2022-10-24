package main

import "fmt"

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

func createLinkedList(list []int) *ListNode {
	var newListNode *ListNode = nil
	for _, j := range list {
		newListNode = addAtTail(newListNode, j)
	}
	return newListNode
}

func AddAtHead(this *ListNode, val int) *ListNode {
	newObj := ListNode{}
	newObj.Val = val
	newObj.Next = this
	return &newObj
}

func reverseList(head *ListNode) *ListNode {
	looper := head
	var fakeHead *ListNode = nil
	for looper != nil {
		fakeHead = AddAtHead(fakeHead, looper.Val)
		looper = looper.Next
	}
	return fakeHead
}

func main() {
	newList1 := createLinkedList([]int{1, 2, 3, 4, 5, 6})
	result := reverseList(newList1)
	fmt.Print("Result is : ")
	if result != nil {
		result.Print()
	}
}
