package main

import (
	"fmt"
	"math/rand"
	"time"
)

/*
Creating a 2D Linked List
The First list would be the list with the most elements and the subsequent ones
will be randomly created skip lists
*/


type Node struct {
	val  int   // Actual Value
	previous *Node // Makes it Doubly Linked
	next *Node // Points to next Node
	down *Node // Points to the Node in the Below Height ( Present on all Non Base Lists )
}

type Linkedlist struct {
	header *Node // Points to individual Nodes
	next *Linkedlist // Points to Next List ( Higher List )
	previous *Linkedlist // Points to Previous List ( Lower List )
}

type Skiplist struct {
	header *Linkedlist // The Highest List
	tail *Linkedlist // The Lowest List
	ListHeight int
	TotalElements int
}

func generateRandom() bool {
	return rand.Intn(2) == 1
}

func getmax(a int , b int) int {
	if(a>b){return a}
	return b
}

func (this *Skiplist) CreateOrRetrieveLinkedList(level int) (*Linkedlist){
	this.ListHeight = getmax(this.ListHeight , level)
	var header *Linkedlist = this.tail;
	var previousHeader *Linkedlist = &Linkedlist{}
	// Check if header itself is undefined
	if(header == nil){
		this.header = previousHeader
		this.tail = previousHeader
		newNode := &Node{-1 , nil ,nil, nil }
		this.header.header = newNode
		return previousHeader
	}
	for i:=level;i>1;i--{
		previousHeader = header
		header = header.next
		if(header == nil ){
			newLinkedList := &Linkedlist{previous: previousHeader}
			previousHeader.next = newLinkedList
			newNode := &Node{-1 , nil ,nil , previousHeader.header}
			newLinkedList.header = newNode
			this.header = newLinkedList
			return newLinkedList
		}
	}
	return header
}

func (this *Skiplist) AdvancedSearch(target int , stopLevel int , stopAtFind bool) (bool,bool, *Node) {

	// Start with the highest list
	currentHeight:=this.ListHeight
	var startLinkedList *Linkedlist = this.header
	if(startLinkedList == nil || (this.ListHeight - stopLevel < 0)){return false,true,&Node{}} // Alert that there is no queue present
	// Iterate through the list until the value gets higher than the actual value, if so go down
	startNode := startLinkedList.header
	if(startNode == nil ) {return false,true,&Node{}}
	for startNode != nil{

		if(startNode.next != nil ){
			// If there is a next node check if its smaller than the target, if so move to that , else move down

			if(startNode.next.val > target) {
				// Next Value is larger, return Down
				if(currentHeight == stopLevel){
					// Return at required Level
					return false,false,startNode
				}
				startNode = startNode.down
				currentHeight--
			} else{
				startNode = startNode.next
			}
		} else{
			// The next node is nil , if down node is also nil , return here , else traverse to the down node
			if(startNode.down != nil){
				// If the current value is strictly greater than the target then try again from the starting of the next list
				if(currentHeight == stopLevel){
					// Return at required Level
					return false,false,startNode
				}
				startNode = startNode.down
				currentHeight--
			}else {
				return false,false,startNode
			}
		}
		if(startNode != nil && stopAtFind){
		if(startNode.val == target){
			return true,false, &Node{}
		}}
	}
	// Continue Process until the Value is the Same or when there is no more list to consume

	return false,false, &Node{}
}

func (this *Skiplist) Add(val int) {

	var currentHeight int = 1
	var previousNode *Node = nil;

	for currentHeight <= this.TotalElements {
		// Search Through the Skip List and find the closes element
		var newLinkedListHeader *Linkedlist =  this.CreateOrRetrieveLinkedList(currentHeight)
		valuePresent , listInvalid , closestNode := this.AdvancedSearch(val , currentHeight , false) // If stopAtFind is True it will ignore Duplicates
		if(valuePresent){return}

		var NewNode *Node = &Node{val: val}
		if(listInvalid){
			// Create the Nth Linked List and get the Header Value Back and add the new Node as its header
			NewNode.down = previousNode
			newLinkedListHeader.header = NewNode
		} else{
			NewNode.next = closestNode.next
			NewNode.down = previousNode
			closestNode.next = NewNode
			NewNode.previous = closestNode
			if(NewNode.next != nil){
				NewNode.next.previous = NewNode
			}
		}
		previousNode = NewNode

		// Add the Element Right next to the closest element

		// Get the elements node and start again if the coin toss succeeds else return and stop
		if(!generateRandom()){
			return
		}
		currentHeight += 1
	}
	this.TotalElements++
}

