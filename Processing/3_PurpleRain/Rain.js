/*
Author : Vignesh Hari
Title : Coding train Challenge 3 : Purple Rain
Date : 27th February 2020
*/


var rain_drops = []

const num_rain_drops = 500
const width = screen.width
const height = screen.height - (7.31 / 100 * screen.height)
var speed = 10
const min_speed = 5
const drop_len = 50
const max_thickness = 8

function setup() {
    createCanvas(width, height);
    for (var i = 0; i < num_rain_drops; i++) {
        rain_drops[i] = new Drop()
    }
}

function draw() {
    speed = map(mouseX, 0, width, 5, 50);
    //translate(width / 2, height / 2);
    background(230, 230, 250);
    for (var i = 0; i < rain_drops.length; i++) {

        rain_drops[i].update();
        rain_drops[i].show();
    }
}



class Drop {

    max_z = 20

    constructor() {
        this.x = random(0, width)
        this.y = random(0, -100)
        this.z = random(0, this.max_z)
        this.drop_speed = map(this.z, 0, this.max_z, speed - 10, speed)
        this.drop_len = map(this.z, 0, this.max_z, 1, drop_len)
        this.drop_thickness = map(this.z, 0, this.max_z, 1, max_thickness)
        //this.last_z = this.z

    }

    update() {
        if (this.y > height) {
            this.y = random(-100, -200)
            this.x = random(0, width)
            this.z = random(0, 300)
        }
    }


    show() {

        fill(255)
        stroke(138, 43, 226);
        strokeWeight(this.drop_thickness)
        line(this.x, this.y, this.x, this.y + this.drop_len);
        this.y = this.y + this.drop_speed
    }
}