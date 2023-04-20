#!/usr/bin/node

const request = require('request');

const Url = process.argv[2];

request.get(Url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);

  const filmsWithWedge = data.results.filter(film =>
    film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')
  );
  console.log(filmsWithWedge.length);
});
