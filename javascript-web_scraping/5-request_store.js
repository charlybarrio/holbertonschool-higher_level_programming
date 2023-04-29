#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
