#!/usr/bin/node
if (process.argv[2] !== undefined && isNaN(process.argv[2]) !== true) {
  console.log('My number: ' + parseInt(process.argv[2], 10));
} else {
  console.log('Not a number');
}
