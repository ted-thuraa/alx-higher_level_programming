#!/usr/bin/node

const Esquare = require('./5-square.js');
class Square extends Esquare {
    charPrint (c) {
        if (c === undefined) {
            c = 'X';
        }
        const rep = c.repeat(this.width);
        for (let i = 0; i < this.height; i++) {
            console.log(rep);
        }
    }
} 
module.exports = Square;