#!/usr/bin/node
const c = 'C is fun';

if (Number(process.argv[2] === undefined)) {
  console.log('Missing number of occurences');
}
for (let x = 0; x < Number(process.argv[2]); x++) {
  console.log(c);
}
