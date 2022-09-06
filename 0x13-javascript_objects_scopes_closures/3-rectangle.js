#!/usr/bin/python3

const { modalUnstyledClasses } = require("@mui/material");

class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0) {
            this.width =w;
            this.height = h;
        }
    }

    print () {
        const rep = 'X'.repeat(this.width);
        for (let i = 0; i < this.height; i++) {
            console.log(rep);
        }
    }
}

module.exports = Rectangle;