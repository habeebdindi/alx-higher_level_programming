#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let present = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { present += 1; }
  }
  return (present);
};
