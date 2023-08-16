#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const rev = [];
  for (let start = len - 1; start > -1; start--) {
    rev.push(list[start]);
  }
  return rev;
};
