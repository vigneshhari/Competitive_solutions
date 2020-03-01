/*
Author : Vignesh Hari
Title : Coding train Challenge 5 : Snake
Date : 1st March 2020
*/

const width = screen.width
const height = screen.height - (7.31 / 100 * screen.height)
const size = 20;
const starting_direction = [1, 0]

var s = starting_direction
class Box {

    x = 0;
    y = 0;
    moves = []

    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    set_random_pos() {
        this.x = Math.round(random(0, width - 10))
        this.y = Math.round(random(0, height - 10))
    }

    setmoves(moves) {
        this.moves = moves;
    }

    move() {
        var cur_s = this.moves.shift()
        this.x = this.x + (cur_s[0] * size)
        this.y = this.y + (cur_s[1] * size)
        if (this.x < 0) {
            this.x = width
        } else if (this.x > width) {
            this.x = 0
        }
        if (this.y < 0) {
            this.y = height
        } else if (this.y > height) {
            this.y = 0
        }
    }

    addmove(s) {
        this.moves.push([s[0], s[1]])
    }

    show() {
        rect(this.x, this.y, size, size);
    }

    getlistpos() {
        return [this.x, this.y]
    }

}
class Snake {

    body = []

    constructor(headbox) {
        this.body[0] = headbox
    }


    move() {
        for (var i = 0; i < this.body.length; i++) {
            this.body[i].move()
        }

    }

    show() {
        for (var i = 0; i < this.body.length; i++) {
            fill(255)
            if (i == 0) {
                fill(255, 100, 0)
            }
            this.body[i].show()
        }
    }

    propogate_move(s) {
        for (var i = 0; i < this.body.length; i++) {
            this.body[i].addmove(s)
        }
    }

    create_new() {
        var last_box = this.body[this.body.length - 1]
        var new_box = new Box(last_box.x, last_box.y)
        new_box.setmoves(last_box.moves.slice())
        return new_box
    }

    getheadpos() {
        return [this.body[0].x, this.body[0].y]
    }
}

var food = new Box(0, 0)
var addmore = false
var snake = null


function setup() {
    frameRate(60);
    createCanvas(width, height);
    background(51);
    head_box = new Box(0, 0)
    snake = new Snake(head_box)
    food.set_random_pos()
}


i = 1

function eucDistance(a, b) {
    return a
        .map((x, i) => Math.abs(x - b[i]) ** 2) // square the difference
        .reduce((sum, now) => sum + now) // sum
        **
        (1 / 2)
}

function check_food_collision() {
    current = snake.getheadpos()
    foodpos = food.getlistpos()
    var dis = eucDistance(foodpos, current)
    if (dis < size) {
        food.set_random_pos()
        addmore = true
    }
}

function draw() {
    background(51);
    fill(255);
    noStroke();
    snake.propogate_move(s)
    if (addmore) {
        new_obj = snake.create_new()
        snake.move()
        snake.body.push(new_obj)
        addmore = false
    } else {
        snake.move()
    }
    check_food_collision()
    snake.show()
    fill(255, 0, 100);
    food.show()
}


function keyPressed() {
    if (keyCode === UP_ARROW) {
        s = [0, -1]
    } else if (keyCode === DOWN_ARROW) {
        s = [0, 1];
    } else if (keyCode === RIGHT_ARROW) {
        s = [1, 0];
    } else if (keyCode === LEFT_ARROW) {
        s = [-1, 0];
    }
}