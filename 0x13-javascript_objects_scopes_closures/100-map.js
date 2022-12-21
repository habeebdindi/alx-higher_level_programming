#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const nArr = list.map((product, index) => product * index);
console.log(nArr);
