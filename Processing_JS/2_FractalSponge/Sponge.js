/*
Author : Vignesh Hari
Title : Coding train Challenge 2 , Fractal Sponge
Date : 26th February 2020
*/

const width = screen.width
const height = screen.height - (7.31 / 100 * screen.height)

var a = 1
var box_list = []


class Box {

    pos = undefined
    size = undefined

    constructor(x, y, z, size) {
        this.pos = createVector(x, y, z);
        this.size = size
    }

    show() {
        push()
        translate(this.pos.x, this.pos.y, this.pos.z);
        //stroke(255);
        noStroke();
        //noFill();
        box(this.size);
        pop()
    }


    generate_squares() {
        var generated_boxes = []
        for (var x = -1; x < 2; x++) {
            for (var y = -1; y < 2; y++) {
                for (var z = -1; z < 2; z++) {
                    if (abs(x) + abs(y) + abs(z) <= 1) {
                        continue
                    }
                    var new_size = this.size / 3
                    var gen_box = new Box(this.pos.x - (new_size * x), this.pos.y - (new_size * y), this.pos.z - (new_size * z), this.size / 3)
                    generated_boxes.push(gen_box)
                }
            }

        }
        return generated_boxes;
    }
}



function setup() {
    createCanvas(width, height, WEBGL);
    box1 = new Box(0, 0, 0, 600)
    box_list.push(box1)
    normalMaterial();
}

function draw() {
    background(20);
    lights()
    rotateX(a);
    rotateY(a * 0.4);
    rotateZ(a * 0.1);
    a += 0.01
    draw_cubes()
}

function draw_cubes() {
    for (var i = 0; i < box_list.length; i++) {
        box_list[i].show();
    }
}



function mousePressed() {
    var new_boxes = []
    for (var i = 0; i < box_list.length; i++) {
        new_boxes = new_boxes.concat(box_list[i].generate_squares());
    }
    box_list = new_boxes
}