#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(Number(a) + Number(b));
  }
}

const a = process.argv[2];
const b = process.argv[3];
add(a, b);
