package main

import (
	"fmt"

)
type MyLinkedList struct {
header *Node
}

type Node struct {
	val int
	next *Node
}


func Constructor() MyLinkedList {
return MyLinkedList{ &Node{ }};
}


func (this *MyLinkedList) Get(index int) int {
	currentNode := this.header
	for i:=0 ; i<index; i++ {
		currentNode = currentNode.next
		if(currentNode.next ==  nil){return -1}
	}
	return currentNode.val
}


func (this *MyLinkedList) AddAtHead(val int)  {
	newObj := Node{}
	newObj.val = val
	newObj.next = this.header
	this.header = &newObj
}


func (this *MyLinkedList) AddAtTail(val int)  {
	var lastNode *Node ;
	currentNode := this.header
	for currentNode.next != nil {
		lastNode = currentNode
		currentNode = currentNode.next
	}
	newObj := Node{}
	newObj.val = val
	newObj.next = currentNode
	if lastNode == nil {
		this.header = &newObj
	} else{
		lastNode.next = &newObj
	}
}


func (this *MyLinkedList) AddAtIndex(index int, val int)  {
	var lastNode *Node ;
	currentNode := this.header
	for i:=0 ; i<index; i++ {
		lastNode = currentNode
		currentNode = currentNode.next
		if(currentNode ==  nil){return}
	}
	newObj := Node{}
	newObj.val = val
	newObj.next = currentNode
	if lastNode == nil {
		this.header = &newObj
	} else{
		lastNode.next = &newObj
	}
}


func (this *MyLinkedList) DeleteAtIndex(index int)  {
	var lastNode *Node ;
	currentNode := this.header
	if(index == 0){
		this.header = currentNode.next
	}
	for i:=0 ; i<index; i++ {
		lastNode = currentNode
		currentNode = currentNode.next
		if(currentNode.next ==  nil){return}
	}
	nextNode := currentNode.next
	if(lastNode != nil){
	lastNode.next = nextNode}
}


func (this *MyLinkedList) Print(){
	currentNode := this.header
	for currentNode.next != nil {
		fmt.Print(currentNode.val , " | ")
		currentNode = currentNode.next
	}
	fmt.Println()
}


func main() {
	LinkedList := Constructor();

	//for i:=0 ; i<=10; i++ {
	//	LinkedList.AddAtTail(i)
	//}
	LinkedList.AddAtHead(4)
	LinkedList.Print()
	LinkedList.Get(1)



}