package main

import (
	"golang.org/x/tour/pic"
)

func Pic(dx, dy int) [][]uint8 {
	a := [][]uint8{}
	for y := 0; y < dy; y++ {
		t := []uint8{0}
		for x := 1; x < dx; x++ {
			val := uint8(-1 * y % x * x)
			t = append(t, val)
		}
		a = append(a, t)
	}
	return a
}

func main() {
	pic.Show(Pic)
}
