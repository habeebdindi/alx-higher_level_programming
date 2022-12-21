#!/usr/bin/node
const rec = require('./4-rectangle');
module.exports = class Square extends rec {
  constructor (size) {
    super(size, size);
  }
};
