#!/usr/bin/node

const request = require('request');
const movie = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movie}`;

request.get({ url }, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(data);
    console.log(movie.title);
  }
});
