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

func createNode(Val int) *ListNode {
	newObj := ListNode{}
	newObj.Val = Val
	newObj.Next = nil
	return &newObj
}

func deleteDuplicates(head *ListNode) *ListNode {
	fakeHead := createNode(-101)
	fakeHead.Next = head
	looper := head
	previouslooper := fakeHead
	for looper != nil {
		if looper.Val == previouslooper.Val {
			previouslooper.Next = looper.Next
		} else {
			previouslooper = previouslooper.Next
		}
		looper = looper.Next
	}
	return fakeHead.Next
}

func main() {
	newList1 := createLinkedList([]int{1, 2, 2, 3, 4, 4, 5, 6, 6})
	result := deleteDuplicates(newList1)
	fmt.Print("Result is : ", result)
}
