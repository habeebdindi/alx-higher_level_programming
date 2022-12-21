#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (width && width > 0 && height && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
};
