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

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	var newHead *ListNode = nil
	var looper *ListNode = nil
	var val int
	for list1 != nil && list2 != nil {
		if list1.Val > list2.Val {
			val = list2.Val
			list2 = list2.Next
		} else {
			val = list1.Val
			list1 = list1.Next
		}
		node := createNode(val)
		if newHead == nil {
			newHead = node
			looper = node
		} else {
			looper.Next = node
			looper = looper.Next
		}
	}
	for list1 != nil {
		node := createNode(list1.Val)
		list1 = list1.Next
		if newHead == nil {
			newHead = node
			looper = node
		} else {
			looper.Next = node
			looper = looper.Next
		}
	}
	for list2 != nil {
		node := createNode(list2.Val)
		list2 = list2.Next
		if newHead == nil {
			newHead = node
			looper = node
		} else {
			looper.Next = node
			looper = looper.Next
		}
	}
	return newHead
}

func main() {
	newList1 := createLinkedList([]int{1, 2, 3, 4, 5, 6})
	newList2 := createLinkedList([]int{1, 2, 3, 4, 5, 6})
	result := mergeTwoLists(newList1, newList2)
	fmt.Print("Result is : ")
	result.Print()
}
