#!/usr/bin/node

class Rectangle {
  constructpr (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }
}

module.exports = Rectangle;
