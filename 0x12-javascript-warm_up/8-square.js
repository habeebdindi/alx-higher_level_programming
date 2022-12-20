#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
}
let p = 'X';
for (let y = 0; y < Number(process.argv[2]); y++) {
  for (let x = 1; x < Number(process.argv[2]); x++) {
    p += 'X';
  }
  console.log(p);
  p = 'X';
}
