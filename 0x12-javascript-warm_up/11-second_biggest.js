#!/usr/bin/node
let arr = 0;
if (process.argv.length <= 3) {
  console.log(arr);
} else {
  arr = process.argv.slice(2);
  arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
