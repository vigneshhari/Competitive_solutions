package main

import (
	"math/rand"
	"time"

	p "github.com/bregydoc/PGoJs/Processing"
)

var width = 950
var height = 950
var speed = 1
var num_stars = 1000

type star struct {
	x int
	y int
	z int
}

var stars []star

func setup() {
	p.CreateCanvas(width, height)
	p.Background(0)
	// balls = append(balls, newBall(200, 200, 50))
	p.NoStroke()
	p.Fill(255)
	s2 := rand.NewSource(time.Now().UnixNano())
	r2 := rand.New(s2)
	for i := 0; i <= num_stars; i++ {
		var new_star = star{r2.Intn(width), r2.Intn(height), height}
		stars = append(stars, new_star)
		p.Ellipse(new_star.x, new_star.y, 8, 8)
	}

}

func draw() {
	p.Background(0)
	s2 := rand.NewSource(time.Now().UnixNano())
	r2 := rand.New(s2)
	for idx, val := range stars {
		p.NoStroke()
		p.Fill(255)
		// fmt.Println(val)
		var nx = 0
		var ny = 0
		if val.z <= 1 {
			stars[idx].x = r2.Intn(width)
			stars[idx].y = r2.Intn(height)
			nx = stars[idx].x
			ny = stars[idx].y
			stars[idx].z = height
		} else {
			nx = (val.x / val.z) * width / 2

			ny = (val.y / val.z) * height / 2

			stars[idx].z = val.z - speed
		}
		p.Ellipse(nx, ny, 8, 8)

	}

}

func main() {

	p.Setup = setup
	p.Draw = draw
	// p.MousePressed = mousePressed

	p.LaunchApp()
}
