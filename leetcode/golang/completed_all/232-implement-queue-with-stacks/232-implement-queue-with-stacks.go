package main

type MyQueue struct {
	stack1 []int
	stack2 []int
}

func Constructor() MyQueue {
	return MyQueue{[]int{}, []int{}}
}

func (this *MyQueue) Push(x int) {
	this.stack1 = append(this.stack1, x)
}

func (this *MyQueue) Pop() int {
	if len(this.stack2) == 0 {
		for _, j := range this.stack1 {
			this.stack2 = append(this.stack2, j)
			this.stack1 = []int{}
		}
	}
	val := this.stack2[0]
	this.stack2 = this.stack2[1:]
	return val
}

func (this *MyQueue) Peek() int {
	if len(this.stack2) == 0 {
		for _, j := range this.stack1 {
			this.stack2 = append(this.stack2, j)
			this.stack1 = []int{}
		}
	}
	val := this.stack2[0]
	return val
}

func (this *MyQueue) Empty() bool {
	return len(this.stack1) == 0 && len(this.stack2) == 0
}
