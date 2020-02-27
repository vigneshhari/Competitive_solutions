/*
Author : Vignesh Hari
Title : Coding train Challenge 1
Date : 26th February 2020
*/


stars = []

const num_stars = 5600
const width = 900
const height = 900
var speed = 20

function setup() {
    createCanvas(width, height);
    for (var i = 0; i < num_stars; i++) {
        stars[i] = new Star()
    }
}

function draw() {
    speed = map(mouseX, 0, width, 0, 50);
    translate(width / 2, height / 2);
    background(0);
    for (var i = 0; i < stars.length; i++) {
        stars[i].update();
        stars[i].show();
    }
}



class Star {

    x = 0
    y = 0
    z = 0
    last_z = 0

    constructor() {
        this.x = random(-width, width)
        this.y = random(-height, height)
        this.z = random(0, height)
        this.last_z = this.z
    }

    update() {
        this.last_z = this.z
        this.z = this.z - speed;
        if (this.z <= 1) {
            this.x = random(-width, width)
            this.y = random(-height, height)
            this.z = height
            this.last_z = this.z

        }

    }


    show() {
        noStroke();
        var old_x = map(this.x / this.last_z, 0, 1, 0, width)
        var old_y = map(this.y / this.last_z, 0, 1, 0, height)

        var new_x = map(this.x / this.z, 0, 1, 0, width)
        var new_y = map(this.y / this.z, 0, 1, 0, height)
        var r = map(this.z, 0, width, 10, 0);

        fill(255)
        ellipse(new_x, new_y, r, r)

        fill(255)
        stroke(255);
        line(old_x, old_y, new_x, new_y);

    }
}