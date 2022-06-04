package main

import "math"

func Solve(a, b, c int) (xpos float64) {
	negB := -b
	twoA := 2 * a
	bSquared := b * b
	fourAC := 4 * a * c
	discrim := bSquared - fourAC
	sq := math.Sqrt(float64(discrim))
	xpos = (float64(negB) + sq) / float64(twoA)
	return xpos
}

func arrangeCoins(n int) int {
	return int(math.Floor(Solve(1, 1, -1*n*2)))
}

func main() {
	print(arrangeCoins(10))
}
