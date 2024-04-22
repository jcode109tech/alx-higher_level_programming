#!/usr/bin/node

const times = process.argv[2];
const intTimes = parseInt(times);
let i = 1;

if (isNaN(times)) {
  console.log('Missing number of occurences');
}
for (i = 1; i <= intTimes; i++) {
  console.log('C is fun');
}
