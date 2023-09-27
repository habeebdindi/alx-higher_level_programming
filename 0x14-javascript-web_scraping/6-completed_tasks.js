#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const completed = data.filter(task => task.completed === true);
  const completedByUser = {};

  completed.forEach(task => {
    if (!completedByUser[task.userId]) {
      completedByUser[task.userId] = 1;
    } else {
      completedByUser[task.userId]++;
    }
  });

  console.log(completedByUser);
});
