#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const todos = JSON.parse(body);
  const completedUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedUser[todo.userId]) {
        completedUser[todo.userId]++;
      } else {
        completedUser[todo.userId] = 1;
      }
    }
  });
  console.log(completedUser);
});
