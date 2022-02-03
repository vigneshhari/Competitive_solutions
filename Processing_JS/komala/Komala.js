/*
Author : Vignesh Hari
Title : Dey Komala ( Poli Sanam )
Date : 26th February 2020
*/

const width = 900;
const height = 900;
const num_stars = 1500;
const speed = 2;
const enable_color = true;
const minnal_bg = true;
const komala_transparency = 150;


var komalas = [];


class Komala {

    x = 0;
    y = 0;
    z = 0;
    last_z = 0;
    cr = 0;
    cg = 0;
    cb = 0;

    constructor() {
        this.x = random(-width, width);
        this.y = random(-height, height);
        this.z = random(0, height);
        this.last_z = this.z;
        this.cr = random(255);
        this.cg = random(255);
        this.cb = random(255);
    }

    update() {
        this.last_z = this.z;
        this.z = this.z - speed;
        if (this.z <= 1) {
            this.x = random(-width, width)
            this.y = random(-height, height)
            this.z = height
        }
    }

    show() {
        var new_x = map(this.x / this.z, 0, 1, 0, width);
        var new_y = map(this.y / this.z, 0, 1, 0, height);
        var r = map(this.z, 0, width, 500, 0);
        if (enable_color) {
            strokeWeight(2);
            stroke(this.cr, this.cg, this.cb);
            fill(this.cr, this.cg, this.cb, komala_transparency);
        }
        ellipse(new_x, new_y, r, r);
    }
}

function setup() {
    createCanvas(width, height);
    for (var i = 0; i < num_stars; i++) {
        komalas[i] = new Komala();
    }
}

function draw() {
    translate(width / 2, height / 2);
    if (minnal_bg) {
        background(random(255), random(255), random(255));
    } else {
        background(0)
    }
    for (var i = 0; i < komalas.length; i++) {
        komalas[i].update();
        komalas[i].show();
    }
}