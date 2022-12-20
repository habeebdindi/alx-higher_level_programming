#!/usr/bin/node

function factorial (fact) {
  if (fact < 0) {
    return (-1);
  }
  if (fact === 0 || isNaN(fact)) {
    return (1);
  }
  return (fact * factorial(fact - 1));
}
console.log(factorial(Number(process.argv[2])));
