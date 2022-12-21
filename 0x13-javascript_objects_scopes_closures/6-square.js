#!/usr/bin/node
const rect = require('./5-square');

module.exports = class Square extends rect {
  charPrint (c) {
    let printC;
    if (c) {
      printC = c;
    } else {
      printC = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(printC.repeat(this.width));
    }
  }
};
