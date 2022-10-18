#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response, body) => {
    if (error) {
        console.log(error);
    }
    let count = 0;
    const doc = JSON.parse(body).results;
    doc.forEach(p => p.characters.forEach(msg => {
        if (msg.slice(-3, -1) === '18') {
            count++;
        }
    }));
    console.log(count);
});