#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request.get({ url: url }, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const completedUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        completedUser[userId] = (completedUser[userId] || 0) + 1;
      }
    });
    console.log(completedUser);
  }
});
