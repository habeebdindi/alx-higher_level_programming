#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (width && width > 0 && height && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let p = 'X';
    for (let y = 0; y < this.height; y++) {
      for (let x = 1; x < this.width; x++) {
        p += 'X';
      }
      console.log(p);
      p = 'X';
    }
  }
};
