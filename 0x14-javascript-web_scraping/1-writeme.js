#!/usr/bin/node

const { writeFile } = require('fs');
const { argv } = require('process');

const con = argv[3];

writeFile(argv[2], con, 'utf-8', err => {
    if (err) {
        console.Console.log(err);
    }
});