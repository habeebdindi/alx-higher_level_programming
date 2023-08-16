#!/usr/bin/node

class Rectangle {
  constructer (w, h) {
    if (w < 1 && h < 1) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
