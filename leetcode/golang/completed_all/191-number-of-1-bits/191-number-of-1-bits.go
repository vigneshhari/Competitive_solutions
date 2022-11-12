package main

import (
	"fmt"
	"math/bits"
)

func hammingWeight(num uint32) int {
	return bits.OnesCount(uint(num))
}

func main() {
	fmt.Print("Power of 2 check : ", hammingWeight(20))
}
