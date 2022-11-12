package main

import (
	"fmt"
	"math/bits"
)

func isPowerOfTwo(n uint32) bool {
	return bits.OnesCount(uint(n)) == 1
}

func main() {
	fmt.Print("Power of 2 check : ", isPowerOfTwo(20))
}
