#!/usr/bin/node
const f = require('fs');
const a = f.readFileSync(`./${process.argv[2]}`);
const b = f.readFileSync(`./${process.argv[3]}`);
f.appendFileSync(`./${process.argv[4]}`, a + b);
