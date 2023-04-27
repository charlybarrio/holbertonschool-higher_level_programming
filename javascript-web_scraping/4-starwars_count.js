#!/usr/bin/node
const [, , url] = process.argv;
const request = require('request');

const SWAPI_ORIGINAL_URL = 'https://swapi-api.hbtn.io/api/films/';
const SWAPI_ALX_URL = 'https://swapi-api.alx-tools.com/api/films/';
const apiUrl = url === SWAPI_ORIGINAL_URL ? SWAPI_ALX_URL : url;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    if (film.characters.some(character => character.endsWith('/18/'))) {
      count++;
    }
  }

  console.log(count);
});
