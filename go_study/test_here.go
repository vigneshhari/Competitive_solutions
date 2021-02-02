package main

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

func fibonacci(a ,b , level uint64) uint64 {
		fmt.Println(a)
		if level == 0 {
			return b
		}
		return fibonacci(b, a+b , level-1 )
}

func createFibonacci(reqlevel uint64) uint64 {
	return fibonacci(0,1 , reqlevel - 2)
}

func main() {
	mainQ()
}


func f(from string , timeOut time.Duration) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
		time.Sleep(timeOut)
	}
}

func mainT() {

	f("direct" , 0)

	go f("goroutine 1",time.Second)
	go f("goroutine 2",time.Millisecond * 10)

	go func(msg string) {
		fmt.Println(msg)
	}("going")

	time.Sleep(time.Second * 5)
	fmt.Println("done")
}


func mainW() {

	messages := make(chan string, 2)

	go func() { messages <- "ping" ; time.Sleep(time.Second * 2) ; messages <- "After Timeout" }()

	msg := <-messages
	fmt.Println(msg)
	msg1 := <-messages
	fmt.Println(msg1)
}



func mainQ() {

	var ops,_ops uint64

	var wg sync.WaitGroup

	for i := 0; i < 50; i++ {
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				_ops++;
				atomic.AddUint64(&ops, 1)
			}
			wg.Done()
		}()
	}

	wg.Wait()

	fmt.Println("ops:", ops)
	fmt.Println("_ops:", _ops)

}