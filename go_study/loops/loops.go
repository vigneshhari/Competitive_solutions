package main

import (
	"fmt"
)

func sqrt(x float64) float64 {
	var z float64 = 1
	for t := 0; t <= 10; t++ {
		z -= (z*z - x) / (2 * z)
		fmt.Println(z)
	}
	return z
}

func main() {
	fmt.Println(sqrt(625))
}
