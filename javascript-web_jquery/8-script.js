#!/usr/bin/node

$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (movie) {
    const movies = $('UL#list_movies');
    for (let i = 0; i < movie.results.length; i++) {
      movies.append(`<li>${movie.results[i].title}</li>`);
    }
  });
});
