#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const cId = 18;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characterPresent = data.results.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${cId}/`));
    console.log(characterPresent.length);
  }
});
