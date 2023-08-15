#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
    console.log(0);
}

const numbers = args.map(arg => parseInt(arg));
const uniqueNumbers = Array.from(new Set(numbers));

if (uniqueNumbers.length <= 1) {
    console.log(0);
    return;
}

const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);
console.log(sortedNumbers[1]);
