#!/usr/bin/node
exports.addMeMaybe = function (number, aFunction) {
  aFunction(++number);
};