func (this *Skiplist) getList(index int) *Linkedlist {
	return &Linkedlist{}
}

func Constructor() Skiplist {
	rand.Seed(int64(time.Now().UnixNano()))
	return Skiplist{TotalElements: 1 , ListHeight: 0}
}

func (this *Skiplist) Search(target int) bool {
	found , _ , _ :=  this.AdvancedSearch(target , 0 , true)
	return found
}

func (this *Skiplist) Erase(num int) bool {
	// Start with the highest list
	var startLinkedList *Linkedlist = this.header
	if(startLinkedList == nil ){return false} // Alert that there is no queue present
	// Iterate through the list until the value gets higher than the actual value, if so go down
	startNode := startLinkedList.header
	if(startNode == nil ) {return false}
	for startNode.val != num{

		if(startNode.next != nil ){
			// If there is a next node check if its smaller than the target, if so move to that , else move down

			if(startNode.next.val > num) {
				// Next Value is larger, return Down
				if(startNode.down != nil){
					// If the current value is strictly greater than the target then try again from the starting of the next list
					startNode = startNode.down
				}else {
					return false
				}
			} else{
				startNode = startNode.next
			}
		} else{
			// The next node is nil , if down node is also nil , return here , else traverse to the down node
			if(startNode.down != nil){
				// If the current value is strictly greater than the target then try again from the starting of the next list
				startNode = startNode.down
			}else {
				return false
			}
		}
	}
	// Continue Process until the Value is the Same or when there is no more list to consume
    if(startNode.val == num){
		// Go Down and Remove all Occurences
    	for startNode != nil {
    		previousNode := startNode.previous
    		nextNode := startNode.next
    		previousNode.next  = nextNode
    		if(nextNode != nil){
    		nextNode.previous = previousNode}
    		startNode = startNode.down
		}

    	return true
	}
	return false
}



func (this *Skiplist) Print() {
	startHeader := this.header

	for (startHeader != nil){
		currentNode := startHeader.header
		for currentNode != nil {
			fmt.Print(currentNode.val , "|")
			currentNode = currentNode.next
		}
		print("\n")
		startHeader = startHeader.previous
	}
	print("\n \n \n")

}

func main() {
		var todo = []string{"add","add","add","add","add","add","add","add","add","erase","search","add","erase","erase","erase","add","search","search","search","erase","search","add","add","add","erase","search","add","search","erase","search","search","erase","erase","add","erase","search","erase","erase","search","add","add","erase","erase","erase","add","erase","add","erase","erase","add","add","add","search","search","add","erase","search","add","add","search","add","search","erase","erase","search","search","erase","search","add","erase","search","erase","search",  "erase"  ,"erase","search","search","add","add","add","add","search","search","search","search","search","search","search","search","search"}
		var values = [][]int{{16},{5},{14},{13},{0},{3},{12},{9},{12},{3},{6},{7},{0},{1},{10},{5},{12},{7},{16},{7},{0},{9},{16},{3},{2},{17},{2},{17},{0},{9},{14},{1},{6},{1},{16},{9},{10},{9},{2},{3},{16},{15},{12},{7},{4},{3},{2},{1},{14},{13},{12},{3},{6},{17},{2},{3},{14},{11},{0},{13},{2},{1},{10},{17},{0},{5},{8},{9},{8},{11},{10},{11},{10},{9},{8},{15},{14},{1},{6},{17},{16},{13},{4},{5},{4},{17},{16},{7},{14},{1}}

	var CurrentSkiplist Skiplist = Constructor()

		for i,v := range todo {
			action := v
			value := values[i][0]
			fmt.Println("Action " , i , " is " , action , " with value " , value)
			if(action == "add"){
				CurrentSkiplist.Add(value)
			} else if (action == "erase") {
				fmt.Println(CurrentSkiplist.Erase(value))
			} else if ( action == "search"){
				fmt.Println(CurrentSkiplist.Search(value))
			}
		}
		CurrentSkiplist.Print()
		//CurrentSkiplist.Add(0)
		//CurrentSkiplist.Print()
		//CurrentSkiplist.Add(5)
		//CurrentSkiplist.Print()
		//CurrentSkiplist.Add(2)
		//CurrentSkiplist.Print()
		//CurrentSkiplist.Add(1)
		//CurrentSkiplist.Print()
		//fmt.Println(CurrentSkiplist.Search(0))
		//fmt.Println(CurrentSkiplist.Erase(5))
		//fmt.Println(CurrentSkiplist.Search(2))
		//fmt.Println(CurrentSkiplist.Search(3))
		//fmt.Println(CurrentSkiplist.Search(2))
		//fmt.Println()

}
